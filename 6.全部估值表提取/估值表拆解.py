import os
import glob
import pandas as pd
import re

#国君+广发估值表处理

folder_path_A = r'C:\Users\Administrator\Desktop\每日抓取py\6.全部估值表提取\估值表A'
search_keywords = ['琢玉','华晟FOF一号','华晟FOF二号','华晟FOF五号','华晟FOF七号','华晟FOF十号','华晟混合一号','华睿平衡']

# 搜索符合条件的Excel文件
matching_files = []
for keyword in search_keywords:
    pattern_xls = os.path.join(folder_path_A, f'*{keyword}*.xls')
    matching_files.extend(glob.glob(pattern_xls))
    
    pattern_xlsx = os.path.join(folder_path_A, f'*{keyword}*.xlsx')
    matching_files.extend(glob.glob(pattern_xlsx))

# 遍历匹配的Excel文件
for file_path in matching_files:
    # 读取Excel文件到DataFrame，并跳过第一行
    df = pd.read_excel(file_path, skiprows=1)
    
    # 在第五列和第七列之前插入空值的列
    df.insert(4, '新列1', '')
    df.insert(4, '新列2', '')
    df.insert(4, '新列3', '')
    df.insert(10, '新列4', '')
    df.insert(13, '新列5', '')
    
    # 获取原文件名
    file_name = os.path.basename(file_path)
    
    # 定义一个函数来提取数字并乘以0.01
    def multiply_numbers_by_001(cell):
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", str(cell))  # 使用正则表达式提取数字部分
        if numbers:  # 如果找到数字
            return float(numbers[0]) * 0.01  # 将找到的第一个数字乘以0.01
        else:
            return cell  # 如果没有找到数字，返回原始值

    # 对第八列应用函数
    df.iloc[:, 8] = df.iloc[:, 8].apply(multiply_numbers_by_001)
    df.iloc[:, 12] = df.iloc[:, 12].apply(multiply_numbers_by_001)
    
    # 构建新文件路径
    new_file_path_A = os.path.join(folder_path_A, file_name)
    
    # 保存DataFrame为新的Excel文件（以xlsx格式）
    df.to_excel(new_file_path_A, index=False, engine='openpyxl')
    
    print(f'已保存文件：{new_file_path_A}')


#中信叠加处理好的国君

folder_path = r'C:\Users\Administrator\Desktop\每日抓取py\6.全部估值表提取\估值表A'

# 创建一个空的DataFrame用于存储提取的内容
result_dfs = []

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历文件夹中的文件
for file in files:
    if file.endswith('.xlsx') or file.endswith('.xls'):
        file_path = os.path.join(folder_path, file)
        
        # 读取Excel文件为DataFrame
        sheets = pd.read_excel(file_path, sheet_name=None, header=None)
        
        # 遍历每个Sheet
        for sheet_name, df in sheets.items():
            # 处理缺失值，用空字符串填充
            df = df.fillna('')
            
            # 获取包含'正常交易'或'虚拟行情'字样的行
            keyword_rows = df[df.apply(lambda row: '正常交易' in ''.join(str(cell) for cell in row) or '虚拟行情' in ''.join(str(cell) for cell in row) or '手工行情' in ''.join(str(cell) for cell in row), axis=1)]
            
            # 筛选特定行
            filtered_df = df[(df.index.isin([0])) |
                             (df.index.isin(keyword_rows.index)) |
                             (df[0].str.contains('1002.01.01')) |
                             #(df[0].str.contains('100201')) |
                             (df[0].isin(['100201','今日可用头寸', '资产净值','基金资产净值:']))]


            # 将符合条件的DataFrame添加到结果DataFrame列表中
            if not filtered_df.empty:
                result_dfs.append(filtered_df)
                
                # 插入两行空白行
                result_dfs.append(pd.DataFrame(index=[0, 0]))         

# 合并结果DataFrame列表为一个DataFrame
result_df = pd.concat(result_dfs, ignore_index=True)

# 删除第三、四和五列
result_df_ONE = result_df.drop(columns=[2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 15, 16])


# 修改第二列和第三列的名称
result_df_ONE = result_df_ONE.rename(columns={1: '名称', 7: '成本', 11: '市值', 14: '估值增值'})
result_df_ONE.to_excel(r'C:\Users\Administrator\Desktop\每日抓取py\6.全部估值表提取\提取结果.xlsx', index=False)

#提取占比情况
result_df_TWO = result_df.drop(columns=[2, 3, 4, 5, 6,7, 8, 9, 10, 13, 14, 15, 16])
result_df_TWO = result_df_TWO.rename(columns={1: '名称', 11: '市值', 12: '占比'})
# 定义需要删除的文字列表
words_to_delete = ["今日可用头寸"]

# 根据条件过滤并删除行
df_filtered = result_df_TWO[~result_df_TWO.astype(str).apply(lambda row: row.str.contains('|'.join(words_to_delete))).any(axis=1)]
#df_filtered = pd.DataFrame(df_filtered)
# 格式化第3列的数字为千位分隔符形式
#df_filtered.iloc[:, 2] = df_filtered.iloc[:, 2].apply(lambda x: '{:,.0f}'.format(x) if pd.notnull(x) and isinstance(x, (int, float)) else x)
# 将第4列的数字转换为百分比形式
#df_filtered.iloc[:, 3] = df_filtered.iloc[:, 3].apply(lambda x: '{:.2%}'.format(x) if pd.notnull(x) and isinstance(x, (float)) else x)
df_filtered.to_excel(r'D:\1.工作文件\5.基金绩效分析\6.全部估值表提取\每日市值及占比情况.xlsx', index=False)

