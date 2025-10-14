---
allowed-tools: [
  mcp__playwright__browser_navigate,
  mcp__playwright__browser_snapshot,
  mcp__playwright__browser_type,
  mcp__playwright__browser_click,
  mcp__playwright__browser_wait_for,
  mcp__playwright__browser_evaluate,
  mcp__playwright__browser_close,
  mcp__playwright__browser_take_screenshot,
  Bash,
  Write,
  Read
]
description: Automated Gartner document search and batch PDF download using browser automation
argument-hint: <search-keyword> [--count N] [--output-dir DIR]
---

# Gartner Batch Download

Automates logging into Gartner.com, searching for documents by keyword, and downloading the top N results as PDF files using Playwright browser automation.

## WARNING

**This command is experimental and requires:**
- Active Gartner subscription with valid credentials
- Playwright MCP server properly configured
- Initial testing with small batches (--count 2-3)

**IMPORTANT:** Gartner's website structure may change. First run will help identify actual page selectors. Be prepared to troubleshoot and adapt.

## Prerequisites

Before running this command, complete the following setup:

### 1. Configure Gartner Credentials

Create or edit `.env` file in your project root:

```bash
# Add these lines to .env
GARTNER_USERNAME=your-email@example.com
GARTNER_PASSWORD=your-password
```

Verify `.env` is in `.gitignore`:
```bash
grep -q "^\.env$" .gitignore || echo ".env" >> .gitignore
```

### 2. Verify Playwright MCP Server

Ensure Playwright MCP server is running and configured in your Claude Code settings.

### 3. Check Output Directory

Default output: `05_Attachments/Gartner/[search-keyword]/`

The command will create directories as needed.

## Arguments

- **search-keyword** (required): Search term for Gartner research documents
- **--count N** (optional): Number of documents to download (default: 10, max: 20)
- **--output-dir DIR** (optional): Custom output directory (default: `05_Attachments/Gartner/`)

## Usage Examples

```bash
# Basic search and download (10 documents)
/gartner-batch-download "application rationalization"

# Download only top 5 results
/gartner-batch-download "AI governance" --count 5

# Custom output directory
/gartner-batch-download "cloud strategy" --output-dir 03_Resources/Research/

# Testing with minimal downloads
/gartner-batch-download "test search" --count 2
```

## Process Overview

The command executes in 4 phases:

```
PHASE 1: AUTHENTICATION
├── Check environment variables for credentials
├── Launch Playwright browser
├── Navigate to Gartner login page
├── Fill and submit login form
└── Verify successful authentication

PHASE 2: SEARCH & EXTRACT
├── Navigate to Gartner search page
├── Enter search keyword
├── Wait for results to load
├── Extract top N article URLs and metadata
└── Display found articles

PHASE 3: BATCH DOWNLOAD
├── For each article (with 5-second delays):
│   ├── Navigate to article page
│   ├── Find PDF download mechanism
│   ├── Trigger download
│   ├── Verify and rename file
│   └── Track success/failure
└── Continue on individual failures

PHASE 4: CLEANUP & REPORT
├── Close browser session
├── Generate summary report
├── Create markdown note with links to downloaded files
└── Display success statistics
```

## Detailed Implementation

### PHASE 1: Authentication

1. **Check Credentials**
   - Read `GARTNER_USERNAME` and `GARTNER_PASSWORD` from environment
   - If missing: Display setup instructions and EXIT
   - Never proceed without valid credentials

2. **Browser Launch & Login**
   ```
   Tool: browser_navigate
   URL: https://www.gartner.com/account/signin
   ```

3. **Take Snapshot to Identify Form Elements**
   ```
   Tool: browser_snapshot
   Purpose: Find login form field references
   ```

4. **Fill Credentials**
   ```
   Tool: browser_type (email field)
   Element: [ref from snapshot - typically input[type="email"]]
   Value: $GARTNER_USERNAME

   Tool: browser_type (password field)
   Element: [ref from snapshot - typically input[type="password"]]
   Value: $GARTNER_PASSWORD
   ```

5. **Submit Login**
   ```
   Tool: browser_click
   Element: [submit button from snapshot]
   ```

6. **Verify Login Success**
   ```
   Tool: browser_wait_for
   Text: "Search" OR user profile indicator
   Timeout: 30 seconds
   ```

7. **Confirm Authentication**
   ```
   Tool: browser_snapshot
   Purpose: Verify we're on logged-in dashboard/home page
   ```

**Error Handling:**
- If credentials missing → Display setup instructions, EXIT
- If login fails → Take screenshot, report error, EXIT
- If timeout → Retry once, then EXIT

