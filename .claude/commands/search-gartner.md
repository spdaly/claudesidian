---
allowed-tools: [WebSearch, WebFetch, Write]
description: Search Gartner for keyword and return URLs of top 5 most recent articles
argument-hint: <search-keyword> [--save]
---

# Search Gartner Research

Searches Gartner research library for a keyword or topic and returns URLs of the top 5 most recent articles with metadata.

## Task

Given a search keyword or topic, query Gartner's research library and return the 5 most recent relevant articles with their URLs, titles, dates, and summaries.

## Arguments

- **search-keyword** (required): Topic, technology, or keyword to search for
- **--save** (optional): Flag to save results to a markdown file in vault

## Process

1. **Execute Search**: Use WebSearch to query Gartner research with keyword
   - Domain filter: `gartner.com/document`
   - Sort by: Most recent
   - Limit: Top 5 results

2. **Extract Information**: For each result, capture:
   - Article title
   - Publication date
   - Document URL
   - Author(s) if available
   - Brief summary/description
   - Document type (research note, report, guide, etc.)

3. **Rank Results**: Sort by recency (newest first)

4. **Format Output**:
   - Present as numbered list
   - Include clickable URLs
   - Show publication dates
   - Brief 1-2 sentence description

5. **Optional Save**: If `--save` flag provided:
   - Create markdown file in `03_Resources/Gartner/`
   - Filename: `Gartner Search - [keyword] - [date].md`
   - Include frontmatter with search metadata

## Output Format

```markdown
# Gartner Search Results: [keyword]
Search Date: YYYY-MM-DD

## Top 5 Recent Articles

1. **[Article Title]** (Published: YYYY-MM-DD)
   - URL: https://www.gartner.com/document/code/XXXXXX
   - Type: Research Note
   - Summary: Brief description of the article content
   - Authors: Name(s)

2. **[Article Title]** (Published: YYYY-MM-DD)
   ...

[Continue for all 5 results]

## Quick Actions
- Download all as PDFs: Use /download-gartner-pdf for each URL
- Create research note: Use /create-note to analyze findings
```

## Example Usage

```bash
# Basic search
/search-gartner "application rationalization"

# Search and save results
/search-gartner "AI strategy" --save

# Technology search
/search-gartner "generative AI governance"

# Methodology search
/search-gartner "TIME framework"
```

## Output Examples

### Console Output
```
🔍 Searching Gartner for: "application rationalization"

Found 5 recent articles:

1. **How to Choose the Right Approach for Application Modernization** (2023-01-15)
   https://www.gartner.com/document/code/772600
   Guide comparing five modernization approaches with decision framework

2. **7 Steps to Rationalize Your Application Portfolio** (2022-11-20)
   https://www.gartner.com/document/code/XXXXXX
   Step-by-step methodology for portfolio rationalization programs

[... 3 more results]

✅ Results saved to: 03_Resources/Gartner/Gartner Search - application rationalization - 2025-10-14.md
```

### Saved File (if --save used)
Will create a markdown file with:
- Frontmatter (search_term, date, results_count)
- All 5 results with full details
- Links ready for /download-gartner-pdf command
- Tags for organization

## Notes

- Requires active Gartner subscription for full access
- Search results may vary based on access level
- URLs will be to gartner.com (requires login)
- Some articles may be behind access restrictions
- Results are sorted by publication date (newest first)

## Integration with Other Commands

This command works well with:
- `/download-gartner-pdf` - Download the found articles
- `/add-frontmatter` - Add metadata to saved search results
- `/create-note` - Create analysis notes from search results

## Search Tips

- Use specific technical terms for better results
- Try methodology names: "TIME framework", "Pace-Layered"
- Search by technology: "generative AI", "application portfolio management"
- Use quotes for exact phrases: "application rationalization"
- Combine terms: "AI cost optimization strategy"
