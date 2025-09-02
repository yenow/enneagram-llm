from app.models.llm_models import LlmRequest, LlmResponse
from app.core.config import LLM_MODEL_NAME
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import asyncio
import uuid
import json

def get_llm_response(request: LlmRequest) -> LlmResponse:

    llm = ChatOpenAI(
        temperature=0.1,  # 창의성 (0.0 ~ 2.0)
        model=LLM_MODEL_NAME,  # 모델명
    )

    prompt = load_prompt("./prompt.yaml", encoding="utf-8")

    chain = (
            {"question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )

    response = chain.invoke(request.query)
    print(response)

    return LlmResponse(response=response, model_used=LLM_MODEL_NAME)

def get_test_llm_response(request: LlmRequest) -> LlmResponse:

    llm = ChatOpenAI(
        temperature=0.1,  # 창의성 (0.0 ~ 2.0)
        model=LLM_MODEL_NAME,  # 모델명
    )

    prompt = load_prompt("./prompt.yaml", encoding="utf-8")

    chain = (
            {"question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )

    response = chain.invoke(request.query)
    print(response)

    return LlmResponse(response=response, model_used=LLM_MODEL_NAME)

async def stream_llm_generator(request: LlmRequest):
    query_id = str(uuid.uuid4())
    llm = ChatOpenAI(
        temperature=0.1,
        model=LLM_MODEL_NAME,
    )

    prompt = load_prompt("./prompt.yaml", encoding="utf-8")

    chain = (
            {"question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )

    try:
        async for chunk in chain.astream(request.query):
            if chunk:
                data_to_send = {
                    "queryId": query_id,
                    "content": chunk,
                }
                yield f"data: {json.dumps(data_to_send, ensure_ascii=False)}\n\n"
                await asyncio.sleep(0.01)

    except Exception as e:
        print(f"!!! An error occurred during LLM stream: {e}")
        error_data = {
            "queryId": query_id,
            "content": f"\n\n[오류 발생: {e}]",
        }
        yield f"data: {json.dumps(error_data, ensure_ascii=False)}\n\n"
        return

    yield "event: end\n"
    yield "data: Stream finished\n\n"
