from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from core import flow


if __name__ == "__main__":
    tickers = flow.get_flow_info()

    for name in tickers:
        print(name)
