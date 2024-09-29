from utils.openai_utils import chat
from xbrain.tool import run_tool, tools


def run(messages):
    openai_tools = []
    for tool in tools:
        openai_tools.append(tool["model"])
    chat_response = chat(messages, tools=openai_tools)
    if chat_response.content is None:
        res = run_tool(chat_response)
    else:
        res = chat_response.content
    return res
    