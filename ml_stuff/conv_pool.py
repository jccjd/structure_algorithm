import sys

import pandas as pd
import argparse


def hello(filename):
    # 构造数据
    df = pd.DataFrame({'data': [5, 10, 30, 50, 40, 30, 60]},
                      index=[11, 22, 42, 83, 94, 111, 333])

    print(df)

    # 使用XlsxWriter作为引擎创建Excel编写器。
    writer = pd.ExcelWriter('gairuo.com.xlsx', engine='xlsxwriter')

    # 将数据框转换为XlsxWriter Excel对象。
    df.to_excel(writer, sheet_name='Sheet1')

    # 获取xlsxwriter工作簿和工作表对象。
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象, 类型设置为折线图
    chart = workbook.add_chart({'type': 'line'})

    # 设置图形的标题
    chart.set_title({'name': 'Data 的折线图'})
    # 从dataframe数据配置图表，指定序列数据区域
    chart.add_series({
        'categories': '=Sheet1!$A$2:$A$8',  # x轴显示内容
        'values': '=Sheet1!$B$2:$B$8',
        'line': {'color': 'red'},  # 线条颜色
        'name': 'data',  # 图例名称
    })

    # 将图表插入工作表，指定图表的位置
    worksheet.insert_chart('D2', chart)

    # 关闭Excel writer并输出Excel文件
    writer.save()


if __name__ == '__main__':
    print(sys.argv[1])
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('--name', default='Great')

    args = parser.parse_args()

    print(args.name)
    hello(args.name)
