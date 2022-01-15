import datetime
import sys

import pandas as pd
import argparse

import xlsxwriter


def my_map(x):
    return x.strftime('%H:%M:%S')


def time_sq(rg_length, send=1):
    """
    :input [1, 2, 3]
    :return 一个时间序列
    :example:
        input: 3,2
        output:[datetime.datetime(1900, 1, 1, 0, 0),
        datetime.datetime(1900, 1, 1, 0, 0, 2),
        datetime.datetime(1900, 1, 1, 0, 0, 4)]

    """
    pd_date = pd.date_range("2021-1-1", periods=rg_length, freq=f'{send}s')
    return [datetime.datetime.strptime(i.strftime('%H:%M:%S'), '%H:%M:%S') for i in pd_date]


def hello(file_name, sends):
    # 构造数据
    list2 = []
    for lin2 in open(file_name):
        if lin2.startswith('[SUM]'):
            sw_str = lin2.strip('[SUM]')
            list1 = sw_str.split(' ')
            #
            # list2.append(list1[3])
            # list2.append(list1[6])
            # list2.append(list1[9])
            list2.append(float(list1[-2]))

    list2_len = len(list2)

    pd_date = time_sq(list2_len, sends)
    workbook = xlsxwriter.Workbook(file_name.split('.')[0] + '.xlsx')  # 创建新的excel

    worksheet = workbook.add_worksheet('sheet1')  # 创建新的sheet

    headings = ['Time', 'Data']  # 创建表头
    data = [
        pd_date,
        list2,

    ]
    time_formats = workbook.add_format({'num_format': 'hh:mm:ss'})
    worksheet.write_row("A1", headings)
    worksheet.write_column("A2", data[0], time_formats)
    worksheet.write_column("B2", data[1])
    chart_col = workbook.add_chart({'type': 'scatter'})

    x = f'=Sheet1!$A$2:$A${len(list2)}'
    y = f'=Sheet1!$B$2:$B${len(list2)}'

    chart_col.set_size({'width': 1500,
                        'height': 500})
    chart_col.add_series(
        {
            "name": '=sheet1!$B$1',
            "categories": x,
            "values": y,
            'marker': {'type': 'circle',
                       'size': 3,
                       'border': {'color': 'blue'},
                       'fill':   {'color': 'blue'}
                       },
        }
    )
    chart_col.set_title({'name': 'Date 点状图'})
    chart_col.set_x_axis({'name': "time"})
    chart_col.set_y_axis({'name': "gb"})

    chart_col.set_style(1)
    worksheet.insert_chart("D4", chart_col, {'x_offset': 25, 'y_offset': 10})
    workbook.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="iperf 数据转表格")
    parser.add_argument('--path', type=str, help='指定处理的文件路径')
    parser.add_argument('--sec', type=int, help='iperf 打流的时间间隔 默认为1')

    args = parser.parse_args()
    hello(args.path, args.sec)