---

### PHASE 2: Search Execution

1. **Navigate to Search Page**
   ```
   Tool: browser_navigate
   URL: https://www.gartner.com/en/search
   ```

2. **Identify Search Input**
   ```
   Tool: browser_snapshot
   Purpose: Find search input field reference
   ```

3. **Enter Search Keyword**
   ```
   Tool: browser_type
   Element: [search input ref from snapshot]
   Value: [user-provided search keyword]
   Submit: true (press Enter after typing)
   ```

4. **Wait for Results**
   ```
   Tool: browser_wait_for
   Text: "results" OR result count indicator
   Timeout: 30 seconds
   ```

5. **Take Results Snapshot**
   ```
   Tool: browser_snapshot
   Purpose: View result structure before extraction
   ```

6. **Extract Article Metadata**
   ```
   Tool: browser_evaluate
   JavaScript:
   () => {
     const results = [];
     // SELECTOR NOTE: These may need adjustment after first run
     const items = document.querySelectorAll('.search-result-item, [data-testid="search-result"]');

     for (let i = 0; i < Math.min([user-count], items.length); i++) {
       const item = items[i];
       const titleElem = item.querySelector('.title, h3, [data-testid="title"]');
       const linkElem = item.querySelector('a[href*="/documents/"]');
       const docIdElem = item.querySelector('.doc-id, [data-testid="doc-id"]');
       const dateElem = item.querySelector('.pub-date, time, [data-testid="date"]');

       if (titleElem && linkElem) {
         results.push({
           title: titleElem.textContent.trim(),
           url: linkElem.href,
           docId: docIdElem?.textContent?.trim() || 'Unknown',
           date: dateElem?.textContent?.trim() || 'Unknown'
         });
       }
     }

     return results;
   }
   ```

7. **Display Found Articles**
   - Show user the list of articles that will be downloaded
   - Confirm count matches expectation
   - Provide option to continue or abort

**Error Handling:**
- No results found → Report to user, EXIT
- Cannot parse results → Take snapshot, report selector issue, EXIT
- Fewer results than requested → Continue with available results

---

### PHASE 3: Batch Download Loop

**CRITICAL NOTE:** PDF download mechanism in Playwright may require special handling. The command will attempt multiple strategies.

**For Each Article in Results:**

1. **Navigate to Article Page**
   ```
   Tool: browser_navigate
   URL: [article.url]
   Timeout: 30 seconds
   ```

2. **Wait for Content Load**
   ```
   Tool: browser_wait_for
   Text: Article title OR "Download" OR "PDF"
   Timeout: 30 seconds
   ```

3. **Take Page Snapshot**
   ```
   Tool: browser_snapshot
   Purpose: Identify PDF download button/link
   ```

4. **Attempt Download - Strategy A: Direct Download Button**
   ```
   Tool: browser_click
   Element: [PDF download button from snapshot]
   Common selectors:
   - button containing "Download PDF"
   - a[href$=".pdf"]
   - [data-testid="download-pdf"]
   ```

5. **Wait for Download**
   ```
   Tool: Bash
   Command: sleep 5 && ls -t ~/Downloads/*.pdf | head -1
   Purpose: Find most recent PDF in downloads folder
   ```

6. **Verify Download Success**
   ```
   Tool: Bash
   Command: Check if new PDF exists and is > 0 bytes
   ```

7. **Rename and Move File**
   ```
   Tool: Bash
   Command: mv [downloaded-file] [target-directory]/Gartner - [clean-title] ([docId]).pdf

   Filename format:
   - Remove special characters from title
   - Limit title to 100 characters
   - Include document ID for reference
   - Example: "Gartner - 7 Steps to Rationalize Your App Portfolio (G006327847).pdf"
   ```

8. **Rate Limiting Delay**
   ```
   Tool: Bash
   Command: sleep 5
   Purpose: Avoid triggering Gartner rate limits
   ```

9. **Track Result**
   - If successful: Add to success list
   - If failed: Add to failure list with error details
   - Continue to next article regardless

**Fallback Strategy B: Print to PDF**

If Strategy A fails (no download button found):

```
Tool: browser_evaluate
JavaScript:
() => {
  window.print();
  return "Print dialog triggered";
}

Note: This may require manual intervention to save as PDF
```

**Fallback Strategy C: Content Extraction**

If both A and B fail:

```
Tool: browser_evaluate
JavaScript:
() => {
  const article = document.querySelector('article, .article-content, main');
  return {
    html: article?.innerHTML || document.body.innerHTML,
    text: article?.textContent || document.body.textContent
  };
}

Then use Bash with wkhtmltopdf or pandoc to generate PDF from HTML
```

