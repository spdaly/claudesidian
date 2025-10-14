# A Visual Guide to Quantization

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9d17077-d9af-4b37-9b9b-57ef9aaa1ca9_680x486.png)
<br>
>[!note]- Readwise Information
>Title:: A Visual Guide to Quantization
>Author:: [[Maarten Grootendorst]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-07-30]]
>Last-Highlighted-Date:: [[2024-09-04]]
>Readwise-Link:: https://readwise.io/bookreview/42893640
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[large language models]] 
>Source URL:: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization
--- 

## Linked Notes
```dataview
LIST
FROM [[A Visual Guide to Quantization by Maarten Grootendorst Highlights]]
```

---

## Highlights
- As such, more and more research has been focused on making these models smaller through improved training, adapters, etc. One major technique in this field is called *quantization*. [View Highlight](https://readwise.io/open/781237607) ^rw781237607
- LLMs get their name due to the number of parameters they contain. Nowadays, these models typically have billions of parameters (mostly *weights*) which can be quite expensive to store. [View Highlight](https://readwise.io/open/754298871) ^rw754298871
- As such, it is very compelling to minimize the number of bits to represent the parameters of your model (as well as during training!). However, as the precision decreases the accuracy of the models generally does as well. [View Highlight](https://readwise.io/open/754300272) ^rw754300272
- We want to reduce the number of bits representing values while maintaining accuracy… This is where *quantization* comes in! [View Highlight](https://readwise.io/open/754300285) ^rw754300285
- Note: Quantization reduces size while trying to maintain a good level of precision
- The main goal of quantization is to reduce the number of bits (colors) needed to represent the original parameters while preserving the precision of the original parameters as best as possible. [View Highlight](https://readwise.io/open/754300517) ^rw754300517
- In symmetric quantization, the range of the original floating-point values is mapped to a symmetric range around zero in the quantized space. [View Highlight](https://readwise.io/open/754300946) ^rw754300946
- Asymmetric quantization, in contrast, is not symmetric around zero. Instead, it maps the minimum (**β**) and maximum (**α**) values from the float range to the minimum and maximum values of the quantized range. [View Highlight](https://readwise.io/open/754301015) ^rw754301015
- Clipping involves setting a different dynamic range of the original values such that all outliers get the same value. [View Highlight](https://readwise.io/open/754301144) ^rw754301144
- Since there are significantly fewer biases (millions) than weights (billions), the biases are often kept in higher precision (such as INT16), and the main effort of quantization is put towards the weights. [View Highlight](https://readwise.io/open/754301313) ^rw754301313
- Going below 8-bit quantization has proved to be a difficult task as the quantization error increases with each loss of bit. Fortunately, there are several smart ways to reduce the bits to 6, 4, and even 2-bits (although going lower than 4-bits using these methods is typically not advised). [View Highlight](https://readwise.io/open/754301501) ^rw754301501
- GGUF
  While GPTQ is a great quantization method to run your full LLM on a GPU, you might not always have that capacity. Instead, we can use GGUF to offload any layer of the LLM to the CPU. [View Highlight](https://readwise.io/open/754301822) ^rw754301822
- This is where Quantization Aware Training (QAT) comes in. Instead of quantizing a model ***after*** it was trained with post-training quantization (PTQ), QAT aims to learn the quantization procedure ***during*** training. [View Highlight](https://readwise.io/open/754301938) ^rw754301938
- QAT tends to be more accurate than PTQ since the quantization was already considered during training. [View Highlight](https://readwise.io/open/754302230) ^rw754302230
