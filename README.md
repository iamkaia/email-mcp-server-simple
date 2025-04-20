```markdown
# Email MCP Server

A FastAPI-based MCP service exposing two tools to Claude Desktop:

- **send_email**: send an email via SMTP  
- **list_recent_emails**: fetch recent emails from an IMAP server  

---

## Tools

| Name                 | Description                         |
|----------------------|-------------------------------------|
| `send_email`         | Send an email via SMTP              |
| `list_recent_emails` | List recent messages from IMAP      |

---

## Configuration

Create a `.env` file in the project root (add it to `.gitignore`):

# SMTP (sending) settings
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=you@example.com
SMTP_PASSWORD=your_smtp_password

# IMAP (fetching) settings
IMAP_SERVER=imap.example.com
IMAP_PORT=993
IMAP_USERNAME=you@example.com
IMAP_PASSWORD=your_imap_password
```

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate      # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt  


```

---

## Running

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## Claude Desktop Integration

1. (If remote) open an SSH tunnel:
   ```bash
   ssh -N -L 9000:localhost:8000 user@remote.host
   ```
2. Install the bridge:
   ```bash
   pip install mcp-proxy
   ```
3. Edit your `claude_desktop_config.json`:
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
4. Quit & restart Claude Desktop → you will see:
   - `send_email`
   - `list_recent_emails`

---

## Usage Examples

### send_email

```json
{
  "tool": "send_email",
  "input": {
    "params": {
      "to": ["receiver@example.com"],
      "subject": "Test Email",
      "body": "Hello from MCP!",
      "html": false
    }
  }
}
```

### list_recent_emails

```json
{
  "tool": "list_recent_emails",
  "input": {
    "params": {
      "imap_server": "imap.gmail.com",
      "username": "you@example.com",
      "password": "your_imap_password",
      "limit": 5
    }
  }
}
```
```