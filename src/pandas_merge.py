'''
Created on Oct 2, 2017

@author: djames

Sandbox to create some dataframes and merge them, simple examples.




'''
# https://stackoverflow.com/questions/41815079/pandas-merge-join-two-data-frames-on-multiple-columns
from pprint import pprint as pp
import time
import pandas as pd
from pandas.io.excel import ExcelWriter
from manipulate_sheets import auto_width
# import numpy as np
# import matplotlib.pyplot as plt


DF1 = pd.DataFrame({"P1": "enabled",
                    "P2":  ["on", "on", "off", "off"],
                    "P3": ["on", "off", "on", "off"],
                    "R": [1, 2, 3, 4]
                    })

DF1C = pd.DataFrame({"P1": "enabled",
                     "P2":  ["on", "on", "off", "off"],
                     "P3": ["on", None, "on", None],
                     "R": [1, 2, 3, 4]
                    })
# short DF1
DF1B = pd.DataFrame({"P1": "enabled",
                     "P2":  ["on", "on", "off"],
                     "P3": ["on", "off", "on"],
                     "R": [1, 2, 3]
                    })

DF1D = pd.DataFrame({"P1": "ReallyReallyReallyReally wide",
                     "P2":  ["on", "on", "off", "off"],
                     "P3": ["on", "off", "on", "off"],
                     "R": [1, 2, 3, 4]
                    })

DF2 = pd.DataFrame({"P1": "enabled",
                    "P2":  ["on", "on", "off", "off"],
                    "P3": ["on", "off", "on", "off"],
                    "R": [5, 6, 7, 8]
                   })
# extra 'P" column
DF3 = pd.DataFrame({"P1": "enabled",
                    "P2":  ["on", "on", "off", "off"],
                    "P3": ["on", "off", "on", "off"],
                    "P4": ["on", "off", "on", "off"],
                    "R": [11, 12, 13, 14]
                   })

# shorter
DF4 = pd.DataFrame({"P1": "enabled",
                    "P2":  ["on", "on", "off"],
                    "P3": ["on", "off", "on"],
                    "P4": ["on", "off", "on"],
                    "R": [15, 16, 17]
                   })

frames = [DF1, DF2, DF3, DF4]
def name_of_object(arg):
    """
    Find name of an object, pull from globals if no specific __name__
    :param arg: an object
    """
    # pylint: disable=line-too-long
    # https://stackoverflow.com/questions/1538342/how-can-i-get-the-name-of-an-object-in-python - second answer
    # pylint: enable=line-too-long
    try:
        return arg.__name__
    except AttributeError:
        pass

    for name, value in globals().items():
        if value is arg and not name.startswith('_'):
            return name


def dpp(dataframe, cap=''):
    """
    Pretty print a dataframe, with name and optional caption
    :param dataframe:
    :param cap: caption  - string to include in the name line
    """
    print("\r" + cap + "(" + (name_of_object(dataframe) or '') + "):")
    pp(dataframe)


def merges():
    """
    A set of merge exercises
    """
    dpp(DF1)
    dpp(DF2)

    # yields an empty dataframe
    results1 = DF1.merge(DF2)
    dpp(results1, cap="null results")
    dpp(DF1.merge(DF2), cap="Inline Null results")

    # as successful merge,

    # left_on and right_on must be the same length, default suffixes are     _x and _y

    results2 = DF1.merge(DF2, left_on=["P1", "P2", "P3"], right_on=["P1", "P2", "P3"])
    dpp(results2)

    # Merge on two
    results3 = DF1.merge(DF2, left_on=["P2", "P3"], right_on=["P2", "P3"])
    dpp(results3, cap="Merge on P2 and P3")

    # hm... looks like the order is x, commmon x, y

    # merge, with extra column in b
    dpp(DF1)
    dpp(DF3)
    results4 = DF1.merge(DF3, left_on=["P1", "P2", "P3"], right_on=["P1", "P2", "P3"])
    dpp(results4)

    # merge, using column that is not in DF1
    try:
        dpp(DF1)
        dpp(DF3)
        results5 = DF1.merge(DF3, left_on=["P1", "P2", "P3", "P4"],
                             right_on=["P1", "P2", "P3", "P4"])
        dpp(results5)
    except KeyError as err:
        print(repr(err))
        print("join keys must be the same length, and present in their DF")

    # merge shorter into longer
    dpp(DF4)
    result5 = DF1.merge(DF4, left_on=["P1", "P2", "P3"], right_on=["P1", "P2", "P3"])
    dpp(result5, cap="Fewer rows on right than left")

    # merger longer(b), into shorter(a)
    dpp(DF1B)
    dpp(DF2)
    result6 = DF1B.merge(DF2, left_on=["P1", "P2", "P3"], right_on=["P1", "P2", "P3"])
    dpp(result6, cap="Fewer rows on left than right")

    # merger on a subset
    dpp(DF3)
    dpp(DF4)
    result7 = DF3.merge(DF4, left_on=["P1", "P3"], right_on=["P1", "P3"])
    dpp(result7, cap="subset of parameters")


def find_and_swap():
    '''A set of table manipulations'''
    # df.loc[df['line_race'] == 0, 'rating'] = 0
    # https://stackoverflow.com/questions/18196203/how-to-conditionally-update-dataframe-column-in-pandas

    dpp(DF1)
    DF1.loc[DF1['P3'] == 'off', 'P1'] = ' disabled'
    dpp(DF1)

    dpp(DF1C)
    DF1C.loc[DF1C['P3'].isnull(), 'P1'] = ' disabled'
    dpp(DF1C)
    DF1C.loc[DF1C['P3'].isnull(), 'P3'] = 'off'
    dpp(DF1C, cap="with P3 'fixed'")


def excel_format():
    '''format in memory'''
    START = time.strftime('%y%m%d-%H%M%S')
    OUTFILE = 'TEST' + START + '.xlsx'

    writer = ExcelWriter(OUTFILE)
    DF1D.to_excel(writer)
    writer.save()
    wb = writer.book
    auto_width(wb['Sheet1'])
    wb.save(writer.path)

if __name__ == '__main__':

    #     merges()
    #     find_and_swap()
    for _ in frames:
        dpp(_)

