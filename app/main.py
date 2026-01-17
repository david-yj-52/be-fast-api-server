from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. CORS 설정: 브라우저가 다른 도메인(Vercel)에서 로컬 API로 접근하는 것을 허용합니다.
app.add_middleware(
    CORSMiddleware,
    # Vercel 프로젝트 주소를 정확히 입력하거나, 테스트용으로 ["*"]를 사용할 수 있습니다.
    allow_origins=[
        "https://tsh-web-plate-71ahjm33t-david-yj-52s-projects.vercel.app",
        "http://localhost:3000"  # 로컬 개발 환경용
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """
    브라우저의 상태 체크 버튼 클릭 시 호출되는 엔드포인트
    """
    return {
        "status": "online",
        "message": "Local Agent is running"
    }

if __name__ == "__main__":
    import uvicorn
    # 8080 포트로 실행
    uvicorn.run(app, host="127.0.0.1", port=8080)