# Copilot Privacy and Protections

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/open-graph-image.png)
<br>
>[!note]- Readwise Information
>Title:: Copilot Privacy and Protections
>Author:: [[KelliDavis]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-12-01]]
>Last-Highlighted-Date:: [[2024-02-14]]
>Readwise-Link:: https://readwise.io/bookreview/37711323
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://learn.microsoft.com/en-us/copilot/privacy-and-protections
--- 

## Linked Notes
```dataview
LIST
FROM [[Copilot Privacy and Protections by KelliDavis Highlights]]
```

---

## Highlights
- When organizations and employees use generative AI services, it's important to understand how these services handle user and chat data. Because employee chats may contain sensitive data, Copilot is designed to protect this information, as illustrated here: [View Highlight](https://readwise.io/open/677063635) ^rw677063635
- An Entra ID user's tenant and user information is removed from chat data at the start of a chat session. This information is only used to determine if the user is eligible for commercial data protection. Search queries triggered by prompts from an Entra ID user aren't linked to users or organizations by Bing. [View Highlight](https://readwise.io/open/677063662) ^rw677063662
- Prompts and responses are maintained for a short caching period for runtime purposes. After the browser is closed, the chat topic is reset, or the session times out, Microsoft discards prompts and responses. [View Highlight](https://readwise.io/open/677063669) ^rw677063669
- Copilot is a generative AI service grounded in data from the public web in the Bing search index only. It doesn't have access to organizational resources or content within Microsoft 365, such as documents in OneDrive, emails, or other data in the Microsoft 365 Graph. [View Highlight](https://readwise.io/open/677063750) ^rw677063750
- Copilot can access organizational content in the chat only when it's provided by users. This can be done in one of two ways:
  1. Users explicitly type or paste this information directly into the chat.
  2. Users type a prompt into Copilot in Edge after enabling the 'Allow access to any webpage or PDF' setting, and an intranet page is open in the browser. In this scenario, Copilot may use this content to help answer questions.
  In both cases, when commercial data is enabled, Copilot doesn't retain any of this data after the chat session is over. [View Highlight](https://readwise.io/open/677063817) ^rw677063817
