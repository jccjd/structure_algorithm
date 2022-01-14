import xlsxwriter                     #导入模块
 
workbook = xlsxwriter.Workbook('new_excel.xlsx')   #创建新的excel
 
worksheet = workbook.add_worksheet('sheet1')        #创建新的sheet
 
headings = ['Number','testA','testB']             #创建表头
 
data = [
    ['2017-9-1','2017-9-2','2017-9-3','2017-9-4','2017-9-5','2017-9-6'],
    [10,40,50,20,10,50],
    [30,60,70,50,40,30],
]                                                       #自己造的数据
 
worksheet.write_row('A1',headings)
 
worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])                    #将数据插入到表格中
 
chart_col = workbook.add_chart({'type':'line'})        #新建图表格式 line为折线图
chart_col.add_series(                                   #给图表设置格式，填充内容
    {
        'name':'=sheet1!$B$1',
        'categories':'=sheet1!$A$2:$A$7',
        'values':   '=sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
        'data_labels': {'value': True} #显示数字，就是直方图上面的数字，默认不显示
    }
)
 
chart_col.set_title({'name':'测试'})
chart_col.set_x_axis({'name':"x轴"})
chart_col.set_y_axis({'name':'y轴'})          #设置图表表头及坐标轴
 
chart_col.set_style(1)
 
worksheet.insert_chart('A10',chart_col,{'x_offset':25,'y_offset':10})   #放置图表位置
 
workbook.close()
