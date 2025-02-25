import requests

# Ollama服务的地址和端口
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# 要使用的模型名称
MODEL_NAME = "deepseek-r1:1.5b"  # 请根据实际情况替换为您想要使用的模型名


def get_chat_response(prompt):
    """
    发送对话请求到Ollama API，并返回响应。
    :param prompt: 用户输入的消息内容。
    :return: 模型生成的回复。
    """
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False  # 如果需要流式传输结果，请设置为True
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Received status code {response.status_code}")
        return None


if __name__ == "__main__":
    user_input = input("请输入您的问题或消息：")
    result = get_chat_response(user_input)

    if result:
        # 输出模型的回复
        print("模型回复:", result.get('message').get('content'))