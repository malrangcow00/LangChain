from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    prompt_template = """
            given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page. Your answer should contain only a URL
        """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func="?",
            description="useful for when you need get the LinkedIn page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linked_profile_url = result["output"]

    return linked_profile_url
