# LLM Hallucinations Explained

![rw-book-cover](https://substackcdn.com/image/fetch/$s_!dh89!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9375d72d-9733-47ac-9fe8-43a7d4e8427b_1024x1024.png)
<br>
>[!note]- Readwise Information
>Title:: LLM Hallucinations Explained
>Author:: [[Nir Diamant]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-03-04]]
>Last-Highlighted-Date:: [[2025-08-03]]
>Readwise-Link:: https://readwise.io/bookreview/53903520
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[generative ai]] [[Hallucinations]] [[retrieval augmented generation]] 
>Source URL:: https://diamantai.substack.com/p/llm-hallucinations-explained?triedRedirect=true
--- 

## Linked Notes
```dataview
LIST
FROM [[LLM Hallucinations Explained by Nir Diamant Highlights]]
```

---

## Highlights
- One of the most effective ways to stop hallucinations is to give the LLM access to actual facts at runtime. RAG does exactly that. The idea is simple: before the model answers a question or completes a task, we fetch relevant information from an external knowledge source (like a database, documentation, or the web) and supply it to the model as additional context. This way, the LLM isn't relying solely on what's "in its head" (the training data), but it has some up-to-date, specific facts to work with. [View Highlight](https://readwise.io/open/922040594) ^rw922040594 
- See also: [[retrieval augmented generation]] [[hallucinations]] [[generative ai]] 
- Another powerful approach is fine-tuning the LLM on custom data or via specialized training processes to reduce its likelihood of hallucination. Fine-tuning means we take a pre-trained model and further train it on a narrower dataset or with additional objectives. One straightforward idea: fine-tune the model on a high-quality dataset of question-answer pairs where all answers are grounded in verified facts (or on a corpus of documentation for a specific domain). This can make the model more knowledgeable about that domain and less likely to make things up. Essentially, the model doesn't have to fill gaps with guesses if the gaps have been filled with real data during fine-tuning.
  Fine-tuning isn't just about adding facts; it can also teach the model behavior. One popular method is Reinforcement Learning from Human Feedback (RLHF) – used in training ChatGPT – where humans rate the model's outputs and the model is tuned to prefer responses that are not only helpful but also truthful. [View Highlight](https://readwise.io/open/922040652) ^rw922040652
- In addition to full model fine-tuning, developers can use lighter-weight tuning techniques like LoRA (Low-Rank Adapters) or prompt tuning on smaller sets of data to adjust a model's style. [View Highlight](https://readwise.io/open/922040667) ^rw922040667
- Sometimes, you don't need to change the model at all – just change how you ask it. Prompt engineering is the art of phrasing your input or system instructions in a way that steers the model towards the kind of output you want. [View Highlight](https://readwise.io/open/922040678) ^rw922040678
- One simple technique is to explicitly instruct the model to be truthful and to admit ignorance. For example, instead of just asking an open question, you might say: "Answer the following question using the provided context. If the answer is not in the context or you're not sure, say 'I don't know'." [View Highlight](https://readwise.io/open/922040688) ^rw922040688
- Even with retrieval and good prompting, it's wise to have a safety net. Rule-based filters and guardrails act as an additional layer that checks the model's output and steps in if something looks off. [View Highlight](https://readwise.io/open/922040730) ^rw922040730
- One more clever idea: have the model reflect on its answer. After the model gives an answer, you can ask it (or a second instance of it), "On a scale of 1-10, how confident are you that the above answer is correct and why?" Surprisingly, sometimes the model will acknowledge uncertainty upon reflection and even point out possible errors. [View Highlight](https://readwise.io/open/922040771) ^rw922040771
- One approach is self-refinement: you prompt the model with something like, "Here is your answer. Now, double-check each fact in it. If you find any unsupported claim, correct it." The model will then go through its answer and often identify sentences that might be questionable. [View Highlight](https://readwise.io/open/922040795) ^rw922040795
