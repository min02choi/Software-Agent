import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent


def execute_sparql(query):
    # SPARQL 쿼리를 실행하는 로직
    return "SPARQL 실행 결과"


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# AI 어시스턴트 에이전트 생성(llm default 값은 gpt4)
assistant = AssistantAgent(name="CodingAssistant", llm_config={"model": "gpt-4o-mini"})
kg_agent = AssistantAgent(
    name="KGAgent",
    llm_config={"model": "gpt-4o-mini"},
    system_message="당신은 지식 그래프 전문가입니다. SPARQL 쿼리를 생성하고 실행하여 답변을 도출하세요.",
    tools=[{"name": "SPARQLExecutor", "type": "function", "function": execute_sparql}]
)
research_agent = AssistantAgent(
    name="ResearchAgent",
    llm_config={"model": "gpt-4o-mini"},
    system_message="당신은 연구 보조 에이전트입니다. 논문을 검색하고 요약하며, 비교 분석하는 역할을 합니다. Arxiv API를 활용하여 최신 논문을 검색하세요."
)
coding_agent = AssistantAgent(
    name="CodingAssistant",
    llm_config={"model": "gpt-4o-mini"},
    system_message="당신은 코드 작성과 디버깅을 도와주는 AI입니다. 주어진 프로그래밍 문제를 해결하고 최적의 코드를 제공하세요."
)

# 유저 역할의 프록시 에이전트 생성
user = UserProxyAgent(
    name="User",
    llm_config={"model": "gpt-4o-mini"},
    code_execution_config={"use_docker": False}
    )
# 유저 프록시 에이전트 1 (데이터 분석가 역할)
user1 = UserProxyAgent(name="DataAnalyst", llm_config={"model": "gpt-4o-mini"})

# 유저 프록시 에이전트 2 (지식 그래프 전문가 역할)
user2 = UserProxyAgent(name="KGExpert", llm_config={"model": "gpt-4o-mini"})


# 유저가 AI에게 질문하기
user.initiate_chat(assistant, message="Python으로 리스트의 중복을 제거하는 방법을 알려줘.")

