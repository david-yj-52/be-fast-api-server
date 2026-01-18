# 1. 파이썬 베이스 이미지 지정 (JRE 설치된 OS 이미지 선택과 유사)
FROM python:3.11-slim

# 2. 서버 내 작업 디렉토리 설정
WORKDIR /app

# 3. 라이브러리 목록 복사 및 설치 (Maven 의존성 설치와 유사)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 전체 소스 코드 복사
COPY . .

# 5. 실행 명령 (Spring Boot의 java -jar 실행과 유사)
# main.py 안에 app = FastAPI() 가 있다고 가정합니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]