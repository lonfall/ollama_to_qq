## ollama本地deepseek R1模型对接qq开放平台机器人
### 连接ollama本地机器人
使用需要修改main.py中 `OLLAMA_API_URL` 字段 `MODEL_NAME` 字段<br>
运行main.py可以在控制台中输入与本地机器人对话，测试本地机器人的状态<br>
ollama本地机器人的搭建请自行搜索
### 对接qq开放平台机器人
请先在[qq开放平台](https://q.qq.com/#/)中注册机器人获取密钥<br>
需要修改config.yaml文件中 `appid`（机器人ID） 与 `secret`（机器人密钥）<br>
之后运行qqChat.py将会启动qq机器人，并自动调用本地机器人，回复群内@消息