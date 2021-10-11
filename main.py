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

from typing import List, Optional

from pf.divporfolio import DividendPorfolio

def main(tickers: List[str],
        start_date: Optional[str] = "2021-10-11",
        end_date: Optional[str] = "2021-12-17"
        ) -> None:

    DP = DividendPorfolio(tickers)
    DP.write_ics(start_date=start_date, end_date= end_date)
    # from IPython import embed; embed()

if __name__ == "__main__":

    # filename = "div_portfolio_tickers.txt"
    # with open(filename) as file:
    #     lines = file.readlines()
    #     lines = [line.rstrip() for line in lines]
    tickers = ["MSFT", "BLK"]  
    main(tickers)
