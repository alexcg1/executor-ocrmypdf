from jina import Executor, DocumentArray, requests
import ocrmypdf


class OCRMyPDF(Executor):
    """"""
    @requests
    def extract_text(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            ocrmypdf.ocr(input_file=doc.uri, output_file=doc.uri, force_ocr=True)
