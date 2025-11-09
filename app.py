from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="YouthGuard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "YouthGuard API is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "YouthGuard Backend"}

@app.get("/api/reports")
def get_reports():
    return {"reports": [
        {"id": 1, "type": "Harassment", "location": "Nairobi", "status": "active"},
        {"id": 2, "type": "Theft", "location": "Mombasa", "status": "resolved"}
    ]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
