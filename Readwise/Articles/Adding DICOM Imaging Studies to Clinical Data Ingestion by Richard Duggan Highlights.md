# Adding DICOM Imaging Studies to Clinical Data Ingestion

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
<br>
>[!note]- Readwise Information
>Title:: Adding DICOM Imaging Studies to Clinical Data Ingestion
>Author:: [[Richard Duggan]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2021-06-16]]
>Last-Highlighted-Date:: [[2023-01-31]]
>Readwise-Link:: https://readwise.io/bookreview/23894443
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://alvearie.io/blog/imaging-ingestion
--- 

## Linked Notes
```dataview
LIST
FROM [[Adding DICOM Imaging Studies to Clinical Data Ingestion by Richard Duggan Highlights]]
```

---

## Highlights
- In the real world, medical imaging centers are less likely to use DICOMweb and much more likely to use DICOM Message Service Element (DIMSE) services for communication of DICOM data. Specifically, images are stored using a DIMSE C-Store composite operation as opposed to the DICOMweb STOW-RS in the simplified topology. As such, we need to extend the previously defined Simplified Approach to enable a bridge from DIMSE to the ingestion services. [View Highlight](https://readwise.io/open/467183407) ^rw467183407
- The resulting topology is identical to the Simplified Approach with the exception that we introduced the **DIMSE Ingestion Service** for processing DIMSE C-STORE operations (1b). Also, we have added a **DIMSE Proxy** that acts as a DIMSE Application Entity (AE) to directly integrate with the existing DIMSE based communication systems within the medical imaging center. The DIMSE proxy and DIMSE Ingestion subcomponents use a [NATS](https://nats.io/) messaging service to bridge the DICOM to a multi-zone regional cloud deployment. [View Highlight](https://readwise.io/open/467183514) ^rw467183514
