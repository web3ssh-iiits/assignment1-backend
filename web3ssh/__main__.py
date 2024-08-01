from importlib import reload
import uvicorn
import asyncio
from web3ssh import app
from web3ssh.routes import router

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("web3ssh.__main__:app", reload=True)
