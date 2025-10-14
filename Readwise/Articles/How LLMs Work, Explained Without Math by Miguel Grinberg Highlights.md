# How LLMs Work, Explained Without Math

![rw-book-cover](https://blog.miguelgrinberg.com/favicon.ico)
<br>
>[!note]- Readwise Information
>Title:: How LLMs Work, Explained Without Math
>Author:: [[Miguel Grinberg]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-05-05]]
>Last-Highlighted-Date:: [[2024-05-14]]
>Readwise-Link:: https://readwise.io/bookreview/40499635
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[artificial intelligence]] [[large language models]] 
>Source URL:: https://blog.miguelgrinberg.com/post/how-llms-work-explained-without-math
--- 

## Linked Notes
```dataview
LIST
FROM [[How LLMs Work, Explained Without Math by Miguel Grinberg Highlights]]
```

---

## Highlights
- Given some text, a language model maked predictions about what token will follow right after. If it helps to see this with Python pseudo-code, here is how you could run one of these models to get predictions for the next token: [View Highlight](https://readwise.io/open/719439532) ^rw719439532 
- See also: [[👻 ai highlighted]] 
- To be able to produce reasonable predictions, the language model has to go through a *training* process. During training, it is presented with lots and lots of text to learn from. At the end of the training, the model is able to calculate next token probabilities for a given token sequence using data structures that it has built using all the text that it saw in training. [View Highlight](https://readwise.io/open/719439531) ^rw719439531 
- See also: [[👻 ai highlighted]] 
- Since the model can only predict what the next token is going to be, the only way to make it generate complete sentences is to run the model multiple times in a loop. With each loop iteration a new token is generated, chosen from the returned probabilities. This token is then added to the input that is given to the model on the next iteration of the loop, and this continues until sufficient text has been generated. [View Highlight](https://readwise.io/open/719439530) ^rw719439530 
- See also: [[👻 ai highlighted]] 
- The job of the `select_next_token()` function is to take the next token probabilities (or predictions) and pick the best token to continue the input sequence. The function could just pick the token with the highest probability, which in machine learning is called a *greedy selection*. Better yet, it can pick a token using a random number generator that honors the probabilities returned by the model, and in that way add some variety to the generated text. This will also make the model produce different responses if given the same prompt multiple times. [View Highlight](https://readwise.io/open/719439533) ^rw719439533 
- See also: [[👻 ai highlighted]] 
- Let's do this with a short vocabulary and dataset. Let's say the model's vocabulary has the following five tokens: [View Highlight](https://readwise.io/open/719439535) ^rw719439535 
- See also: [[👻 ai highlighted]] 
- An issue with this technique is that only one token (the last of the input) is used to make a prediction. Any text that appears before that last token doesn't have any influence when choosing how to continue, so we can say that the *context window* of this solution is equal to one token, which is very small. With such a small context window the model constantly "forgets" its line of thought and jumps from one word to the next without much consistency. [View Highlight](https://readwise.io/open/719439536) ^rw719439536 
- See also: [[👻 ai highlighted]] 
- I personally do not see LLMs as having an ability to reason or come up with original thoughts, but that does not mean to say they're useless. Thanks to the clever calculations they perform on the tokens that are in the context window, LLMs are able to pick up on patterns that exist in the user prompt and match them to similar patterns learned during training. The text they generate is formed from bits and pieces of training data for the most part, but the way in which they stitch words (tokens, really) together is highly sophisticated, in many cases producing results that feel original and useful. [View Highlight](https://readwise.io/open/719439537) ^rw719439537 
- See also: [[👻 ai highlighted]] 
