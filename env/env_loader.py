from dotenv import load_dotenv, find_dotenv

class EnvLoader:
    def loadEnv():
        load_dotenv(find_dotenv())
