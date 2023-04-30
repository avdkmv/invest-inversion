"""Requests tickers information and prints it"""

import sys
import argparse
import logging

from core import flow

logger = logging.getLogger("invest-inversion")


def configure_logger():
    logger = logging.getLogger("invest-inversion")
    logger.setLevel(logging.DEBUG)

    default_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s]: %(message)s",
        "%d/%m/%Y %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(default_formatter)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)


def parse_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "-t",
        "--tickers",
        type=str,
        required=False,
        nargs="+",
        default="SBER GAZP MTLR",
        help="List of tickers to get. Example: SBER GAZP MTLR",
    )
    argparser.add_argument(
        "-i",
        "--iterations",
        type=int,
        required=False,
        default=200,
        help="Amount of iterations",
    )

    args = argparser.parse_args()
    args.tickers = args.tickers.split()

    return args


def main():
    args = parse_args()
    configure_logger()

    ticker_info = flow.get_flow_info(tickers=args.tickers, iteration=args.iterations)

    for ticker_data in ticker_info:
        logger.info(ticker_data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
