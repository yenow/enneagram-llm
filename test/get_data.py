from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
import pprint

load_dotenv()

DB_PATH = "./chroma_db"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings,
    collection_name="enneagram_db",
)
result = db.get()
print(len(result['ids']))
print(len(result['documents']))

search = db.similarity_search("돈 리처드 리소에 대해서 알려줘", k=2)

