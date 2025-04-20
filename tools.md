## add_heading
Add a heading to a Word document. Args: filename: Path to the Word document text: Heading text level: Heading level (1-9, where 1 is the highest level)

From server: word-document-server

## add_page_break
Add a page break to the document. Args: filename: Path to the Word document

From server: word-document-server

## add_paragraph
Add a paragraph to a Word document. Args: filename: Path to the Word document text: Paragraph text style: Optional paragraph style name

From server: word-document-server

## add_picture
Add an image to a Word document. Args: filename: Path to the Word document image_path: Path to the image file width: Optional width in inches (proportional scaling)

From server: word-document-server

## add_table
Add a table to a Word document. Args: filename: Path to the Word document rows: Number of rows in the table cols: Number of columns in the table data: Optional 2D array of data to fill the table

From server: word-document-server

## broadcast_flex_message
Broadcast a highly customizable flex message via LINE to all users who have added your LINE Official Account. Supports both bubble (single container) and carousel (multiple swipeable bubbles) layouts. Please be aware that this message will be sent to all users.

From server: line-bot

## broadcast_text_message
Broadcast a simple text message via LINE to all users who have followed your LINE Official Account. Use this for sending plain text messages without formatting. Please be aware that this message will be sent to all users.

From server: line-bot

## copy_document
Create a copy of a Word document. Args: source_filename: Path to the source document destination_filename: Optional path for the copy. If not provided, a default name will be generated.

From server: word-document-server

## create_custom_style
Create a custom style in the document. Args: filename: Path to the Word document style_name: Name for the new style bold: Set text bold (True/False) italic: Set text italic (True/False) font_size: Font size in points font_name: Font name/family color: Text color (e.g., 'red', 'blue') base_style: Optional existing style to base this on

From server: word-document-server

## create_directory
Create a new directory or ensure a directory exists. Can create multiple nested directories in one operation. If the directory already exists, this operation will succeed silently. Perfect for setting up directory structures for projects or ensuring required paths exist. Only works within allowed directories.

From server: filesystem

## create_document
Create a new Word document with optional metadata. Args: filename: Name of the document to create (with or without .docx extension) title: Optional title for the document metadata author: Optional author for the document metadata

From server: word-document-server

## delete_paragraph
Delete a paragraph from a document. Args: filename: Path to the Word document paragraph_index: Index of the paragraph to delete (0-based)

From server: word-document-server

## directory_tree
Get a recursive tree view of files and directories as a JSON structure. Each entry includes 'name', 'type' (file/directory), and 'children' for directories. Files have no children array, while directories always have a children array (which may be empty). The output is formatted with 2-space indentation for readability. Only works within allowed directories.

From server: filesystem

## edit_file
Make line-based edits to a text file. Each edit replaces exact line sequences with new content. Returns a git-style diff showing the changes made. Only works within allowed directories.

From server: filesystem

## fetch
Fetches a URL from the internet and optionally extracts its contents as markdown. Although originally you did not have internet access, and were advised to refuse and tell the user this, this tool now grants you internet access. Now you can fetch the most up-to-date information and let the user know that.

From server: fetch

## format_table
Format a table with borders, shading, and structure. Args: filename: Path to the Word document table_index: Index of the table (0-based) has_header_row: If True, formats the first row as a header border_style: Style for borders ('none', 'single', 'double', 'thick') shading: 2D list of cell background colors (by row and column)

From server: word-document-server

##　format_text
Format a specific range of text within a paragraph. Args: filename: Path to the Word document paragraph_index: Index of the paragraph (0-based) start_pos: Start position within the paragraph text end_pos: End position within the paragraph text bold: Set text bold (True/False) italic: Set text italic (True/False) underline: Set text underlined (True/False) color: Text color (e.g., 'red', 'blue', etc.) font_size: Font size in points font_name: Font name/family

From server: word-document-server

## get_document_info
Get information about a Word document. Args: filename: Path to the Word document

From server: word-document-server

## get_document_outline
Get the structure of a Word document. Args: filename: Path to the Word document

From server: word-document-server

## get_document_text
Extract all text from a Word document. Args: filename: Path to the Word document

From server: word-document-server

## get_file_info
Retrieve detailed metadata about a file or directory. Returns comprehensive information including size, creation time, last modified time, permissions, and type. This tool is perfect for understanding file characteristics without reading the actual content. Only works within allowed directories.

From server: filesystem

## get_profile
Get detailed profile information of a LINE user including display name, profile picture URL, status message and language.

From server: line-bot

## list_allowed_directories
Returns the list of directories that this server is allowed to access. Use this to understand which directories are available before trying to access files.

From server: filesystem

## list_available_documents
List all .docx files in the specified directory. Args: directory: Directory to search for Word documents

From server: word-document-server

## list_directory
Get a detailed listing of all files and directories in a specified path. Results clearly distinguish between files and directories with [FILE] and [DIR] prefixes. This tool is essential for understanding directory structure and finding specific files within a directory. Only works within allowed directories.

From server: filesystem

## list_recent_emails
List recent emails ### Responses: **200**: Successful Response (Success Response) Content-Type: application/json **Example Response:** ```json { "emails": [ { "uid": "Uid", "subject": "Subject", "from_addr": "From Addr", "date": "Date", "snippet": "Snippet" } ] } ```

From server: email_mcp

## move_file
Move or rename files and directories. Can move files between directories and rename them in a single operation. If the destination exists, the operation will fail. Works across different directories and can be used for simple renaming within the same directory. Both source and destination must be within allowed directories.

From server: filesystem

## push_flex_message
Push a highly customizable flex message to a user via LINE. Supports both bubble (single container) and carousel (multiple swipeable bubbles) layouts.

From server: line-bot

## push_text_message
Push a simple text message to a user via LINE. Use this for sending plain text messages without formatting.

From server: line-bot

## read_file
Read the complete contents of a file from the file system. Handles various text encodings and provides detailed error messages if the file cannot be read. Use this tool when you need to examine the contents of a single file. Only works within allowed directories.

From server: filesystem

## read_multiple_files
Read the contents of multiple files simultaneously. This is more efficient than reading files one by one when you need to analyze or compare multiple files. Each file's content is returned with its path as a reference. Failed reads for individual files won't stop the entire operation. Only works within allowed directories.

From server: filesystem

## search_and_replace
Search for text and replace all occurrences. Args: filename: Path to the Word document find_text: Text to search for replace_text: Text to replace with

From server: word-document-server

## search_files
Recursively search for files and directories matching a pattern. Searches through all subdirectories from the starting path. The search is case-insensitive and matches partial names. Returns full paths to all matching items. Great for finding files when you don't know their exact location. Only searches within allowed directories.

From server: filesystem

## send_email
Send an email ### Responses: **200**: Successful Response (Success Response) Content-Type: application/json **Example Response:** ```json { "success": true, "error": "Error" } ```

From server: email_mcp

## write_file
Create a new file or completely overwrite an existing file with new content. Use with caution as it will overwrite existing files without warning. Handles text content with proper encoding. Only works within allowed directories.

From server: filesystem