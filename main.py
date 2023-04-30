"""Requests tickers information and prints it"""

import sys
import argparse
import logging

from colorama import Fore

from core import flow

logger = logging.getLogger("invest-inversion")


def configure_logger():
    class CustomFormatter(logging.Formatter):
        def _get_msg(color_code):
            return f"%(asctime)s %(name)s {color_code}%(levelname)s{Fore.RESET}: %(message)s (%(filename)s:%(lineno)d)"

        FORMATS = {
            logging.DEBUG: _get_msg(Fore.YELLOW),
            logging.INFO: _get_msg(Fore.GREEN),
            logging.WARNING: _get_msg(Fore.LIGHTRED_EX),
            logging.ERROR: _get_msg(Fore.RED),
            logging.CRITICAL: _get_msg(Fore.MAGENTA),
        }

        def format(self, record):
            formatter = logging.Formatter(self.FORMATS[record.levelno])
            return formatter.format(record)

    logger = logging.getLogger("invest-inversion")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
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
        default=["SBER", "GAZP", "MTLR"],
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
