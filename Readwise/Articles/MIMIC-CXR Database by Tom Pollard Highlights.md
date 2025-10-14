# MIMIC-CXR Database

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
<br>
>[!note]- Readwise Information
>Title:: MIMIC-CXR Database
>Author:: [[Tom Pollard]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2019-09-19]]
>Last-Highlighted-Date:: [[2023-01-31]]
>Readwise-Link:: https://readwise.io/bookreview/23894278
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://physionet.org/content/mimic-cxr/2.0.0/
--- 

## Linked Notes
```dataview
LIST
FROM [[MIMIC-CXR Database by Tom Pollard Highlights]]
```

---

## Highlights
- The BIDMC operates a locally built electronic health record (EHR) to store and process clinical data. A collection of images associated with a single report is referred to as a study. We queried the BIDMC EHR for chest x-ray studies made in the emergency department between 2011 - 2016, and extracted the set of patient identifiers associated with these studies. We subsequently extracted all chest x-ray studies for this set of patients between 2011 - 2016. For anonymization purposes, two sets of random identifiers were generated. First, a random identifier was generated for each patient in the range 10,000,000 - 19,999,999, which we refer to as the `subject_id`. Each patient was also assigned a date shift which mapped their first index admission year to a year between 2100 - 2200. This ensures anonymity of the data while preserving the relative chronology of patient information, which is crucial for appropriate processing of the data.  Second, each report was associated with a single unique identifier. We generated a random identifier for each study in the range 50,000,000 - 59,999,999. We refer to the anonymized study identifier as the `study_id`. As multiple images may be associated with the same study (e.g. one frontal and one lateral image), multiple images in MIMIC-CXR have the same `study_id`. Finally, a random 40 character hash was generated for each individual image file. These hashes are unique to each image. [View Highlight](https://readwise.io/open/467181717) ^rw467181717
- Chest radiographs were sourced from the hospital picture archiving and communication system (PACS) in Digital Imaging and Communications in Medicine (DICOM) format. DICOM is a common format for medical images which facilitates interoperability of many distinct medical devices. Put simply, the DICOM format contains structured meta-data associated with one or more images, and the DICOM standard stipulates strict rules around the structure of this information. [View Highlight](https://readwise.io/open/467182317) ^rw467182317
- The acquired DICOM images contained PHI which required removal for conformance with HIPAA. Images sometimes contain ``burned in'' annotations: areas where pixel values have been modified after image acquisition in order to display text. Annotations contain relevant information including: image orientation, anatomical position of the subject, timestamp of image capture, and so on. The resulting image, with textual annotations encoded within the pixel themselves, is then transferred from the modality to PACS. Since the annotations are applied at the modality level, it is impossible to recover the original image without annotations. [View Highlight](https://readwise.io/open/467182338) ^rw467182338
