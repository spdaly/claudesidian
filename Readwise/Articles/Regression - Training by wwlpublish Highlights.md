# Regression - Training

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/open-graph-image_zpCOSwp.png)
<br>
>[!note]- Readwise Information
>Title:: Regression - Training
>Author:: [[wwlpublish]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-11-15]]
>Last-Highlighted-Date:: [[2024-06-05]]
>Readwise-Link:: https://readwise.io/bookreview/41219404
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/4-regression
--- 

## Linked Notes
```dataview
LIST
FROM [[Regression - Training by wwlpublish Highlights]]
```

---

## Highlights
- Regression models are trained to predict numeric label values based on training data that includes both features and known labels. [View Highlight](https://readwise.io/open/729649464) ^rw729649464
- The process for training a regression model (or indeed, any supervised machine learning model) involves multiple iterations in which you use an appropriate algorithm (usually with some parameterized settings) to train a model, evaluate the model's predictive performance, and refine the model by repeating the training process with different algorithms and parameters until you achieve an acceptable level of predictive accuracy. [View Highlight](https://readwise.io/open/729649504) ^rw729649504
- One way to produce a metric that "amplifies" larger errors by *squaring* the individual errors and calculating the mean of the squared values. This metric is known as the **mean squared error** (MSE).
  In our ice cream example, the mean of the squared absolute values (which are 4, 9, 9, 1, 4, and 9) is **6**. [View Highlight](https://readwise.io/open/729649735) ^rw729649735
- that doesn't measure its accuracy in terms of the number of ice creams that were mispredicted; 6 is just a numeric score that indicates the level of error in the validation predictions.
  If we want to measure the error in terms of the number of ice creams, we need to calculate the *square root* of the MSE; which produces a metric called, unsurprisingly, **Root Mean Squared Error**. In this case √6, which is **2.45** (ice creams). [View Highlight](https://readwise.io/open/729650014) ^rw729650014
- The **coefficient of determination** (more commonly referred to as **R2** or **R-Squared**) is a metric that measures the proportion of variance in the validation results that can be explained by the model, as opposed to some anomalous aspect of the validation data [View Highlight](https://readwise.io/open/729650088) ^rw729650088
- the closer to 1 this value is, the better the model is fitting the validation data. In the case of the ice cream regression model, the R2 calculated from the validation data is **0.95**. [View Highlight](https://readwise.io/open/729650736) ^rw729650736
