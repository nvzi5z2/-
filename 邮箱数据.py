import pandas as pd

sk_pathf1='C:/Users/Administrator/Desktop/'
sk_pathf2='C:/Users/Administrator/Desktop/'
sk_pathf3='C:/Users/Administrator/Desktop/'
sk_pathf4='C:/Users/Administrator/Desktop/'
path1=r'C:\Users\Administrator\Desktop'

def set_basename():
    file_path = r'C:\Users\Administrator\Desktop\每日净值_ready.csv'
    data = pd.read_csv(file_path)
    #华睿稳健
    data['子基金名称'] = data['子基金名称'].replace('华睿稳健FOF一号', '华睿稳健FOF一号')
   # data['子基金名称'] = data['子基金名称'].replace('杉阳云杉量化1号私募证券投资基金', '杉阳云杉量化1号')
    #data['子基金名称'] = data['子基金名称'].replace('跃威权鑫一号私募证券投资基金A类', '跃威权鑫一号')
    #data['子基金名称'] = data['子基金名称'].replace('珺容无相纯债2号私募证券投资基金', '珺容无相纯债2号')
    #data['子基金名称'] = data['子基金名称'].replace('盛丰烁今1号私募证券投资基金', '盛丰烁今1号')
    #data['子基金名称'] = data['子基金名称'].replace('远澜银杏1号私募证券投资基金', '远澜银杏1号')
    #data['子基金名称'] = data['子基金名称'].replace('潼骁新资产私募证券投资基金', '潼骁新资产')
    #data['子基金名称'] = data['子基金名称'].replace('蒙玺科创50指数量化1号私募证券投资基金B', '蒙玺科创50指数量化1号')
    #data['子基金名称'] = data['子基金名称'].replace('殊馥兴义2号私募证券投资基金', '殊馥兴义2号')
    #data['子基金名称'] = data['子基金名称'].replace('致远量化对冲运作6号私募证券投资基金B类', '致远量化对冲运作6号')
    data['子基金名称'] = data['子基金名称'].replace('量派对冲9号私募证券投资基金A', '量派对冲9号')
    #data['子基金名称'] = data['子基金名称'].replace('鸣熙CTA2号私募证券投资基金', '鸣熙CTA2号')
    #data['子基金名称'] = data['子基金名称'].replace('吾执九二号私募证券投资基金B类', '吾执九二号')
    data['子基金名称'] = data['子基金名称'].replace('量派CTA七号私募证券投资基金A', '量派CTA7号')
    #data['子基金名称'] = data['子基金名称'].replace('宏翼高频1号私募证券投资基金', '宏翼高频1号')
    #data['子基金名称'] = data['子基金名称'].replace('鸣熙日耀套利1号私募证券投资基金', '鸣熙日耀套利1号')
    data['子基金名称'] = data['子基金名称'].replace('博润易量稳健1号私募证券投资基金', '博润易量稳健1号')
    data['子基金名称'] = data['子基金名称'].replace('交叉智能-量化增强2号私募证券投资基金', '交叉智能增强2号')
    #data['子基金名称'] = data['子基金名称'].replace('世纪前沿量化对冲62号a期私募证券投资基金B', '世纪前沿量化对冲62号a期私募证券投资基金B')
    #data['子基金名称'] = data['子基金名称'].replace('波粒二象东大楼私募证券投资基金', '波粒二象东大楼')
    #匠燃
    data['子基金名称'] = data['子基金名称'].replace('匠燃进取FOF', '匠燃进取FOF一号')
    #data['子基金名称'] = data['子基金名称'].replace('常瑜宇称2号私募证券投资基金', '常瑜宇称2号')
    #data['子基金名称'] = data['子基金名称'].replace('量派对冲9号私募证券投资基金A', '量派对冲9号')
    #data['子基金名称'] = data['子基金名称'].replace('殊馥兴义2号私募证券投资基金', '殊馥兴义2号')
    #data['子基金名称'] = data['子基金名称'].replace('汇艾资产稳健2号私募证券投资基金', '汇艾资产稳健2号')
    #data['子基金名称'] = data['子基金名称'].replace('潼骁新资产私募证券投资基金', '潼骁新资产')
    data['子基金名称'] = data['子基金名称'].replace('灵均恒君3号私募证券投资基金', '灵均恒君3号')
    data['子基金名称'] = data['子基金名称'].replace('浅湾-岳海精选六号股指CTA专享私募证券投资基金', '浅湾-岳海精选六号')
    #轩哥六号
    data['子基金名称'] = data['子基金名称'].replace('华凌轩哥六号', '轩哥六号')
    #data['子基金名称'] = data['子基金名称'].replace('跃威常鑫一号私募证券投资基金', '跃威常鑫一号')
    #data['子基金名称'] = data['子基金名称'].replace('潼骁周周享私募证券投资基金', '潼骁周周享')
    #data['子基金名称'] = data['子基金名称'].replace('致远量化对冲运作6号私募证券投资基金B类', '致远量化对冲运作6号')
    #data['子基金名称'] = data['子基金名称'].replace('优美利东海心选1号私募证券投资基金', '优美利东海心选1号')
    #data['子基金名称'] = data['子基金名称'].replace('汇艾资产稳健2号私募证券投资基金', '汇艾资产稳健2号')
    #data['子基金名称'] = data['子基金名称'].replace('吾执九二号私募证券投资基金B类', '吾执九二号')
    data['子基金名称'] = data['子基金名称'].replace('灵均恒君3号私募证券投资基金', '灵均恒君3号')
    data['子基金名称'] = data['子基金名称'].replace('世纪前沿量化对冲62号a期私募证券投资基金B', '世纪前沿量化对冲62号a期私募证券投资基金B')
    #琢玉
    data['子基金名称'] = data['子基金名称'].replace('华云琢玉FOF一号', '华云琢玉fof一号')
    #data['子基金名称'] = data['子基金名称'].replace('鸣熙致远二十号', '鸣熙致远二十号')
    data['子基金名称'] = data['子基金名称'].replace('潼骁新资产私募证券投资基金', '潼骁新资产')
    data['子基金名称'] = data['子基金名称'].replace('珺容无相纯债2号私募证券投资基金', '珺容无相纯债2号')
    #data['子基金名称'] = data['子基金名称'].replace('SVZ972-跃威常鑫一号私募证券投资基金', '跃威常鑫一号')
    #data['子基金名称'] = data['子基金名称'].replace('殊馥兴义2号私募证券投资基金', '殊馥兴义2号')
    #data['子基金名称'] = data['子基金名称'].replace('千衍九凌1号私募证券投资基金B类', '千衍九凌1号')
    data['子基金名称'] = data['子基金名称'].replace('量派CTA七号私募证券投资基金A', '量派CTA7号')
    data['子基金名称'] = data['子基金名称'].replace('量派对冲9号私募证券投资基金A', '量派对冲9号')
    data['子基金名称'] = data['子基金名称'].replace('常瑜宇称2号私募证券投资基金（A类份额）', '常瑜宇称2号')
    data['子基金名称'] = data['子基金名称'].replace('宏翼高频1号私募证券投资基金', '宏翼高频1号')
    data['子基金名称'] = data['子基金名称'].replace('统一提成', '东恺祖率中性一号')
    data.to_csv(file_path, index=False)

