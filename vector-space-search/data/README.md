```markdown
# Data Directory Structure

This directory contains the dataset files used for the Vector Space Search Engine.

## Directory Layout
- `raw/`: Contains raw document collections (JSON / Text format).
- `processed/`: Stores generated token lists, vocabulary files, and serialized inverted index mapping.

## Dataset Schema
The input files in `raw/` follow a standard JSON list format:
```json
{
  "id": "integer - Unique document identifier",
  "title": "string - Title of the document",
  "content": "string - Full text content"
}
