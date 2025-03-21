import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# AI 어시스턴트 에이전트 생성(llm default 값은 gpt4)
assistant = AssistantAgent(name="CodingAssistant", llm_config={"model": "gpt-4o-mini"})
# 유저 역할의 프록시 에이전트 생성
user = UserProxyAgent(
    name="User",
    llm_config={"model": "gpt-4o-mini"},
    code_execution_config={"use_docker": False}
    )

# 유저가 AI에게 질문하기
user.initiate_chat(assistant, message="Python으로 리스트의 중복을 제거하는 방법을 알려줘.")
