from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from app.models.llm_models import LlmRequest, LlmResponse
from app.services.llm_service import get_llm_response, get_test_llm_response, stream_llm_generator

router = APIRouter()

@router.post("/llm", response_model=LlmResponse, summary="Simulated LLM endpoint")
def llm_simulation_endpoint(request: LlmRequest):
    response = get_llm_response(request)
    return response


@router.post("/llm/test", response_model=LlmResponse, summary="Actual LLM test endpoint")
def llm_real_test_endpoint(request: LlmRequest):
    response = get_test_llm_response(request)
    return response


@router.get("/llm/stream", summary="Streaming LLM endpoint (GET)")
async def llm_stream_get_endpoint(
    query: str = Query(..., description="The query to send to the LLM."),
    temperature: float = Query(0.7, description="The temperature for the LLM response.")
):
    # Create an LlmRequest object from query parameters to pass to the service layer
    request_data = LlmRequest(query=query, temperature=temperature)
    return StreamingResponse(stream_llm_generator(request_data), media_type="text/event-stream")