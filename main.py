# 'from langchain import PromptTemplate' was deprecated
from langchain_core.prompts import PromptTemplate
# langchain_community.chat_models.openai.ChatOpenAI` was deprecated
# To use it run `pip install -U langchain-openai` and import as `from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from Agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from Third_Parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print('Hello, Langchain!')

    linkedin_profile_url = linkedin_lookup_agent(name="Harrison Chase")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. A short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=['information'], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    # The function `run` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
    print(chain.run(information=linkedin_data))
