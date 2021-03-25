# Scrapy Crawler Script

The reason of creating this repo is some troubles to integrate Scrapy with single-threaded tasks like Celery tasks, some Django features. Internet has a lot of solutions this problem, but some of them are already out of date.

### Used sources
- Similar legacy solution in answer to [StackOverflow question][stackoverflow-question]
- Solution based on [clemfromspace's gist][gist-of-clemfromspace]
- A [scrapyscrypt] library with more functionality, but problems with large data sizes [[1][scrapyscrypt-issue]]

<!-- Attachments -->
[gist-of-clemfromspace]: https://gist.github.com/clemfromspace/2edb88a79de3d6dde0d93c68354db385
[stackoverflow-question]: https://stackoverflow.com/questions/22116493/run-a-scrapy-spider-in-a-celery-task
[scrapyscrypt]: https://github.com/jschnurr/scrapyscript
[scrapyscrypt-issue]: https://github.com/jschnurr/scrapyscript/issues/3

