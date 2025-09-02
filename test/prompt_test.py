from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import load_prompt
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# DB_PATH = "./chroma_db"
# db = Chroma(
#     persist_directory=DB_PATH,
#     embedding_function=embeddings,
#     collection_name="enneagram_db"
# )

# retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 6, "lambda_mult": 0.1, "fetch_k": 10})

# 단계 6: 프롬프트 생성(Create Prompt)
prompt = load_prompt("./prompt.yaml", encoding="utf-8")

# 단계 7: 언어모델(LLM) 생성
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# 단계 8: 체인(Chain) 생성
# chain = (
#     {"context": retriever, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )

question = ("8유형 사람에게 마음에 드려면 어떻게 해야해?")
# response = chain.invoke(question)
# print(response)
#
# print("---------------------------------")

prompt2 = PromptTemplate.from_template("""
You are an assistant for question-answering tasks.  
If the question is not related to the Enneagram, please say you don't know.
If you don't know the answer, just say that you don't know.
Answer in Korean.

#Question:
{question}

#Answer:
""")

chain2 = (
    {"question": RunnablePassthrough()}
    | prompt2
    | llm
    | StrOutputParser()
)
response2 = chain2.invoke(question)
print(response2)