**Error Handling:**
- Page load timeout → Skip article, log failure
- PDF button not found → Try fallback strategies
- Download timeout → Skip article, log failure
- File rename error → Log warning, use fallback naming
- Network error → Retry once, then skip

---

### PHASE 4: Cleanup & Reporting

1. **Close Browser**
   ```
   Tool: browser_close
   ```

2. **Organize Files**
   ```
   Tool: Bash
   Create directory structure:
   05_Attachments/Gartner/
   └── [search-keyword]/
       ├── Gartner - Article 1 (G00123456).pdf
       ├── Gartner - Article 2 (G00234567).pdf
       └── ...
   ```

3. **Generate Summary Report**
   ```
   Tool: Write
   File: 05_Attachments/Gartner/batch-download-log-[timestamp].md
   ```

4. **Create Obsidian Note**
   ```
   Tool: Write
   File: 03_Resources/Gartner/[search-keyword] - Batch Download Results.md

   Content:
   - Links to all downloaded PDFs
   - Failed download list with manual URLs
   - Statistics and metadata
   ```

5. **Display Summary**
   - Total articles found
   - Successfully downloaded count
   - Failed download count
   - File locations
   - Next steps for failures

---

## Output Files

### Downloaded PDFs
```
05_Attachments/Gartner/[search-keyword]/
├── Gartner - Article Title One (G00123456).pdf
├── Gartner - Article Title Two (G00234567).pdf
└── ...
```

### Summary Report
```markdown
# Gartner Batch Download Report

**Search Keyword:** "application rationalization"
**Date:** 2025-10-14 15:30:45
**Status:** 7 of 10 successful

## Downloaded Files

1. [SUCCESS] 7 Steps to Rationalize Your Application Portfolio
   - Document ID: G006327847
   - File: 05_Attachments/Gartner/application-rationalization/Gartner - 7 Steps... (G006327847).pdf
   - Size: 4.2 MB
   - Downloaded: 15:31:12

2. [SUCCESS] 3 Actions to Take Application Rationalization Beyond Cost Savings
   - Document ID: G006780334
   - File: 05_Attachments/Gartner/application-rationalization/Gartner - 3 Actions... (G006780334).pdf
   - Size: 3.8 MB
   - Downloaded: 15:31:25

... (continue for all successful downloads)

## Failed Downloads

1. [FAILED] Overcome the Challenges of Application Rationalization
   - Document ID: G006297615
   - URL: https://www.gartner.com/en/documents/6297615
   - Error: PDF download button not found on page
   - Manual Action: Visit URL while logged in and download manually

2. [FAILED] Application Rationalization Key Initiative
   - Document ID: G002551315
   - URL: https://www.gartner.com/en/documents/2551315
   - Error: Download timeout after 60 seconds
   - Manual Action: Check network connection and retry

## Statistics

- Articles found: 10
- Successfully downloaded: 7 (70%)
- Failed: 3 (30%)
- Total size: 42.3 MB
- Total time: 8 minutes 32 seconds

## Manual Download Instructions

For failed downloads:
1. Ensure you're logged into Gartner.com
2. Visit the URL listed above
3. Click the "Download PDF" or "Save as PDF" button
4. Save to: 05_Attachments/Gartner/application-rationalization/

## Next Steps

- Review failed downloads and attempt manual retrieval
- Check file quality and completeness
- Create research notes in Obsidian linking to PDFs
- Use /create-note to analyze downloaded content
```

---

## Troubleshooting

### Issue: "Environment variables not found"

**Solution:**
1. Create `.env` file in project root
2. Add credentials:
   ```
   GARTNER_USERNAME=your-email@example.com
   GARTNER_PASSWORD=your-password
   ```
3. Verify file is git-ignored
4. Restart Claude Code to reload environment

---

### Issue: "Login failed" or "Cannot find login form"

**Possible Causes:**
- Gartner login page structure changed
- Incorrect credentials
- Account locked or requires verification

**Solution:**
1. Manually visit https://www.gartner.com/account/signin
2. Verify you can log in successfully
3. Take note of actual form field attributes
4. Update selectors in command if needed
5. Check for CAPTCHA or 2FA requirements (may require manual login first)

---

### Issue: "Cannot find search results" or "Zero results extracted"

**Possible Causes:**
- Search page structure changed
- Search term has no matches
- Results taking too long to load

**Solution:**
1. Manually search on Gartner.com with same keyword
2. Verify results appear
3. Inspect page HTML to identify actual result selectors
4. Update extraction JavaScript in Phase 2, Step 6
5. Increase wait timeout if network is slow

