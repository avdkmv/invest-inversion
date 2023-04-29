import sys
import argparse

from core import flow

def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-t", "--tickers", type=str, required=False, nargs="+", default="SBER GAZP MTLR"
    )
    argparser.add_argument("-i", "--iterations", type=int, required=False, default=200)

    args = argparser.parse_args()
    args.tickers = args.tickers.split()

    return args


def main():
    args = parse_args()

    ticker_info = flow.get_flow_info(tickers=args.tickers, iteration=args.iterations)

    for ticker_data in ticker_info:
        print(ticker_data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
