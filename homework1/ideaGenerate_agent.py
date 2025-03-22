from autogen import AssistantAgent, UserProxyAgent

# 사용자 프록시 에이전트 (사용자 입력을 처리)
user_agent = UserProxyAgent(name="User")

# 아이디어 생성 에이전트
idea_generator = AssistantAgent(
    name="Idea_Generator",
    system_message="당신은 창의적인 연구 아이디어 생성 전문가입니다. 사용자의 키워드를 바탕으로 새로운 연구 아이디어를 제안하세요."
)

# 검증 에이전트
validation_agent = AssistantAgent(
    name="Validation_Agent",
    system_message="당신은 연구 검증 전문가입니다. 제안된 연구 아이디어가 기존 연구와 얼마나 다른지 평가하고, 참신성을 분석하세요."
)

# 연구 계획서 작성 에이전트
proposal_writer = AssistantAgent(
    name="Proposal_Writer",
    system_message="당신은 연구 계획서 작성 전문가입니다. 최종 확정된 연구 아이디어를 기반으로 연구 계획서를 작성하세요."
)

# 연구 아이디어 브레인스토밍 흐름 정의
def brainstorming_session(keyword):
    # 1. 아이디어 생성
    user_agent.initiate_chat(idea_generator, message=f"연구 키워드: {keyword}에 대한 연구 아이디어를 생성해줘.")
    idea = idea_generator.get_last_message()
    
    # 2. 아이디어 검증
    user_agent.initiate_chat(validation_agent, message=f"이 연구 아이디어의 참신성을 평가해줘: {idea}")
    validated_idea = validation_agent.get_last_message()
    
    # 3. 연구 계획서 작성
    user_agent.initiate_chat(proposal_writer, message=f"이 연구 아이디어를 기반으로 연구 계획서를 작성해줘: {validated_idea}")
    proposal = proposal_writer.get_last_message()
    
    return proposal

# 실행 예시
if __name__ == "__main__":
    research_keyword = "지식 그래프 기반 질의응답 시스템"
    research_proposal = brainstorming_session(research_keyword)
    print("\n### 최종 연구 계획서 ###\n")
    print(research_proposal)
