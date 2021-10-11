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

" Dividend Portfolio "

from typing import List, Optional

import yfinance as yf
from datetime import datetime, timedelta

class DividendPorfolio(object):
    """
    Class for dividend porfolio.
    """

    def __init__(self, 
                    tickers = List[str],
                 ) -> None:
        r"""
        Initialization of the DividendPorfolio class
        Args:
            tickers: List of tickers symbols.
        """

        # Get parameters
        self._tickers = [yf.Ticker(t) for t  in tickers]
        self._symbols = [t.get_info()["symbol"] for t in self._tickers]

    def get_exDividendDates(self,
                        date_format: Optional[str] = '%Y-%m-%d',
                        ) -> dict:
        r"""
        Get all the ex-dividend dates.
        Args:
            date_format: Date format. Default '%Y-%m-%d'.
        Return:
            exDividendDates: Dictionary with ticker symbols as keys and ex-dividend dates as values.
        """
        
        # Get parameter
        self._date_format = date_format

        # Put ex-devidend dates into a dictionary with the method get_info
        exDividendDates = {}
        for t in self._tickers:
            info = t.get_info()
            exDividendDates[info["symbol"]] = datetime.utcfromtimestamp(info['exDividendDate']).strftime(date_format)

        self._exDividendDates = exDividendDates
        return exDividendDates

    def write_ics(self,
                save_path: Optional[str] = ".",
                calendar_name: Optional[str] = "ex-Dividend Dates",
                start_date: Optional[str] = None,
                end_date: Optional[str] = None
                ) -> None:
        r"""
        Save all the ex-dividend dates in a ics file.
        Args:
            save_path (Optional): The path where the .ics file is saves.
            calendar_name (Optional): name of the ics file.
        """

        from ics import Calendar, Event

        # Check if the ex-divdend dates exist, if not get_exDividendDates
        try:
            exDividendDates = self._exDividendDates
        except AttributeError:
            exDividendDates = self.get_exDividendDates()

        # Check start and end date
        if start_date is not None:
            start_date = datetime.strptime(start_date, self._date_format)
        if end_date is not None:
            end_date = datetime.strptime(end_date, self._date_format)

        # Put all dates as events into a ics file
        c = Calendar()
        ind = 0
        while ind < len(self._symbols):

            ticker = self._symbols[ind]
            date = datetime.strptime(exDividendDates[ticker], self._date_format)

            try: 
                if date > start_date:
                    try:
                        if date < end_date:
                            e = Event()
                            e.name = "[ExDivDate] " + ticker
                            e.begin = date
                            e.make_all_day()
                            c.events.add(e)
                    except TypeError:
                            e = Event()
                            e.name = "[ExDivDate] " + ticker
                            e.begin = date
                            e.make_all_day()
                            c.events.add(e)
            except TypeError:
                try:
                    if date < end_date:
                        e = Event()
                        e.name = "[ExDivDate] " + ticker
                        e.begin = date
                        e.make_all_day()
                        c.events.add(e)
                except TypeError:
                        e = Event()
                        e.name = "[ExDivDate] " + ticker
                        e.begin = date
                        e.make_all_day()
                        c.events.add(e)
            ind+=1

        print(start_date, end_date, c.events)
        with open(save_path + "/" + calendar_name + '.ics', 'w') as my_file:
            my_file.writelines(c)