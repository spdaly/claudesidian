# Defeating Nondeterminism in LLM Inference

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/cover-social.png)
<br>
>[!note]- Readwise Information
>Title:: Defeating Nondeterminism in LLM Inference
>Author:: [[Thinking Machines Lab]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-09-10]]
>Last-Highlighted-Date:: [[2025-09-22]]
>Readwise-Link:: https://readwise.io/bookreview/54918670
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
--- 

## Linked Notes
```dataview
LIST
FROM [[Defeating Nondeterminism in LLM Inference by Thinking Machines Lab Highlights]]
```

---

## Highlights
- But why *aren’t* LLM inference engines deterministic? One common hypothesis is that some combination of floating-point non-associativity and concurrent execution leads to nondeterminism based on which concurrent core finishes first. [View Highlight](https://readwise.io/open/936805750) ^rw936805750
- While this hypothesis is not entirely wrong, it doesn’t reveal the full picture. [View Highlight](https://readwise.io/open/940404234) ^rw940404234
- Unfortunately, even *defining* what it means for LLM inference to be deterministic is difficult. Perhaps confusingly, the following statements are all simultaneously true:
  1. Some kernels on GPUs are **nondeterministic**.
  2. However, all the kernels used in a language model’s forward pass are **deterministic**.
  3. Moreover, the forward pass of an LLM inference server (like vLLM) can also be claimed to be **deterministic**.
  4. Nevertheless, from the perspective of anybody using the inference server, the results are **nondeterministic**. [View Highlight](https://readwise.io/open/936805781) ^rw936805781
- The culprit is **floating-point non-associativity.** That is, with floating-point numbers:
  (a+b)+c≠a+(b+c) (a + b) + c \neq a + (b + c) (a+b)+c=a+(b+c) [View Highlight](https://readwise.io/open/936805816) ^rw936805816
- Ironically, breaking associativity is what makes floating-point numbers useful. [View Highlight](https://readwise.io/open/936805830) ^rw936805830
- Although this is the underlying cause for non-identical outputs, it does not directly answer where the nondeterminism comes from. [View Highlight](https://readwise.io/open/940405358) ^rw940405358
- As mentioned above, one common explanation for why kernels add numbers in different orders is the “concurrency + floating point” hypothesis. The hypothesis states that if the order in which concurrent threads finish is nondeterministic and the accumulation order depends on the order in which concurrent threads finish (such as with an atomic add), our accumulation order will be nondeterministic as well. [View Highlight](https://readwise.io/open/936806344) ^rw936806344
- This is usually what folks mean by “nondeterminism” — you execute the same kernel twice with exactly the same inputs and you get a different result out. This is known as *run-to-run nondeterminism*, where you run the same python script twice with the exact same dependencies but get a different result. [View Highlight](https://readwise.io/open/936806390) ^rw936806390
- Wikipedia writes that “a deterministic algorithm is an algorithm that, given a particular input, will always produce the same output.” And in this case, given the exact same inputs (i.e. the exact requests the inference server is processing), the forward pass always produces the exact same outputs. [View Highlight](https://readwise.io/open/936836302) ^rw936836302
