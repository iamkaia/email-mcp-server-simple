from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel, EmailStr, Field
from typing import List
import smtplib, imaplib, email
from email.message import EmailMessage
from pydantic_settings import BaseSettings, SettingsConfigDict

# 0) .env 里读 SMTP/IMAP 配置
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    smtp_server: str
    smtp_port: int = 587
    smtp_username: EmailStr
    smtp_password: str
    imap_server: str
    imap_port: int = 993
    imap_username: EmailStr
    imap_password: str

settings = Settings()

# 1) 定义 Pydantic 模型
class SendEmailParams(BaseModel):
    to: List[EmailStr]
    subject: str
    body: str
    html: bool = False

class SendEmailResult(BaseModel):
    success: bool
    error: str = ""

class ListEmailsParams(BaseModel):
    mailbox: str = "INBOX"
    limit: int = Field(3, ge=1, le=5)

class EmailItem(BaseModel):
    uid: str
    subject: str
    from_addr: str
    date: str
    snippet: str

class ListEmailsResult(BaseModel):
    emails: List[EmailItem]

# 2) 业务实现
def send_email_logic(params: SendEmailParams) -> SendEmailResult:
    try:
        msg = EmailMessage()
        msg["Subject"] = params.subject
        msg["From"] = settings.smtp_username
        msg["To"] = ", ".join(params.to)
        if params.html:
            msg.add_alternative(params.body, subtype="html")
        else:
            msg.set_content(params.body)
        with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(settings.smtp_username, settings.smtp_password)
            smtp.send_message(msg)
        return SendEmailResult(success=True)
    except Exception as e:
        return SendEmailResult(success=False, error=str(e))

def list_recent_emails_logic(params: ListEmailsParams) -> ListEmailsResult:
    try:
        imap = imaplib.IMAP4_SSL(settings.imap_server, settings.imap_port)
        imap.login(settings.imap_username, settings.imap_password)
        imap.select(params.mailbox)
        typ, data = imap.search(None, "ALL")
        uids = data[0].split()[::-1][: params.limit]
        items = []
        for uid in uids:
            _, msg_data = imap.fetch(uid, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            snippet = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        snippet = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                snippet = msg.get_payload(decode=True).decode(errors="ignore")
            items.append(EmailItem(
                uid=uid.decode(),
                subject=msg.get("Subject",""),
                from_addr=msg.get("From",""),
                date=msg.get("Date",""),
                snippet=snippet[:200].replace("\n"," "),
            ))
        imap.logout()
        return ListEmailsResult(emails=items)
    except Exception as e:
        raise HTTPException(500, detail=f"IMAP error: {e}")

# 3) FastAPI + 路由
app = FastAPI()

@app.post(
    "/send_email",
    operation_id="send_email",       # ← 这个就是你给 MCP 工具的名字
    response_model=SendEmailResult,
    summary="Send an email"
)
def send_email_endpoint(params: SendEmailParams):
    return send_email_logic(params)

@app.post(
    "/list_recent_emails",
    operation_id="list_recent_emails",
    response_model=ListEmailsResult,
    summary="List recent emails"
)
def list_recent_emails_endpoint(params: ListEmailsParams):
    return list_recent_emails_logic(params)

# 4) 挂载 MCP（默认就是 /mcp SSE）
mcp = FastApiMCP(
    app,
    name="EmailMCP",                         # 可随便起
    base_url="http://localhost:8000",        # 你的服务外部可访问地址   
)
mcp.mount()

# === 啟動服務 ===
# 使用：
#   uvicorn main:app --reload --host 0.0.0.0 --port 8000