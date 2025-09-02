import pprint
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# 단계 1: 문서 로드(Load Documents)
FILE_PATH = "./400_ocr.pdf"
loader = PyMuPDFLoader(FILE_PATH)
docs = loader.load()

# 1유형
pprint.pprint(docs[130].metadata)
print(docs[130].page_content)

# 2유형
pprint.pprint(docs[166].metadata)
print(docs[166].page_content)

# 3유형
pprint.pprint(docs[199].metadata)
print(docs[199].page_content)

# 4유형
pprint.pprint(docs[234].metadata)
print(docs[234].page_content)

# 5유형
pprint.pprint(docs[270].metadata)
print(docs[270].page_content)

# 6유형
pprint.pprint(docs[305].metadata)
print(docs[305].page_content)

# 7유형
pprint.pprint(docs[339].metadata)
print(docs[339].page_content)

# 8유형
pprint.pprint(docs[374].metadata)
print(docs[374].page_content)

# 9유형
pprint.pprint(docs[409].metadata)
print(docs[409].page_content)

# 442


