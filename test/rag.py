import pprint
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import load_prompt
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# 단계 1: 문서 로드(Load Documents)
FILE_PATH = "./400_ocr.pdf"
loader = PyMuPDFLoader(FILE_PATH)
docs = loader.load()

# 단계 2: 문서 분할(Split Documents)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = text_splitter.split_documents(docs)
print(f"분할된 청크의수: {len(split_docs)}")
split_docs = split_docs[0:20]

# 단계 3: 임베딩(Embedding) 생성
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 단계 4: DB 생성(Create DB) 및 저장
DB_PATH = "./chroma_db"
db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings,
    collection_name="enneagram_db"
)
batch_size = 100
for i in range(0, len(split_docs), batch_size):
    db.add_documents(split_docs[i:i+batch_size])

# 단계 5: 검색기(Retriever) 생성
retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 6, "lambda_mult": 0.1, "fetch_k": 10})

# 단계 6: 프롬프트 생성(Create Prompt)
prompt = load_prompt("./prompt.yaml", encoding="utf-8")

# 단계 7: 언어모델(LLM) 생성
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# 단계 8: 체인(Chain) 생성
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

question = "에니어그램 4유형에 대해서 설명해줘"
response = chain.invoke(question)
print(response)