# 定义一个函数，用于找到子基金名称对应的子表格
def refine_matching_sheet(sub_fund_name, sheet_names):
    normalized_sub_fund_name = ''.join(filter(str.isalnum, sub_fund_name)).lower()
    for sheet in sheet_names:
        normalized_sheet = ''.join(filter(str.isalnum, sheet)).lower()
        if normalized_sub_fund_name in normalized_sheet:
            return sheet
    return None

#加载数据函数
def add_daily(temp,path):
    # 加载原始Excel文件
    excel_file_path = path + temp + '.xlsx' 
    excel_data = pd.read_excel(excel_file_path, sheet_name=None)

    # 获取所有子表格的名称
    sheet_names = excel_data.keys()
    # 加载CSV文件
    csv_file_path = r'C:\Users\Administrator\Desktop\每日净值_ready.csv'  
    daily_net_values = pd.read_csv(csv_file_path)

    # 初始化更新后的表格数据字典
    updated_sheets = {sheet: df.copy() for sheet, df in excel_data.items()}

    # 更新每个子表格的数据
    for index, row in daily_net_values.iterrows():
        matching_sheet = refine_matching_sheet(row['子基金名称'], sheet_names)
        if matching_sheet:
            sheet_df = updated_sheets[matching_sheet]
            date_row_index = sheet_df[sheet_df['日期'] == row['日期']].index
            if not date_row_index.empty:
                sheet_df.at[date_row_index[0], sheet_df.columns[1]] = row['累计净值']
            else:
                # 使用不同的方法添加新行
                new_row = pd.DataFrame({'日期': [row['日期']], sheet_df.columns[1]: [row['累计净值']]})
                sheet_df = pd.concat([sheet_df, new_row], ignore_index=True)
            updated_sheets[matching_sheet] = sheet_df

    # 将更新后的数据写回processExcel文件
    updated_excel_file_path = path + temp + '.xlsx'
    with pd.ExcelWriter(updated_excel_file_path) as writer:
        for sheet_name, df in updated_sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

