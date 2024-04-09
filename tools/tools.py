from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for a LinkedIn profile Page"""
    search = SerpAPIWrapper()
    result = search.run(f'{text}')
    return result
