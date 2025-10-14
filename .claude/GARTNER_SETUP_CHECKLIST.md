# Gartner Batch Download - Setup Checklist

## Prerequisites Status

### 1. Credentials Configuration
- [x] `.env` file created
- [ ] **ACTION REQUIRED:** Edit `.env` and add your actual Gartner credentials
  - Replace `your-email@example.com` with your Gartner login email
  - Replace `your-password-here` with your Gartner password
- [x] `.env` is in `.gitignore` (verified - credentials are secure)

### 2. MCP Server
- [x] Playwright MCP server is running and responsive
- [x] Browser automation tools are available

### 3. Directory Structure
- [x] Output directory created: `05_Attachments/Gartner/`
- [x] Command file created: `.claude/commands/gartner-batch-download.md`

### 4. System Requirements
- [x] Disk space available (estimated 50MB for 10 documents)
- [x] Network access to gartner.com (assumed - will verify on first run)

---

## Next Steps: Testing

### BEFORE FIRST RUN

**YOU MUST edit the .env file with your real Gartner credentials:**

```bash
# Open .env in your editor
# Replace placeholder values with:
GARTNER_USERNAME=your-actual-email@example.com
GARTNER_PASSWORD=your-actual-password
```

### Test Phase 1: Minimal Batch (2 documents)

Once credentials are added, run:

```bash
/gartner-batch-download "application rationalization" --count 2
```

**What to watch for:**
- [ ] Authentication succeeds (login completes)
- [ ] Search page loads and query is entered
- [ ] At least 2 results are found and displayed
- [ ] Navigation to first article works
- [ ] PDF download mechanism is identified

**Expected issues on first run:**
- Selectors may need adjustment for Gartner's actual page structure
- PDF download button may have different attributes than assumed
- Page load times may vary

### Test Phase 2: Analyze Results

After first run, check:

1. **Authentication logs:** Did login work?
2. **Search results:** Were articles found and extracted?
3. **Download attempts:** What happened at download stage?
4. **Error messages:** What specific failures occurred?

### Test Phase 3: Selector Refinement

Based on Phase 1 results:

1. Take note of actual Gartner page selectors
2. Update command file if needed
3. Re-run with --count 2 to verify fixes
4. Iterate until successful

### Test Phase 4: Scale Up

Once 2 documents download successfully:

```bash
/gartner-batch-download "application rationalization" --count 5
```

Then gradually increase to full batch of 10.

---

## Troubleshooting Quick Reference

### Issue: "Environment variables not found"
**Solution:** Edit `.env` file and add actual credentials

### Issue: "Login failed"
**Solution:**
1. Verify credentials work on gartner.com manually
2. Check for 2FA/CAPTCHA requirements
3. Update login page selectors if Gartner UI changed

### Issue: "Cannot find search results"
**Solution:**
1. Manually search on Gartner to verify results exist
2. Inspect page HTML for actual result selectors
3. Update extraction JavaScript in command file

### Issue: "PDF download not working"
**Solution:**
1. Check if direct download button exists on article page
2. Try print-to-PDF fallback
3. Use manual download URLs provided in error report

---

## Success Criteria

Minimum requirements for considering setup complete:

- [x] Credentials configured in `.env`
- [ ] First test run completes without fatal errors
- [ ] At least 1 PDF successfully downloaded
- [ ] Files saved with correct naming convention
- [ ] Summary report generated

---

## Current Status

**Setup Phase:** READY FOR CREDENTIALS
**Next Action:** Edit `.env` file with real Gartner credentials
**Then Run:** `/gartner-batch-download "test keyword" --count 2`

---

**Created:** 2025-10-14
**Last Updated:** 2025-10-14
