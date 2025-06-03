from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from shared.lib.auth import create_access_token, verify_token

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/login")
async def login(username: str, password: str):
    # In production: verify against DB
    return {"access_token": create_access_token({"sub": username})}

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Access granted"}