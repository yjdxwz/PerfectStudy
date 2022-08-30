from fastapi import FastAPI, Request
# jinja2 模板渲染
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("pages")


@app.get("/")
def user(username,req: Request):

    # template.get_template("index.html")
    return template.TemplateResponse("index.html", context={"request": req,"username":username})
