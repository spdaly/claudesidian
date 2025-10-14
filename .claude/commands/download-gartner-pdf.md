---
allowed-tools: [WebFetch, Bash, Write, Read]
description: Download Gartner research articles as PDF files
argument-hint: <gartner-url> [output-folder]
---

# Download Gartner PDF

Downloads Gartner research articles from provided URLs and saves them as PDF files.

## Task

Given a Gartner research URL (or multiple URLs), fetch the content and save it as a well-formatted PDF file with proper metadata and citation information.

## Arguments

- **gartner-url** (required): Full Gartner document URL (e.g., https://www.gartner.com/document/code/XXXXXX)
- **output-folder** (optional): Target folder for PDF output. Defaults to `05_Attachments/`

## Process

1. **Validate URL**: Confirm the URL is a valid Gartner document link
2. **Fetch Content**: Use WebFetch to retrieve the full article content
3. **Extract Metadata**:
   - Article title
   - Author(s)
   - Publication date
   - Document ID
   - Abstract/summary
4. **Format Content**:
   - Clean HTML formatting
   - Preserve headings, lists, and tables
   - Include citation information
5. **Generate PDF**:
   - Use system tools (wkhtmltopdf, pandoc, or chrome headless)
   - Include proper page breaks
   - Add header with Gartner branding
   - Include footer with citation
6. **Save File**:
   - Filename format: `Gartner [YYYY] - [Title].pdf`
   - Save to specified output folder
   - Create corresponding markdown note with link

## Output

- PDF file saved to output folder
- Markdown note created with:
  - Frontmatter (title, source, author, date)
  - Link to PDF
  - Article summary
  - Key findings

## Example Usage

```bash
# Single article
/download-gartner-pdf https://www.gartner.com/document/code/772600

# Specify output folder
/download-gartner-pdf https://www.gartner.com/document/code/772600 03_Resources/Gartner/

# Multiple articles (run command multiple times or provide space-separated URLs)
/download-gartner-pdf https://www.gartner.com/document/code/772600 https://www.gartner.com/document/code/347617
```

## Notes

- Requires Gartner subscription/access
- PDF generation requires system dependencies (wkhtmltopdf or chrome)
- Large articles may take 30-60 seconds to process
- Failed downloads will provide error details

## Technical Requirements

The command will attempt to use available PDF generation tools in this order:
1. Chrome/Chromium headless (via playwright/chrome-devtools)
2. wkhtmltopdf (if installed)
3. Pandoc (if installed)
4. Fallback: Save as formatted HTML with print stylesheet

If no PDF tools are available, the command will save rich markdown instead and notify the user about PDF generation options.
