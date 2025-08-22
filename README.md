# 에니어그램 Chat-RAG Server 

## Setup

1. 의존성 설치:
    ```bash
    pip install -r requirements.txt
    ```
   
## 실행
1. 앱 실행:
    ```bash
    uvicorn main:app --reload
    ```

2. 도커 컴포즈로 실행
    ```bash
    docker-compose up 
    # 백그라운드 실행
    docker-compose up -d
    ```

## 도커 이미지
도커 이미지 만들기
```bash
  docker build -t enneagram-llm-local:latest .
 ```
도커 이미지 리스트
```bash
  docker images enneagram-llm-local
 ```
도커로 이미지 실행
```bash
   # LLM
   docker run -d --rm -p 8000:8000 --name enneagram-llm-local enneagram-llm-local:latest
   # Backend
   docker run -d --rm -p 8080:8080 --name enneagram-backend-local -e SPRING_PROFILES_ACTIVE=docker enneagram-backend-local:latest
 ```

## Swagger UI
http://localhost:8000/docs