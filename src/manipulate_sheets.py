'''
Created on Oct 6, 2017

@author: djames
'''

import openpyxl
from openpyxl import load_workbook
from openpyxl import chart
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter

# Auto Width
# https://stackoverflow.com/questions/13197574/openpyxl-adjust-column-width-size

def auto_width(sheet):
    column_widths = []
    for row in sheet.iter_rows():
        for i, cell in enumerate(row):
            try:
                print(str(cell.value))
                column_widths[i] = max(column_widths[i],len(str(cell.value)))
            except IndexError:
                column_widths.append(len(str(cell.value)))

    for i, column_width in enumerate(column_widths):
        sheet.column_dimensions[get_column_letter(i + 1)].width = column_width
def main():
    '''Main'''
    
    wb = load_workbook(filename='51-SysTst.xlsx')
    sum_sheet = wb['Summary']
    print(sum_sheet['B2'].value)
    print(len(sum_sheet["A1"].value or ''))
    print(len(str(sum_sheet["A1"].value)))
    auto_width(sum_sheet)
    wb.save(filename='51-SysTstPLUS.xlsx')
if __name__ == '__main__':
    main()