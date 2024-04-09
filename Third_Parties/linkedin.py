import environ
import requests

env = environ.Env()
env.read_env()


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
        scrape information from LinkedIn profiles,
        Manually scrape the information from the LinkedIn profile
    """

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {env("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic.url", None)

    return data


if __name__ == "__main__":
    # harrison chase is the creator of the langchain
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
    )
    print(linkedin_data)
