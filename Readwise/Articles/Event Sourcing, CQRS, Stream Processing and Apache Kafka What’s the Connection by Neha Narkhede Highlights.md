# Event Sourcing, CQRS, Stream Processing and Apache Kafka: What’s the Connection?

![rw-book-cover](https://cdn.confluent.io/wp-content/uploads/seo-logo-meadow.png)
<br>
>[!note]- Readwise Information
>Title:: Event Sourcing, CQRS, Stream Processing and Apache Kafka: What’s the Connection?
>Author:: [[Neha Narkhede]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2016-09-06]]
>Last-Highlighted-Date:: [[2022-12-31]]
>Readwise-Link:: https://readwise.io/bookreview/22702438
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://www.confluent.io/blog/event-sourcing-cqrs-stream-processing-apache-kafka-whats-connection/
--- 

## Linked Notes
```dataview
LIST
FROM [[Event Sourcing, CQRS, Stream Processing and Apache Kafka: What’s the Connection? by Neha Narkhede Highlights]]
```

---

## Highlights
- Event sourcing as an application architecture pattern is rising in popularity. Event sourcing involves modeling the state changes made by applications as an immutable sequence or “log” of events. Instead of modifying the state of the application in-place, event sourcing involves storing the event that triggers the state change in an immutable log and modeling the state changes as responses to the events in the log. [View Highlight](https://readwise.io/open/446421194) ^rw446421194
- Event sourcing involves changing the profile web app to model the profile update as an event — something important that happened — and write it to a central log, like a Kafka topic. In this state of the world, all the applications that need to respond to the profile update event, merely subscribe to the Kafka topic and create the respective materialized views – be it a write to cache, index the event in Elasticsearch or simply compute an in-memory aggregate [View Highlight](https://readwise.io/open/446421360) ^rw446421360
- Event sourcing enables building a forward-compatible application architecture — the ability to add more applications in the future that need to process the same event but create a different materialized view. [View Highlight](https://readwise.io/open/446421450) ^rw446421450
