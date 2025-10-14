# Large language models, explained with a minimum of math and jargon
Large language models, explained with a minimum of math and jargon

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3e159bd-1228-4205-b1eb-5898ab9172d3_1600x856.png)
<br>
>[!note]- Readwise Information
>Title:: Large language models, explained with a minimum of math and jargon
Large language models, explained with a minimum of math and jargon
>Author:: [[Timothy B. Lee]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-07-27]]
>Last-Highlighted-Date:: [[2023-11-29]]
>Readwise-Link:: https://readwise.io/bookreview/34688383
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[artificial intelligence]] [[llm]] [[tutorial]] 
>Source URL:: https://www.understandingai.org/p/large-language-models-explained-with
--- 

## Linked Notes
```dataview
LIST
FROM [[Large language models, explained with a minimum of math and jargon
Large language models, explained with a minimum of math and jargon by Timothy B. Lee Highlights]]
```

---

## Highlights
- GPT-3, the model behind the original version of ChatGPT[2](https://www.understandingai.org/p/large-language-models-explained-with`#`footnote-2-135476638), is organized into dozens of layers. Each layer takes a sequence of vectors as inputs—one vector for each word in the input text—and adds information to help clarify the meaning of that word and better predict which word might come next [View Highlight](https://readwise.io/open/633216261) ^rw633216261
- Each layer of an LLM is a transformer, a neural network architecture that was first introduced by Google in a [landmark 2017 paper](https://arxiv.org/abs/1706.03762). [View Highlight](https://readwise.io/open/633216408) ^rw633216408
- The transformer figures out that **wants** and **cash** are both verbs (both words can also be nouns). We’ve represented this added context as red text in parentheses, but in reality the model would store it by modifying the word vectors in ways that are difficult for humans to interpret. These new vectors, known as a hidden state, are passed to the next transformer in the stack [View Highlight](https://readwise.io/open/633216449) ^rw633216449
- The most powerful version of GPT-3, for example, has 96 layers. [View Highlight](https://readwise.io/open/633216477) ^rw633216477
- Researchers don’t understand exactly how LLMs keep track of this information, but logically speaking the model must be doing it by modifying the hidden state vectors as they get passed from one layer to the next. It helps that in modern LLMs, these vectors are extremely large. [View Highlight](https://readwise.io/open/633216513) ^rw633216513
- For example, the most powerful version of GPT-3 uses word vectors with 12,288 dimensions—that is, each word is represented by a list of 12,288 numbers. That’s 20 times larger than Google’s 2013 word2vec scheme. You can think of all those extra dimensions as a kind of “scratch space” that GPT-3 can use to write notes to itself about the context of each word. Notes made by earlier layers can be read and modified by later layers, allowing the model to gradually sharpen its understanding of the passage as a whole. [View Highlight](https://readwise.io/open/633216577) ^rw633216577
- In the **attention step**, words “look around” for other words that have relevant context and share information with one another. [View Highlight](https://readwise.io/open/633216648) ^rw633216648
- In the **feed-forward step**, each word “thinks about” information gathered in previous attention steps and tries to predict the next word. [View Highlight](https://readwise.io/open/633216650) ^rw633216650
- it’s the network, not the individual words, that performs these steps. [View Highlight](https://readwise.io/open/633216672) ^rw633216672
- transformers treat words, rather than entire sentences or passages, as the basic unit of analysis [View Highlight](https://readwise.io/open/633216704) ^rw633216704
- LLMs to take full advantage of the massive parallel processing power of modern GPU chips. And it also helps LLMs to scale to passages with thousands of words. [View Highlight](https://readwise.io/open/633216762) ^rw633216762
- You can think of the attention mechanism as a matchmaking service for words. Each word makes a checklist (called a query vector) describing the characteristics of words it is looking for. Each word also makes a checklist (called a key vector) describing its own characteristics. The network compares each key vector to each query vector (by computing a [dot product](https://en.wikipedia.org/wiki/Dot_product)) to find the words that are the best match. Once it finds a match, it transfers information from the word that produced the key vector to the word that produced the query vector. [View Highlight](https://readwise.io/open/633216815) ^rw633216815
- After the attention heads transfer information between word vectors, there’s a feed-forward network
  that “thinks about” each word vector and tries to predict the next word. No information is exchanged between words at this stage: the feed-forward layer analyzes each word in isolation [View Highlight](https://readwise.io/open/633734981) ^rw633734981
- The largest version of GPT-3 has 96 layers with 96 attention heads each, so GPT-3 performs 9,216 attention operations each time it predicts a new word. [View Highlight](https://readwise.io/open/633216869) ^rw633216869
- We love this example because it illustrates just how difficult it will be to fully understand LLMs [View Highlight](https://readwise.io/open/633217094) ^rw633217094
