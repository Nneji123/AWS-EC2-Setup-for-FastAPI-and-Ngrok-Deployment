from fastapi import FastAPI
from colabcode import ColabCode

app = FastAPI()
@app.get('/')
def home():
    return {'Title': 'Super Resolution and Colorisation API'}


cc = ColabCode(port=18000, code=False)
cc.run_app(app=app)