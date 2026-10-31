from fastapi import FastAPI, Header, HTTPException
import jwt

app = FastAPI(title="BOLA Vulnerable API")

SECRET_KEY = "supersecretkey"

users_db = {
    1: {"id": 1, "name": "Rahul Sharma", "email": "rahul@example.com", "balance": 5000},
    2: {"id": 2, "name": "Simran Kashyap", "email": "simran@example.com", "balance": 15000}
}

@app.get("/")
def home():
    return {
        "message": "API Security Framework Target Online",
        "version": "2.0",
        "status": "Secure"
    }

@app.post("/login/{user_id}")
def login(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

# VULNERABLE ENDPOINT (BOLA Bug)
@app.get("/api/v1/user/{user_id}/profile")
def get_user_profile(user_id: int, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization Header Missing")
    
    try:
        token = authorization.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        # BOLA BUG: Token decoded user_id cross-check missing
        if user_id in users_db:
            return users_db[user_id]
        raise HTTPException(status_code=404, detail="User profile not found")
        
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Token")

# SECURED ENDPOINT (BOLA Fixed)
@app.get("/api/v2/user/{user_id}/profile")
def get_user_profile_secured(user_id: int, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization Header Missing")
    
    try:
        token = authorization.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        # SECURITY FIX: Validate that token owner matches requested resource ID
        if decoded.get("user_id") != user_id:
            raise HTTPException(status_code=403, detail="Forbidden: You cannot access another user's profile")
        
        if user_id in users_db:
            return users_db[user_id]
        raise HTTPException(status_code=404, detail="User profile not found")
        
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Token")