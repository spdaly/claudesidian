# 😺 We Now Know How to Fix AI's Biggest Flaw

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
<br>
>[!note]- Readwise Information
>Title:: 😺 We Now Know How to Fix AI's Biggest Flaw
>Author:: [[The Neuron]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-09-11]]
>Last-Highlighted-Date:: [[2025-09-11]]
>Readwise-Link:: https://readwise.io/bookreview/54924516
>Readwise-Source:: #Readwise/source/reader
--- 

## Linked Notes
```dataview
LIST
FROM [[😺 We Now Know How to Fix AI's Biggest Flaw by The Neuron Highlights]]
```

---

## Highlights
- Horace and his team discovered the real culprit isn't the usual suspect: floating-point math weirdness that engineers typically blame. Instead, it's something called “batch invariance.” **Think of it like this:**
  1. Imagine ordering the same coffee at Starbucks, but it tastes different depending on how many other customers are in line. That's essentially what's happening with AI models.
  2. When an AI server is busy handling lots of requests, it processes them in batches.
  3. Your request gets bundled with others (because that’s more efficient), and somehow this changes your specific answer… even though it shouldn't.
  4. Follow the logic, and the busier the server, the more your results vary.
  *This also happens in real life; ever been to your local Starbucks during coffee rush hour? Unless you have a god tier level barista, your order might not taste the same!* [View Highlight](https://readwise.io/open/936878842) ^rw936878842 
- See also: [[artificial intelligence]] [[large language models]] 
- Note: This is the root cause and a potential solution for the nondeterministic nature of large language models
