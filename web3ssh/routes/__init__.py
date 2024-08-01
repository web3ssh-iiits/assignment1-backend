from fastapi import APIRouter
from importlib import import_module
from os import walk
from os.path import join

router = APIRouter()

for path, _, files in list(walk("./web3ssh/routes")):
    if path.endswith("__pycache__"):
        continue
    route = ("/" + path.replace("./web3ssh/routes", "").replace("\\", "/")).replace(
        "//", "/"
    )
    if route.endswith("/"):
        route = route[:-1]
    sub_router = APIRouter(prefix=route)
    for file in files:
        file_name = file.replace(".py", "")
        if file.startswith(("test", "__")):
            continue
        print(
            join(path, file)
            .replace(".py", "")
            .replace("\\", "/")
            .replace("/", ".")
            .replace("..", "")
        )
        file = import_module(
            join(path, file)
            .replace(".py", "")
            .replace("\\", "/")
            .replace("/", ".")
            .replace("..", "")
        )
        if not file or not bool(file.router) or not isinstance(file.router, APIRouter):
            print("NOT WORKING")
            continue
        sub_router.include_router(file.router, prefix="/" + file_name)
    router.include_router(sub_router)
