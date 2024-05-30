import yaml, os, uvicorn
from fastapi import FastAPI
configs = yaml.load(open("config.yml", "r", encoding='utf8'), Loader=yaml.FullLoader)

path_root = configs['datapath']
path_level = os.path.join(path_root, 'level')
path_rank = os.path.join(path_root, 'rank')
def initDataPath():
    os.makedirs(path_level, exist_ok=True)
    os.makedirs(path_rank, exist_ok=True)
initDataPath()

app = FastAPI()
@app.get("/")
def ping():
    return '码上速成后台服务器连接成功！'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=configs['port'])