# Training Is Not the Same as Chatting: ChatGPT and Other LLMs Don’t Remember Everything You Say

![rw-book-cover](https://rdl.ink/render/https%3A%2F%2Fsimonwillison.net%2F2024%2FMay%2F29%2Ftraining-not-chatting%2F)
<br>
>[!note]- Readwise Information
>Title:: Training Is Not the Same as Chatting: ChatGPT and Other LLMs Don’t Remember Everything You Say
>Author:: [[simonwillison.net]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-05-29]]
>Last-Highlighted-Date:: [[2024-05-31]]
>Readwise-Link:: https://readwise.io/bookreview/41001011
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Gartner]] [[generative ai]] [[large language models]] 
>Source URL:: https://simonwillison.net/2024/May/29/training-not-chatting/
--- 

## Linked Notes
```dataview
LIST
FROM [[Training Is Not the Same as Chatting: ChatGPT and Other LLMs Don’t Remember Everything You Say by simonwillison.net Highlights]]
```

---

## Highlights
- Short version: ChatGPT and other similar tools **do not directly learn from and memorize everything that you say to them**. [View Highlight](https://readwise.io/open/726154985) ^rw726154985
- There is no point at all in “telling” a model something in order to improve its knowledge for future conversations. I’ve heard from people who have invested weeks of effort pasting new information into ChatGPT sessions to try and “train” a better bot. That’s a waste of time! [View Highlight](https://readwise.io/open/727114003) ^rw727114003
- Understanding this helps explain why the “context length” of a model is so important. Different LLMs have different context lengths, expressed in terms of “tokens”—a token is about 3/4s of a word. This is the number that tells you how much of a conversation the bot can consider at any one time. [View Highlight](https://readwise.io/open/727114034) ^rw727114034
- The first is to pile in several TBs of text—think all of Wikipedia, a scrape of a large portion of the web, books, newspapers, academic papers and more—and spend months of time and potentially millions of dollars in electricity crunching through that “pre-training” data identifying patterns in how the words relate to each other. [View Highlight](https://readwise.io/open/727114435) ^rw727114435
- The second phase aims to fix that—this can incorporate instruction tuning or Reinforcement Learning from Human Feedback (RLHF) which has the goal of teaching the model to pick the best possible sequences of words to have productive conversations. [View Highlight](https://readwise.io/open/727114410) ^rw727114410
- The model is stored in a static file and loaded, continuously, across 10s of thousands of identical servers each of which serve each instance of the Claude model. [View Highlight](https://readwise.io/open/727114474) ^rw727114474
- These models don’t change very often! [View Highlight](https://readwise.io/open/727114479) ^rw727114479
- Many LLM providers have terms and conditions that allow them to improve their models based on the way you are using them. Even when they have opt-out mechanisms these are often opted-in by default. [View Highlight](https://readwise.io/open/727114489) ^rw727114489
