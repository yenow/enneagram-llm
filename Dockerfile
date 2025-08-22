# 1. Python 3.11 슬림 버전을 기반으로 이미지를 빌드합니다.
FROM python:3.11-slim

# 2. 작업 디렉토리를 /llm으로 설정합니다.
WORKDIR /llm

# 3. requirements.txt 파일을 이미지로 복사합니다.
COPY requirements.txt .

# 4. pip를 최신 버전으로 업그레이드하고, requirements.txt에 명시된 패키지를 설치합니다.
# --no-cache-dir 옵션은 이미지 크기를 줄이는 데 도움이 됩니다.
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# 5. 현재 디렉토리의 모든 파일을 이미지의 /llm 디렉토리로 복사합니다.
COPY . /llm

# 6. uvicorn을 사용하여 FastAPI 애플리케이션을 실행합니다.
# --host 0.0.0.0 옵션은 컨테이너 외부에서 애플리케이션에 접근할 수 있도록 합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