#转换时间格式的函数
# 修改 convert_date_columns 函数，使用指定的日期格式 '%Y-%m-%d'
def convert_date_columns_with_format(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            # 先尝试直接转换为日期时间格式，不指定格式
            df[col] = pd.to_datetime(df[col], errors='coerce')

            # 如果转换成功且不全为空，则提取日期部分
            if not df[col].isnull().all():
                df[col] = df[col].dt.date
    return df

def check_datetype_deduplicate(temp,path):    
    # 加载Excel文件
    file_path = path + temp + '.xlsx'

    # 读取Excel文件中的所有子表格
    sheets = pd.read_excel(file_path, sheet_name=None)

    # 筛选出包含列名为"日期"的子表格，并转换日期列，然后去重
    converted_deduplicated_sheets = {}
    for sheet_name, sheet in sheets.items():
        if '日期' in sheet.columns:
            # 转换日期格式
            sheet['日期'] = pd.to_datetime(sheet['日期'], errors='coerce').dt.date
            # 去重，保留第一个出现的记录
            deduplicated_sheet = sheet.drop_duplicates(subset=['日期'], keep='last')
            converted_deduplicated_sheets[sheet_name] = deduplicated_sheet

    # 定义要保存的新文件路径
    output_file_path = path + temp + '.xlsx'

    # 将转换后且去重的每个子表格写入新的Excel文件
    with pd.ExcelWriter(output_file_path) as writer:
        for sheet_name, sheet in converted_deduplicated_sheets.items():
            sheet.to_excel(writer, sheet_name=sheet_name, index=False)

def fof1():
    add_daily('华睿稳健FOF一号净值',path1)
    check_datetype_deduplicate('华睿稳健FOF一号净值',path1)
def fof2():
    add_daily('匠燃进取FOF一号',path1)
    check_datetype_deduplicate('匠燃进取FOF一号',path1)
def fof3():
    add_daily('轩哥六号',path1)
    check_datetype_deduplicate('轩哥六号',path1)
def fof4():
    add_daily('华云琢玉fof一号',path1)
    check_datetype_deduplicate('华云琢玉fof一号',path1)

def skfof1():
    add_daily('华睿稳健FOF一号净值',sk_pathf1)
    check_datetype_deduplicate('华睿稳健FOF一号净值',sk_pathf1)
def skfof2():
    add_daily('匠燃进取FOF一号',sk_pathf2)
    check_datetype_deduplicate('匠燃进取FOF一号',sk_pathf2)
def skfof3():
    add_daily('轩哥六号',sk_pathf3)
    check_datetype_deduplicate('轩哥六号',sk_pathf3)
def skfof4():
    add_daily('华云琢玉fof一号',sk_pathf4)
    check_datetype_deduplicate('华云琢玉fof一号',sk_pathf4)

def run():
    fof1()
    fof2()
    fof3()
    fof4()  
def main():
    set_basename()
    run()

def f1():
    set_basename()
    fof1()
def f2():
    set_basename()
    fof2()
def f3():
    set_basename()
    fof3()
def f4():
    set_basename()  
    fof4()      

def skf1():
    set_basename()
    skfof1()
def skf2():
    set_basename()
    skfof2()
def skf3():
    set_basename()
    skfof3()
def skf4():
    set_basename()  
    skfof4()     

if __name__ == '__main__':
    main()