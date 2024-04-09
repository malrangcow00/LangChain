import environ
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# environ.Env.read_env()
env = environ.Env()
env.read_env()

if __name__ == "__main__":
    information = """
        William Henry Gates III (born October 28, 1955) is an American businessman, investor, philanthropist, and writer best known for co-founding the software giant Microsoft, along with his childhood friend Paul Allen. During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president, and chief software architect, while also being its largest individual shareholder until May 2014.[2][a] He was a pioneer of the microcomputer revolution of the 1970s and 1980s.
    """

    summary_template = """
        given the infromation {information} about a person I want you to create:
        1. A short summary
        2. two interesting factsd about theme
    """
    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.invoke(input={"information": information})

    print(result)
