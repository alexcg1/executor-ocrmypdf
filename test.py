from docarray import DocumentArray
from jina import Flow
from executor import OCRMyPDF

# print-to-pdf of https://courses.cs.vt.edu/csonline/AI/Lessons/VisualProcessing/OCRscans_files/bowers.jpg
docs = DocumentArray.from_files("./data/bowers*.pdf")

flow = (
    Flow()
    .add(uses=OCRMyPDF, name="ocrpdf")
    .add(uses="jinahub://PDFSegmenter", name="segmenter", install_requirements=True)
)

with flow:
    output = flow.index(docs, show_progress=True)

for chunk in output[0].chunks:
    print(chunk)
    if hasattr(chunk, "text"):
        print(chunk.text)
