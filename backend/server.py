import yaml, os, uvicorn, glob
from fastapi import FastAPI
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

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=configs['port'])