# OCRMyPDF

This Executor uses [OCRMyPDF](https://ocrmypdf.readthedocs.io/en/latest/) to extract text from OCRed PDFs and stores it "behind" the PDF pages. It doesn't write any textual data to the Document itself, but rather modifies the PDF file directly.

You can then use [PDFSegmenter](https://hub.jina.ai/executor/x9w7lcwg) to extract that textual content.

Input Documents should have their `uri` set to the PDF file location.

As far as I know this works for English only, but feel free to make a PR to add other language options.
