import sys

import pandas as pd
import argparse


def my_map(x):
    return x.strftime('%H:%M:%S')


def time_sq(rg_length):
    pd_date = pd.date_range("2021-1-1", periods=rg_length, freq='1s')
    pd_date = pd_date.map()
    return [i.strftime('%H:%M:%S') for i in pd_date]


def hello(file_name):
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
    pd_date = pd.date_range("2021-1-1", periods=list2_len, freq='1s')
    pd_date = pd_date.map(my_map)

    df = pd.DataFrame({'data': list2},
                      index=pd_date)
    # datetime.datetime.now().strftime('%F %H:%M:S')

    # 使用XlsxWriter作为引擎创建Excel编写器。
    writer = pd.ExcelWriter(file_name.split('.')[0] + '.xlsx', engine='xlsxwriter')

    # 将数据框转换为XlsxWriter Excel对象。
    df.to_excel(writer, sheet_name='Sheet1')

    # 获取xlsxwriter工作簿和工作表对象。
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象, 类型设置为折线图
    chart = workbook.add_chart({'type': 'scatter'})
    chart.set_size({'width': 1500,
                    'height': 500})
    # 设置图形的标题
    chart.set_title({'name': 'Data 点状图'})
    # 从dataframe数据配置图表，指定序列数据区域
    x = f'=Sheet1!$A$2:$A${len(list2)}'
    y = f'=Sheet1!$B$2:$B${len(list2)}'
    print(x)
    print(y)
    chart.add_series({
        'categories': x,  # x轴显示内容
        'values': y,
        'name': 'data',  # 图例名称
    })

    # 将图表插入工作表，指定图表的位置
    worksheet.insert_chart('D2', chart)

    # 关闭Excel writer并输出Excel文件
    writer.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="iperf 数据转表格")
    parser.add_argument('--path', help='指定处理的文件路径')

    args = parser.parse_args()
    hello('957412-p1.txt')
