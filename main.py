# -*- coding: utf-8 -*-
#
# Written by Adel Sohbi, https://github.com/adelshb
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test script. """

from argparse import ArgumentParser

from pf.divporfolio import DividendPorfolio

def main(args):

    with open(args.tickers_filename) as file:
        tickers = file.readlines()
        tickers = [ticker.rstrip() for ticker in tickers]

    DP = DividendPorfolio(tickers)
    DP.write_ics(start_date=args.start_date, end_date=args.end_date)
    # from IPython import embed; embed()

if __name__ == "__main__":

    parser = ArgumentParser()

    # Tickers
    # parser.add_argument("--tickers", type=int, nargs='+', default=["MSFT", "BLK"])
    parser.add_argument("--tickers_filename", type=str, default="tickers.txt")

    # Calendar
    parser.add_argument("--start_date", type=str, default="2021-10-11")
    parser.add_argument("--end_date", type=str, default="2021-12-31")
    
    args = parser.parse_args()
    main(args)
