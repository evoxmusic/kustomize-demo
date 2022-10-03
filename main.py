import os
import sys

from fastapi import FastAPI

app = FastAPI()


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down... Bye!")

    sys.exit(0)


@app.on_event("startup")
async def start_event():
    for env_key in ["KUBECONFIG_B64", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]:
        if os.getenv(env_key):
            print(f"{env_key} is set")
        else:
            print(f"{env_key} is not set")

    print("Kustomize scripts has been executed!")


@app.get("/")
async def root():
    return {"message": "Hello Kustomize Demo"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