---

### Issue: "PDF download not working"

**Possible Causes:**
- No direct PDF download button exists
- Playwright cannot access downloads folder
- Download requires special permissions

**Solutions:**
1. **Check download location:**
   ```bash
   ls -la ~/Downloads/*.pdf
   ```

2. **Try alternative approach:**
   - Use print-to-PDF method
   - Extract content and generate PDF locally
   - Use Chrome DevTools MCP instead of Playwright

3. **Manual fallback:**
   - Command will provide list of URLs
   - Download manually while logged in
   - Save to appropriate directory

---

### Issue: "Rate limited" or "Access denied during batch"

**Solution:**
1. Increase delay between downloads: modify sleep duration
2. Run in smaller batches (--count 3-5)
3. Try during off-peak hours
4. Contact Gartner support if persistent

---

### Issue: "Playwright MCP not responding"

**Solution:**
1. Check MCP server status in Claude Code settings
2. Restart Playwright MCP server
3. Verify Playwright installation:
   ```bash
   npx playwright --version
   ```
4. Reinstall if needed:
   ```bash
   npx playwright install
   ```

---

## Known Limitations

1. **Browser Automation Brittleness**
   - Gartner UI changes will break selectors
   - Requires periodic maintenance
   - First run may need adjustments

2. **PDF Download Mechanism**
   - Playwright file download support varies by configuration
   - May require manual intervention for some documents
   - Alternative PDF generation may reduce quality

3. **Authentication Constraints**
   - Does not support 2FA/MFA (requires manual pre-authentication)
   - Does not handle CAPTCHA
   - Session may expire during long batches

4. **Rate Limiting**
   - Gartner may throttle automated requests
   - Large batches (>10) may trigger restrictions
   - Delays between requests help but don't guarantee success

5. **File Management**
   - Cannot detect duplicate downloads automatically
   - Title-based naming may conflict if titles are identical
   - Special characters in titles may cause filesystem issues

---

## Best Practices

1. **Start Small**
   - Test with --count 2 first
   - Verify authentication and search work
   - Confirm at least one download succeeds
   - Scale up after validation

2. **Use During Off-Peak Hours**
   - Less likely to hit rate limits
   - Faster page loads
   - Better success rates

3. **Monitor First Run Closely**
   - Watch for selector errors
   - Note any manual interventions needed
   - Document actual page structures
   - Update command as needed

4. **Organize Downloaded Content**
   - Review PDFs for completeness
   - Create research notes with summaries
   - Tag and categorize in Obsidian
   - Link related documents

5. **Keep Credentials Secure**
   - Never commit .env file
   - Use strong, unique passwords
   - Rotate credentials periodically
   - Consider using password manager

---

## Future Enhancements

**Planned improvements for V2:**

- Resume capability (skip already downloaded files)
- Browser session persistence (stay logged in)
- Parallel downloads (if rate limiting allows)
- Integration with /search-gartner command
- Support for downloading from saved search results
- Progress indicators and ETA
- Webhook notifications on completion
- Export to citation managers (Zotero, Mendeley)

---

## Related Commands

- **/search-gartner** - Search only, no downloads (faster for discovery)
- **/download-gartner-pdf** - Download single PDF from URL
- **/create-note** - Create analysis note from downloaded PDFs

---

## Technical Notes

**Selector Strategy:**
The command uses a "snapshot-first" approach where it takes an accessibility snapshot before each interaction to identify the correct element references. This makes it more resilient to minor UI changes but requires the overall page structure to remain similar.

**Error Recovery:**
Non-fatal errors (individual download failures) are logged but don't stop execution. Fatal errors (authentication, search failures) stop execution immediately and provide diagnostic information.

**File Naming:**
Document IDs (G00XXXXXX format) are included in filenames to ensure uniqueness and enable cross-referencing with Gartner's system.

**Performance:**
Expect approximately 30-60 seconds per document (including delays). A batch of 10 documents typically completes in 8-12 minutes.

---

## Support

If you encounter issues:

1. Check Prerequisites section - ensure all requirements met
2. Review Troubleshooting section for common issues
3. Run with --count 1 to isolate problem
4. Take screenshots/snapshots at failure point
5. Check Playwright MCP logs for detailed errors
6. Update selectors if Gartner UI changed
7. Consider manual download as temporary workaround

For persistent issues, the command will always provide a list of URLs that can be downloaded manually while logged into Gartner.

---

**Version:** 1.0.0
**Last Updated:** 2025-10-14
**Status:** Experimental - Requires testing and validation
