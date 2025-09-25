# utils/file_loader.py

import pandas as pd

# tenta importar pypdf (moderno) e em fallback tenta PyPDF2
try:
    from pypdf import PdfReader as _PdfReader
    _READER_NAME = "pypdf"
except ImportError:
    try:
        from PyPDF2 import PdfReader as _PdfReader
        _READER_NAME = "PyPDF2"
    except ImportError:
        _PdfReader = None
        _READER_NAME = None


def load_pdf(path):
    """
    Retorna o texto do PDF em `path`.
    Lança RuntimeError se nenhum leitor estiver instalado.
    """
    if _PdfReader is None:
        raise RuntimeError("pypdf ou PyPDF2 não está instalado. Rode: pip install pypdf")

    # abrir como caminho (funciona na maioria das versões) ou usar file object:
    try:
        reader = _PdfReader(path)
    except TypeError:
        # algumas versões requerem file-like object
        with open(path, "rb") as f:
            reader = _PdfReader(f)

    texts = []
    for page in getattr(reader, "pages", []):
        # compatibilidade: extract_text (novo) ou extractText (antigo)
        if hasattr(page, "extract_text"):
            texts.append(page.extract_text() or "")
        elif hasattr(page, "extractText"):
            texts.append(page.extractText() or "")
    return "\n".join(texts)


def load_excel(path):
    """
    Lê um arquivo Excel (.xlsx, .xls) e retorna um DataFrame do pandas.
    """
    try:
        df = pd.read_excel(path, engine="openpyxl")
        return df
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar Excel: {e}")

