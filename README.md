```markdown
# MCP Servers Collection

This repository hosts five Model Context Protocol (MCP) servers you can mount into Claude Desktop:

1. **line-bot**  
2. **email_mcp**  
3. **fetch**  
4. **word-document-service**  
5. **filesystem**  

---

## 🚀 Quick Start

1. **Clone & enter**  
   ```bash
   git clone https://github.com/iamkaia/email-mcp-server-simple.git
   cd email-mcp-server-simple
   ```

2. **Set up Python env** (for _email_mcp_, _fetch_, _word-document-service_)  
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Fill `.env`** (for `email_mcp` only—do **not** commit):
   ```ini
   # SMTP
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   SMTP_USERNAME=you@example.com
   SMTP_PASSWORD=your_smtp_password

   # IMAP
   IMAP_SERVER=imap.example.com
   IMAP_PORT=993
   IMAP_USERNAME=you@example.com
   IMAP_PASSWORD=your_imap_password
   ```

4. **Install Node dependencies** (for _line-bot_ and _filesystem_):
   ```bash
   cd line-bot-mcp-server && npm install && cd ..
   # filesystem uses npx/@modelcontextprotocol, no local build needed
   ```

5. **Start each server** (in separate terminals):
   ```bash
   # email_mcp + fetch + word-document-service
   uvicorn email_mcp.main:app --host 0.0.0.0 --port 8000
   uvicorn fetch.main:app    --host 0.0.0.0 --port 8001
   uvicorn word-doc.main:app --host 0.0.0.0 --port 8002
   ```
   ```bash
   # line-bot
   cd line-bot-mcp-server
   node dist/index.js
   ```
   ```bash
   # filesystem (via NPX)
   npx -y @modelcontextprotocol/server-filesystem \
     "C:/Users/Grace Ho/OneDrive/Desktop" \
     "C:/Users/Grace Ho/OneDrive/Documents"
   ```

---

## 🔧 Claude Desktop Configuration

Edit your `claude_desktop_config.json` to spawn each MCP tool:

```jsonc
{
  "mcpServers": {
    "line-bot": {
      "command": "node",
      "args": ["C:/…/line-bot-mcp-server/dist/index.js"],
      "env": {
        "CHANNEL_ACCESS_TOKEN": "...",
        "DESTINATION_USER_ID": "..."
      }
    },
    "email_mcp": {
      "command": "C:/…/mcp-proxy.exe",
      "args": ["http://localhost:8000/mcp"]
    },
    "fetch": {
      "command": "C:/…/mcp-proxy.exe",
      "args": ["http://localhost:8001/mcp"]
    },
    "word-document-service": {
      "command": "C:/…/mcp-proxy.exe",
      "args": ["http://localhost:8002/mcp"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "--yes",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Grace Ho/OneDrive/Desktop",
        "C:/Users/Grace Ho/OneDrive/Documents"
      ]
    }
  }
}
```

After saving, **quit & restart** Claude Desktop. The 🔨 Tools menu will list all available MCP tools.

---

## 📦 Servers & Tools

### 1. **line-bot**  
- **Tools**: `send_line_message`  
- **Push** messages into a Line chat.

### 2. **email_mcp**  
- **Tools**: `send_email`, `list_recent_emails`

### 3. **fetch**  
- **Tools**: `fetch_page`  
- **Input**: `url` ⇒ **Output**: title, headings, snippet.

### 4. **word-document-service**  
- **Tools**:  
  - `create_document`, `add_heading`, `insert_table`, `format_text`, `search_replace`, …  
- **Manipulate** DOCX files programmatically.

### 5. **filesystem**  
- **Tools**:  
  - `read_file`, `write_file`, `list_directory`, `search_files`, `get_file_info`, …  
- **Operate** only within the mounted directories.

---

## 🎯 Example JSON‑RPC Calls

```json
// send_email
{
  "tool":"send_email",
  "input":{"params":{
    "to":["friend@example.com"],
    "subject":"Hello",
    "body":"This is a test.",
    "html":false
  }}
}

// list_recent_emails
{
  "tool":"list_recent_emails",
  "input":{"params":{
    "limit":3
  }}
}

// fetch_page
{
  "tool":"fetch_page",
  "input":{"params":{"url":"https://example.com"}}
}

// create a Word doc
{
  "tool":"create_document",
  "input":{"params":{"filename":"report.docx","title":"Sales Report"}}
}

// filesystem read
{
  "tool":"read_file",
  "input":{"params":{"path":"C:/Users/Grace Ho/OneDrive/Desktop/notes.txt"}}
}
```

---

## 📃 License

All servers are MIT‑licensed. See each subfolder’s LICENSE for details.