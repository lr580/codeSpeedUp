## 简介

码上速成 / Code Speed-Up

> 游戏命名建议采自 GPT4

游戏功能：

1. 使用多行文本框输入给定的代码；正确输入的地方绿色显示，错误红色；实时显示正确率与速度；可以随时暂停。
2. 选择多种不同语言的不同代码段进行自由练习。
3. 可以将你的用时上传，与其他人做排行对比。

代码目录：

- `frontend/` 前端
- `backend/` 后端
- `backend/data/` 数据层(暂不使用数据库)

## 运行方法

1. 运行后端：(安装依赖)

```sh
cd backend # 在项目根目录打开 backend/ ;请安装 python 依赖，具体略
python server.py # 运行服务器后端
# 后台运行：nohup python3 server.py &
# 关闭后台运行：ps aux | grep server.py 然后 kill -9 PID (PID 是第二列值)
```

2. 运行前端：

  ```sh
  cd frontend # 在项目根目录打开 frontend/
  npm run i # 如果还没安装依赖，先安装
  npm run dev # 如果要部署到服务器，可以 npm run build，然后使用 Nginx 等方法
  ```

部署方法略，比较简单不再赘述。请根据具体情况修改前后端配置文件，如 URL 地址，端口号。(分别是 `frontend/src/config.js` 和 `backend/config.yml`)

> 前端配置文件参考：(`config.js`)
>
> ```js
> export default {
>     serverURL: 'http://localhost:5802',
>     icp: '粤ICP备2024123456号',
>     icpHref: 'https://beian.miit.gov.cn/'
> };
> ```

## 数据说明

### 关卡数据

数据根目录一般为 `backend/data/`，可以根据配置文件(`backend/configs.yml`)修改。

关卡按照类别划分，每个类别是 `data/` 下的文件夹。

每个文件夹下存储若干文件，文件完整名(含后缀名)是该关卡的名字。

每个关卡有描述，数据根目录下，有 `levelDesc.yml` 配置文件，按类别存储每个关卡的代码文件的描述。其格式为：

```yaml
文件夹名:
    文件名: 字符串描述
    文件名: 字符串描述
文件夹名:
    文件名: 字符串描述
    文件名: 字符串描述
# ...
```

会根据该配置文件读取文件夹列表，而不是遍历文件夹来看有哪些类别。

数据根目录下，有 `levelTypeName.yml` 配置文件，存储每个关卡类别的名字。格式如：

```yaml
文件夹名: 类别名
```



### 排行数据

因为数据量少，懒得用数据库了，直接使用文本来存储每个关卡的排行数据。

使用 `.txt` 存储每个提交数据，在 1e5 数据内都表现理论良好。存储路径为 `data/rank/关卡类型名/关卡名.txt`。(如 `data/rank/Python语法/HelloWorld.py.txt`)

## 未来改进

欢迎就包括但不限于下面的方面提交 PR 或宝贵的建议：

1. 自动/跟随滚动，代码参考区横竖都随着输入区而滚动。
2. 修改判定逻辑，如对 C++ 忽略所有换行和空格，但是有很多细节。
