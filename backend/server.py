import yaml, os, uvicorn, glob
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
configs = yaml.load(open("config.yml", "r", encoding='utf8'), Loader=yaml.FullLoader)

path_root = configs['datapath']
path_level = os.path.join(path_root, 'level')
path_rank = os.path.join(path_root, 'rank') 
def initDataPath(): # useless
    os.makedirs(path_level, exist_ok=True)
    os.makedirs(path_rank, exist_ok=True)
initDataPath()

# 访问 `/docs` 可以查看 API 文档
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ping():
    return '码上速成后台服务器连接成功！'

levelDesc = yaml.load(open(os.path.join(path_root, 'levelDesc.yml'), 'r', encoding='utf8'), Loader=yaml.FullLoader)
@app.get("/getLevelDesc")
def getLevelDesc():
    return levelDesc
@app.get("/getLevelTypeList")
def getLevelTypeList(): # useless
    return list(levelDesc.keys())
@app.get("/getAllLevels")
def getAllLevels(): # 因为关卡数据量少，就这样做了，关卡多再改吧
    result = {}
    for topic in levelDesc.keys():
        levels = {}
        for path in glob.glob(f'{path_level}/{topic}/*'):
            name = os.path.basename(path)
            with open(path, encoding='utf8') as f:
                levels[name] = f.read().strip()
        result[topic] = levels
    return result
# 以后再增加一关一关的 desc 和代码文本的 get 接口

class SubmitScoreData(BaseModel):
    name: str
    time: str
    score: int
    level: str
    levelType: str
@app.post('/submitScore')
def submitScore(data : SubmitScoreData):
    topicPath = os.path.join(path_rank, data.levelType)
    levelPath = os.path.join(topicPath, data.level+'.txt')
    os.makedirs(topicPath, exist_ok=True)
    dataLine = f'{data.name} {data.time} {data.score}\n'
    with open(levelPath, 'a', encoding='utf8') as f:
        f.write(dataLine)
    return {"message":"ok"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=configs['port'])