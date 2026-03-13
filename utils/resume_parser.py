from pypdf import PdfReader

def parse_resume(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text