import re

import botpy
import os
from botpy.message import GroupMessage, Message
from botpy import logging
from botpy.ext.cog_yaml import read
from main import get_chat_response

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_at_message_create(self, message: GroupMessage):
        _log.info(message)
        # 获取消息内容
        content = message.content

        result = get_chat_response(content)

        msg_back = result.get('message').get('content')
        msg_back = re.sub(r'<think>.*?</think>', '', msg_back, flags=re.DOTALL)

        await self.api.post_group_message(group_openid=message.group_openid,
                                          content=msg_back,
                                          msg_id=message.id)

    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        # 获取消息内容
        content = message.content

        # 假设你想对特定的内容做出响应
        if "hello" in content.lower():
            await self.api.post_message(channel_id=message.channel_id,
                                        content="Hello back!",
                                        msg_id=message.id)


# 设置意图（Intents），这里仅监听公共频道的消息
intents = botpy.Intents(public_messages=True)

# 创建客户端实例
client = MyClient(intents=intents)

# 运行客户端，需要config.yaml配置文件中替换为你的app id和secret
client.run(appid=test_config["appid"], secret=test_config["secret"])
