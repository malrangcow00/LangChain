# 'from langchain import PromptTemplate' was deprecated
from langchain_core.prompts import PromptTemplate
# langchain_community.chat_models.openai.ChatOpenAI` was deprecated
# To use it run `pip install -U langchain-openai` and import as `from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print('Hello, Langchain!')

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
        linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
    )

    # The function `run` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
    print(chain.run(information=linkedin_data))
    # invoke 사용시 제대로 전달되지 않으나 ... 현재 토큰 부족으로 테스트 불가
    # print(chain.invoke(input={"information": linkedin_data}))
    '''
    {'information': {'public_identifier': 'harrison-chase-961287118', 'profile_pic_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/harrison-chase-961287118/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20240409%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20240409T055654Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=dcc7082942221a0732d935d2f63e83acb5ab53f98d99b44d17f7da97cfe0c225', 'first_name': 'Harrison', 'last_name': 'Chase', 'full_name': 'Harrison Chase', 'follower_count': 9554, 'occupation': 'Co-Founder and CEO at LangChain', 'headline': 'Co-Founder and CEO at LangChain', 'summary': '{sports, machine learning, software engineering, statistics}', 'country': 'US', 'country_full_name': 'United States of America', 'city': 'San Francisco', 'state': 'California', 'experiences': [{'starts_at': {'day': 1, 'month': 1, 'year': 2023}, 'ends_at': None, 'company': 'LangChain', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/langchain', 'title': 'Co-Founder and CEO', 'description': None, 'location': 'San Francisco Bay Area', 'logo_url': 'https://media.licdn.com/dms/image/D560BAQGTObF4UNvy4A/company-logo_400_400/0/1708009961301/langchain_logo?e=1717632000&v=beta&t=Cxb7Hy9V48eJErTp8ZCGUvrERPvfbs2VHiR016zQOrc'}, {'starts_at': {'day': 1, 'month': 10, 'year': 2019}, 'ends_at': {'day': 31, 'month': 1, 'year': 2023}, 'company': 'Robust Intelligence', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/robust-intelligence', 'title': 'Machine Learning Engineer', 'description': None, 'location': None, 'logo_url': 'https://media.licdn.com/dms/image/C560BAQG6ByyNGNci0w/company-logo_400_400/0/1658120310534/robust_intelligence_logo?e=1717632000&v=beta&t=lC4ZBEVoC4Cz9SVeefToD5haZ_sXerHnC9LKeK2mGC4'}, {'starts_at': {'day': 1, 'month': 7, 'year': 2017}, 'ends_at': {'day': 31, 'month': 10, 'year': 2019}, 'company': 'Kensho Technologies', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/kensho-technologies', 'title': 'Machine Learning Engineer', 'description': None, 'location': None, 'logo_url': 'https://media.licdn.com/dms/image/C560BAQHQ4hJleHE7Vw/company-logo_400_400/0/1675961374389/kensho_technologies_logo?e=1717632000&v=beta&t=Tyqbcbu8BKYotaZtC67x_ZQJZX3ic5eY3xPbVbZNvXE'}], 'education': [{'starts_at': {'day': 1, 'month': 1, 'year': 2013}, 'ends_at': {'day': 31, 'month': 12, 'year': 2017}, 'field_of_study': None, 'degree_name': None, 'school': 'Harvard University', 'school_linkedin_profile_url': 'https://www.linkedin.com/company/1646/', 'description': None, 'logo_url': 'https://media.licdn.com/dms/image/C4E0BAQF5t62bcL0e9g/company-logo_400_400/0/1631318058235?e=1717632000&v=beta&t=M21XaAC1NOgSwUfahbcIkupo6AnJlbMOAqK7RYYAc2I', 'grade': None, 'activities_and_societies': None}], 'connections': 2024, 'recommendations': ['Sam Shleifer\n\n\n\nI hired Harrison in 2016 at Kensho and that was the most impactful thing I did for the firm in my 3  years there. He is willing to do whatever it takes to help the team, from feature engineering/experiment running, to tricky backend tasks that he had no idea how to do and figured out. For example, he figured out how to cut down the memory overhead of our multiprocessing workloads by 5x just by reading about how multiprocessing works and profiling the code, most data scientists I have worked with do not go that deep into "backend" programming. \n\nHe is also very strong at prioritizing next steps and isolating bottlenecks. For example, he identified a moment when a model was good enough to put in front of users (I wanted to keep making it better) and reoriented me towards doing the data engineering necessary to get the model out the door.  His next step intuition is so good that even when I was meant to be managing him I would send him my plan for every day to get his feedback, and this ended up saving me a huge amount of time. Harrison is a very strong python programmer and a careful code reviewer — he will take the bugs that nobody wants to fix, even if he didn’t create them, or provide a useful solution concept to a less experienced programmer if he thinks they would benefit from implementing it themselves.\n\nFinally, Harrison has an uncanny ability to generate significant model improvements by looking model at errors and thinking of features that might explain those differences. This skill is not only relevant with Timeseries and text data, which we worked on at Kensho — we did a sports project together and it was exactly the same. In conclusion, Harrison knows exactly what features need to be built and consistently gets to a point where the model is good enough to productionize, and also has the skills to productionize and get feedback from users.'], 'groups': [{'profile_pic_url': 'https://media.licdn.com/dms/image/C5607AQG-nbIUJbOhRg/group-logo_image-shrink_48x48/0/1630999209236?e=1710460800&v=beta&t=5mHtv2MGPoceQWU50yxvtLKdeuEVqKulDL8OKb6yEAo', 'name': 'Harvard Engineering and Applied Sciences Alumni', 'url': 'https://www.linkedin.com/groups/13881335'}, {'profile_pic_url': 'https://media.licdn.com/dms/image/C5607AQH6AydVJ99PdQ/group-logo_image-shrink_48x48/0/1631419369862?e=1710460800&v=beta&t=fXO9ry2Voxi9p_pwekO5CWids025xeqJt2cwLg-SBhM', 'name': 'HSAC Members & Alumni', 'url': 'https://www.linkedin.com/groups/13504297'}]}, 'text': '1. Harrison Chase is the Co-Founder and CEO of LangChain, a company based in San Francisco, California. He has a background in machine learning, software engineering, and statistics, with a strong focus on sports-related projects.\n\n2. Two interesting facts about Harrison Chase:\n   - He has a strong track record of improving models by identifying key features and prioritizing next steps for model deployment.\n   - Harrison is known for his willingness to tackle challenging backend tasks and his ability to provide valuable feedback and solutions to less experienced programmers.'}
    '''



    # 정상 출력 시
    '''
    1. Short Summary:
    Harrison Chase is the Co-Founder and CEO of LangChain, a sports, machine learning, software engineering, and statistics enthusiast based in San Francisco, California. With a background in machine learning engineering and a strong educational foundation from Harvard University, Harrison is known for his exceptional programming skills, prioritization abilities, and knack for generating significant model improvements.
    
    2. Two Interesting Facts:
    - Harrison has a keen eye for identifying bottlenecks and prioritizing next steps, which has proven to be invaluable in his roles as a machine learning engineer and CEO.
    - He is highly skilled in Python programming and is known for his meticulous code reviewing process, often taking on challenging bugs and providing useful solutions to less experienced programmers.
    '''