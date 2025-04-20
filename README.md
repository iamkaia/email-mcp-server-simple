```markdown
# Email MCP Server

A FastAPI service exposing two MCP tools to Claude Desktop:

- **send_email**: send SMTP email  
- **list_recent_emails**: list recent IMAP messages (default limit 3)

---

## 🔧 Setup

1. **Copy & fill `.env`** (do **not** commit):
   ```ini
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   SMTP_USERNAME=you@example.com
   SMTP_PASSWORD=your_smtp_password

   IMAP_SERVER=imap.example.com
   IMAP_PORT=993
   IMAP_USERNAME=you@example.com
   IMAP_PASSWORD=your_imap_password
   ```
2. **Create a virtualenv** and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install fastapi uvicorn fastapi-mcp pydantic pydantic-settings python-dotenv
   ```
3. **Start the server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 🔗 Claude Desktop Integration

1. (Optional) **SSH tunnel** if the server is remote:
   ```bash
   ssh -N -L 9000:localhost:8000 user@remote.host
   ```
2. **Install** the local bridge:
   ```bash
   pip install mcp-proxy
   ```
3. **Edit** your `claude_desktop_config.json`:
   ```jsonc
   {
     "mcpServers": {
       "email_mcp": {
         "command": "/full/path/to/mcp-proxy",
         "args": ["http://localhost:9000/mcp"]
       }
     }
   }
   ```
4. **Quit & restart** Claude Desktop.  
   You should see **send_email** and **list_recent_emails** in the 🔨 Tools menu.

---

## ▶️ Usage Examples

- **Natural language**:  
  “Send an email to me@example.com with subject ‘Hi’ and body ‘Hello from MCP!’”  
- **Tool form**:  
  Click **list_recent_emails**, set `limit=3`, then Run.

---

## Troubleshooting

- **Login fails**: use an app‑specific password (e.g. Gmail 2FA).  
- **Timeouts**: default MCP timeout is 5 s—reduce `limit` or optimize IMAP logic.  
- **No tools**: confirm `mcp-proxy` args and fully restart Claude Desktop.  
```