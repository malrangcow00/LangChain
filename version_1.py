if __name__ == "__main__":
    print("This is version 1 for LangChain Practice")

import environ
import os

env = environ.Env()
environ.Env.read_env('.env.development')

print(os.getenv("SECRET_KEY"))
