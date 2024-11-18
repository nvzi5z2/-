from imapclient import IMAPClient
import email
from email.header import decode_header
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# 配置您的登录信息
USERNAME = 'shaokai@hwqh.com.cn'
PASSWORD  = 'HUAwen2024'
HOST  = 'imaphz.qiye.163.com'  # 替换为您电子邮件提供商的IMAP服务器地址
first = 'first'
second = 'second'
#邮箱路径
def Decide_path(name,title,level):
    # 定义一个字典来映射 'title' 变量的值到相应的路径前缀
    path_prefixes = {
        '华睿稳健FOF一号': 'INBOX/华睿稳健FOF一号/',
        '华云琢玉FOF一号': 'INBOX/华云琢玉FOF一号/',
        '匠燃进取FOF': 'INBOX/匠燃进取FOF/',
        '华凌轩哥六号': 'INBOX/华凌轩哥六号/'
    }

    # 构建 'name' 变量
    if level == 'first':
        path = 'INBOX/' + title
    elif level == 'second':
        if title in path_prefixes:
            path = path_prefixes[title] + name
            #if name == '常瑜宇称2号私募证券投资基金':
                #path = path+'/估值表'
    return name,path,title
#提前设置位置具体点位
def xy_get(name,path,title,past):
    # 定义一个映射，用于将 names 映射到对应的 x, y, name 值
    
    if title == '华睿稳健FOF一号':
        map = {
            '华睿稳健FOF一号': (0, -1-past),
            #'珺容无相纯债2号私募证券投资基金': (1, -1-past),
            #'潼骁新资产私募证券投资基金': (2, -1-past),
            '量派对冲9号私募证券投资基金A': (3, -1-past),
            #'鸣熙CTA2号私募证券投资基金': (3, -1-past),
            '宏翼高频1号私募证券投资基金': (3, -1-past),
            '量派CTA七号私募证券投资基金A': (3, -1-past),
            #'鸣熙日耀套利1号私募证券投资基金': (3, -1-past),
            '博润易量稳健1号私募证券投资基金': (4, -1-past),
            #'世纪前沿量化对冲62号a期私募证券投资基金B': (3, -1-past)
        }

    elif title == '华凌轩哥六号':
        map = {
        '华凌轩哥六号': (0, -1-past),
        '潼骁周周享私募证券投资基金': (4, -1-past),
        '图斯和贞私募证券投资基金': (4, -1-past),
        '致远量化对冲运作6号私募证券投资基金B类': (1, 0-past),
        '跃威常鑫一号私募证券投资基金':(0,0-past),
        '优美利东海心选1号私募证券投资基金':(3, -1-past),
        '汇艾资产稳健2号私募证券投资基金':(3, -1-past),
        '吾执九二号私募证券投资基金B类': (3, -1-past),
        '灵均恒君3号私募证券投资基金': (2, -1-past)
    }
    elif title == '匠燃进取FOF':
        map = {
        '匠燃进取FOF': (0, -1-past),
        '常瑜宇称2号私募证券投资基金': (1, -1-past),
        '汇艾资产稳健2号私募证券投资基金':(3, -1-past),
        '量派对冲9号私募证券投资基金A': (3, -1-past),
        '殊馥兴义2号私募证券投资基金': (3, -1-past),
        '潼骁新资产私募证券投资基金': (2, -1-past),
        '灵均恒君3号私募证券投资基金': (2, -1-past),
        '浅湾-岳海精选六号股指CTA专享私募证券投资基金': (2, -1-past)
    }
    elif title == '华云琢玉FOF一号':
        map = {
        '华云琢玉FOF一号': (1, -1-past),
        '潼骁新资产私募证券投资基金': (2, -1-past),
        '珺容无相纯债2号私募证券投资基金': (1, -1-past),
        '殊馥兴义2号私募证券投资基金': (3, -1-past),
        '千衍九凌1号私募证券投资基金B类':(1,-1-past),
        '量派CTA七号私募证券投资基金A':(3,-1-past),
        '量派对冲9号私募证券投资基金A': (3, -1-past),
        '常瑜宇称2号私募证券投资基金': (3, -1-past),
        '宏翼高频1号私募证券投资基金': (3, -1-past)
    }

    x,y=map.get(name,(None,None))
    return name , x,y,path


def get_ht(names,x,y,path):
    if names == '致远量化对冲运作6号私募证券投资基金B类' or names == '跃威常鑫一号私募证券投资基金'or names == '常瑜宇称2号私募证券投资基金':
        return
    else:
        with IMAPClient(HOST) as client:
            # 登录到IMAP服务器
            client.login(USERNAME, PASSWORD)
            # 选择邮箱文件夹，例如 "INBOX"
            client.select_folder(path, readonly=True)

            # 搜索邮件，这里选取所有邮件
            messages = client.search(['NOT', 'DELETED'])

            # 如果文件夹不为空，处理最新的邮件
            if messages:
                latest_email_id = messages[y-1]
                # 注意：fetch 方法期望的是一个邮件 ID 的列表
                response = client.fetch([latest_email_id], ['BODY[]'])

                # 从响应中获取邮件正文
                # response 是一个字典，邮件 ID 是键，对应的值是另一个字典
                email_body = response[latest_email_id].get(b'BODY[]')
                if email_body is not None:
                    email_message = email.message_from_bytes(email_body)
                else:
                    # Handle the case where email_body is None by raising an exception
                    return
                email_message = email.message_from_bytes(email_body)

                if email_message.is_multipart():
                    for part in email_message.walk():
                        if part.get_content_type() == 'text/html':
                            # 尝试解码 HTML 内容
                            try:
                                html_content = part.get_payload(decode=True).decode(part.get_content_charset())
                            except (UnicodeDecodeError, AttributeError):
                                # 如果解码失败，尝试使用默认的 'latin1' 编码
                                html_content = part.get_payload(decode=True).decode('latin1', 'ignore')
                            #print(html_content)
                            break
                else:
                    try:
                        html_content = email_message.get_payload(decode=True).decode(email_message.get_content_charset())
                    except (UnicodeDecodeError, AttributeError):
                        html_content = email_message.get_payload(decode=True).decode('latin1', 'ignore')
                    #print(html_content)
        if names == '致远量化对冲运作6号私募证券投资基金B类' or names == '跃威常鑫一号私募证券投资基金'or names == '常瑜宇称2号私募证券投资基金':
            return
        else:
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # 初始化一个空列表来存储浮点数
            float_numbers = []

            td_tags = soup.select('td')

            float_pattern = re.compile(r'\d\.\d+')
            
            for td in td_tags:
                match = float_pattern.search(td.text)
                if match:
                    # 找到浮点数，将其添加到列表
                    float_numbers.append(match.group())
                    #print(f"Found value: {match.group()}")
                #else:
                    #print("No floating-point number found in the specified <td> tag.")

            # 使用浮点数列表创建 DataFrame
            df_num = pd.DataFrame(float_numbers, columns=['累计净值'])
            k=df_num['累计净值'][x]
            return k

#获取所需数据
def get_html(names,x,y,path,past):
    last_num = get_ht(names=names,x=x,y=y,path=path)
    if names == '致远量化对冲运作6号私募证券投资基金B类' or names == '跃威常鑫一号私募证券投资基金'or names == '常瑜宇称2号私募证券投资基金':
        read_download_file(path,past)
    else:
        with IMAPClient(HOST) as client:
            # 登录到IMAP服务器
            client.login(USERNAME, PASSWORD)
            # 选择邮箱文件夹，例如 "INBOX"
            client.select_folder(path, readonly=True)

            # 搜索邮件，这里选取所有邮件
            messages = client.search(['NOT', 'DELETED'])

            # 如果文件夹不为空，处理最新的邮件
            if messages:
                latest_email_id = messages[y]
                # 注意：fetch 方法期望的是一个邮件 ID 的列表
                response = client.fetch([latest_email_id], ['BODY[]'])

                # 从响应中获取邮件正文
                # response 是一个字典，邮件 ID 是键，对应的值是另一个字典
                email_body = response[latest_email_id].get(b'BODY[]')
                if email_body is not None:
                    email_message = email.message_from_bytes(email_body)
                else:
                    # Handle the case where email_body is None by raising an exception
                    return
                email_message = email.message_from_bytes(email_body)

                if email_message.is_multipart():
                    for part in email_message.walk():
                        if part.get_content_type() == 'text/html':
                            # 尝试解码 HTML 内容
                            try:
                                html_content = part.get_payload(decode=True).decode(part.get_content_charset())
                            except (UnicodeDecodeError, AttributeError):
                                # 如果解码失败，尝试使用默认的 'latin1' 编码
                                html_content = part.get_payload(decode=True).decode('latin1', 'ignore')
                            #print(html_content)
                            break
                else:
                    try:
                        html_content = email_message.get_payload(decode=True).decode(email_message.get_content_charset())
                    except (UnicodeDecodeError, AttributeError):
                        html_content = email_message.get_payload(decode=True).decode('latin1', 'ignore')
                    #print(html_content)
        
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 初始化一个空列表来存储浮点数
        float_numbers = []

        td_tags = soup.select('td')

        float_pattern = re.compile(r'\d\.\d+')
        
        for td in td_tags:
            match = float_pattern.search(td.text)
            if match:
                # 找到浮点数，将其添加到列表
                float_numbers.append(match.group())
                #print(f"Found value: {match.group()}")
            #else:
                #print("No floating-point number found in the specified <td> tag.")

        # 使用浮点数列表创建 DataFrame
        df_num = pd.DataFrame(float_numbers, columns=['累计净值'])
        if float(last_num) - float(df_num['累计净值'][x]) > 0.2:
            x=x-1
        # 现在 df 包含了所有找到的浮点数

        # 初始化一个变量来存储第一个找到的日期
        first_date = None

        td_tags = soup.select('td')

        # 编译一个正则表达式来匹配YYYY-MM-DD格式的日期
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        
        for td in td_tags:
            if first_date is None:  # 只有当我们还没有找到日期时才继续搜索
                match = date_pattern.search(td.text)
                if match:
                    # 找到第一个日期，存储它并停止搜索
                    first_date = match.group()
                    break  # 找到第一个匹配项后退出循环

        # 如果找到了日期，创建一个只包含这个日期的DataFrame
        if first_date:
            df = pd.DataFrame([first_date], columns=['日期'])
            try:
                print('子基金:'+names+'日期是：'+df['日期'][0]+'累计净值是：'+df_num['累计净值'][x])
                # Assign the data to the DataFrame
                df['子基金名称'] = [names] 
                df['累计净值'] = [df_num['累计净值'][x]] 
                df['日期']=pd.to_datetime(df['日期'])
            except KeyError:
                print('子基金:'+names+'日期是：'+df['日期'][0]+'累计净值是：'+df_num['累计净值'][x-1])
                # Assign the data to the DataFrame
                df['子基金名称'] = [names]  
                df['累计净值'] = [df_num['累计净值'][x-1]]  
                df['日期']=pd.to_datetime(df['日期'])
            # Define the CSV file path
            csv_file_path = r'C:\Users\Administrator\Desktop\每日净值.csv'
    # Write the DataFrame to a CSV file, ap/每日净值.csv'
            # Write the DataFrame to a CSV file, appending if it already exists
            if not os.path.isfile(csv_file_path):
                df.to_csv(csv_file_path, mode='a', index=False, header=True)
            else:
                df.to_csv(csv_file_path, mode='a', index=False, header=False)
        else:
            if names=='蒙玺科创50指数量化1号私募证券投资基金B':
                date_pattern = re.compile(r'\d{8}')
                match_count = 0  # 初始化一个计数器

                for td in td_tags:
                    match = date_pattern.search(td.text)
                    if match:
                        match_count += 1  # 每找到一个匹配项，计数器增加1
                        if match_count == 2:
                            # 找到第二个日期，存储它并停止搜索
                            first_date = match.group()
                            break  # 找到第二个匹配项后退出循环
            else:
                # 编译一个正则表达式来匹配8位数字的日期格式
                date_pattern = re.compile(r'\d{8}')

                for td in td_tags:
                    match = date_pattern.search(td.text)
                    if match:
                            # 找到第一个日期，存储它并停止搜索
                            first_date = match.group()
                            break  # 找到第一个匹配项后退出循环

            # 如果找到了日期，创建一个只包含这个日期的DataFrame
            if first_date:
                df = pd.DataFrame([first_date], columns=['日期'])
                try:
                    print('子基金:'+names+'日期是：'+df['日期'][0]+'累计净值是：'+df_num['累计净值'][x])
                    # Assign the data to the DataFrame
                    df['子基金名称'] = [names]  # Make sure 'names' is a list or wrapped in a list if it's a single value
                    df['累计净值'] = [df_num['累计净值'][x]]  # Wrap the value in a list to ensure it is compatible with DataFrame assignment
                    df['日期']=pd.to_datetime(df['日期'])
                except KeyError:
                    print('子基金:'+names+'日期是：'+df['日期'][0]+'累计净值是：'+df_num['累计净值'][x-1])
                    # Assign the data to the DataFrame
                    df['子基金名称'] = [names]  # Make sure 'names' is a list or wrapped in a list if it's a single value
                    df['累计净值'] = [df_num['累计净值'][x-1]]  # Wrap the value in a list to ensure it is compatible with DataFrame assignment
                    df['日期']=pd.to_datetime(df['日期'])
                # Define the CSV file path
                csv_file_path = r'C:\Users\Administrator\Desktop\每日净值.csv'
    # Write the DataFrame to a CSV file, ap/每日净值.csv'

                # Write the DataFrame to a CSV file, appending if it already exists
                if not os.path.isfile(csv_file_path):
                    df.to_csv(csv_file_path, mode='a', index=False, header=True)
                else:
                    df.to_csv(csv_file_path, mode='a', index=False, header=False)
#整合以上三个步骤
def combine(a,b,c,past):
    name, path, title = Decide_path(a, b, c)
    names, x, y, path = xy_get(name, path, title,past)
    get_html(names, x, y, path,past)
#三个fof的各个子基金跑一遍
def fof1_p(past):
    combine('华睿稳健FOF一号','华睿稳健FOF一号',first,past)
    #combine('杉阳云杉量化1号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('跃威权鑫一号私募证券投资基金A类','华睿稳健FOF一号',second,past)
    #combine('珺容无相纯债2号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('盛丰烁今1号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('鸣熙致远二十号私募证券投资基金','华睿稳健FOF一号',second)
    #combine('远澜银杏1号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('潼骁新资产私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('蒙玺科创50指数量化1号私募证券投资基金B','华睿稳健FOF一号',second,past)
    #combine('殊馥兴义2号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('致远量化对冲运作6号私募证券投资基金B类','华睿稳健FOF一号',second,past)
    combine('量派对冲9号私募证券投资基金A','华睿稳健FOF一号',second,past)
    #combine('鸣熙CTA2号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('吾执九二号私募证券投资基金B类','华睿稳健FOF一号',second,past)
    combine('量派CTA七号私募证券投资基金A','华睿稳健FOF一号',second,past)
    #combine('宏翼高频1号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('鸣熙日耀套利1号私募证券投资基金','华睿稳健FOF一号',second,past)
    combine('博润易量稳健1号私募证券投资基金','华睿稳健FOF一号',second,past)
    #combine('世纪前沿量化对冲62号a期私募证券投资基金B','华睿稳健FOF一号',second,past)
def fof2_p(past):
    combine('匠燃进取FOF','匠燃进取FOF',first,past)
    #combine('常瑜宇称2号私募证券投资基金','匠燃进取FOF',second,past)
    #combine('汇艾资产稳健2号私募证券投资基金','匠燃进取FOF',second,past)
    #combine('量派对冲9号私募证券投资基金A','匠燃进取FOF',second,past)
    #combine('殊馥兴义2号私募证券投资基金','匠燃进取FOF',second,past)
    #combine('潼骁新资产私募证券投资基金','匠燃进取FOF',second,past)
    combine('灵均恒君3号私募证券投资基金','匠燃进取FOF',second,past)
    combine('浅湾-岳海精选六号股指CTA专享私募证券投资基金','匠燃进取FOF',second,past)
def fof3_p(past):
    combine('华凌轩哥六号','华凌轩哥六号',first,past)
    #combine('图斯和贞私募证券投资基金','华凌轩哥六号',second)
    #combine('潼骁周周享私募证券投资基金','华凌轩哥六号',second,past)
    #combine('致远量化对冲运作6号私募证券投资基金B类','华凌轩哥六号',second,past)
    #combine('跃威常鑫一号私募证券投资基金','华凌轩哥六号',second,past)
    #combine('优美利东海心选1号私募证券投资基金','华凌轩哥六号',second,past)
    #combine('汇艾资产稳健2号私募证券投资基金','华凌轩哥六号',second,past)
    #combine('吾执九二号私募证券投资基金B类','华凌轩哥六号',second,past)
    combine('灵均恒君3号私募证券投资基金','华凌轩哥六号',second,past)
def fof4_p(past):
    combine('华云琢玉FOF一号','华云琢玉FOF一号',first,past)
    #combine('潼骁新资产私募证券投资基金','华云琢玉FOF一号',second,past)
    combine('珺容无相纯债2号私募证券投资基金','华云琢玉FOF一号',second,past)
    combine('千衍九凌1号私募证券投资基金B类','华云琢玉FOF一号',second,past)
    combine('量派CTA七号私募证券投资基金A','华云琢玉FOF一号',second,past)
    combine('量派对冲9号私募证券投资基金A','华云琢玉FOF一号',second,past)
    combine('常瑜宇称2号私募证券投资基金','华云琢玉FOF一号',second,past)
    combine('宏翼高频1号私募证券投资基金','华云琢玉FOF一号',second,past)
#网络文字解码
def decode_mime_words(s):
    return ''.join(word.decode(encoding or 'utf-8') if isinstance(word, bytes) else word
                   for word, encoding in decode_header(s))
#下载附件
def download_file(path,past):  
    with IMAPClient(HOST) as client:
        # 登录到IMAP服务器
        client.login(USERNAME, PASSWORD)
        
        # 选择邮箱文件夹，例如 "INBOX"
        client.select_folder(path, readonly=True)

        # 搜索邮件，这里选取所有邮件
        messages = client.search(['NOT', 'DELETED'])

        # 如果文件夹不为空，处理最新的邮件
        if messages:
            latest_email_id = messages[-1-past]
            response = client.fetch([latest_email_id], ['BODY.PEEK[]'])

            messages = client.search(['NOT', 'DELETED'])
        if messages:
            latest_email_id = messages[-1-past]
            response = client.fetch([latest_email_id], ['BODY[]', 'FLAGS'])

            message = email.message_from_bytes(response[latest_email_id][b'BODY[]'])
            for part in message.walk():
                if part.get_content_maintype() == 'application':
                    filename = part.get_filename()
                    if filename:
                        decoded_filename = decode_mime_words(filename)
                        filepath = os.path.join('C:/Users/Administrator/Desktop/','temp.xls')
    # Write the DataFrame to a CSV file, ap/", 'temp.xls')
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        #print(f"附件 {decoded_filename} 已下载到 {filepath}")
#找到各个附件的数据位置并爬取储存
def read_download_file(path,past):
    if path == 'INBOX/华凌轩哥六号/致远量化对冲运作6号私募证券投资基金B类':
        x = 1
        y = 7
        z = 2
        s = 1
    if path == 'INBOX/华睿稳健FOF一号/致远量化对冲运作6号私募证券投资基金B类':
        x = 1
        y = 7
        z = 2
        s = 1
    elif path == 'INBOX/华凌轩哥六号/跃威常鑫一号私募证券投资基金':
        x = 0
        y = 5
        z = 3
        s = 0
    elif path == 'INBOX/华云琢玉FOF一号/跃威常鑫一号私募证券投资基金':
        x = 0
        y = 5
        z = 3
        s = 0
    elif path == 'INBOX/华云琢玉FOF一号/常瑜宇称2号私募证券投资基金':
        x = 1
        y = 7
        z = 6
        s = 0
    download_file(path,past)
    df=pd.read_excel(r'C:\Users\Administrator\Desktop\temp.xls')

    data = {
        '日期':(),
        '子基金名称':(),
        '累计净值':() 
    }
    df1=pd.DataFrame(data)
    df1['子基金名称'] = [df.iloc[s,x]]
    df1['日期'] = pd.to_datetime(df.iloc[s,z],format='%Y%m%d') 
    df1['累计净值'] = [df.iloc[s,y]]

    sub_fund_name = str(df.iloc[s, x])
    date_str = pd.to_datetime(df.iloc[s, z], format='%Y%m%d').strftime('%Y-%m-%d')
    net_value = str(df.iloc[s, y])
    print('子基金:' + sub_fund_name + ' 日期是：' + date_str + ' 累计净值是：' + net_value)


    # Define the CSV file path
    csv_file_path = r'C:\Users\Administrator\Desktop\每日净值.csv'
    # Write the DataFrame to a CSV file, appending if it already exists
    if not os.path.isfile(csv_file_path):
        df1.to_csv(csv_file_path, mode='a', index=False, header=True)
    else:
        df1.to_csv(csv_file_path, mode='a', index=False, header=False)
    os.remove(r'C:\Users\Administrator\Desktop\temp.xls')
#综合代码 跑所有观察的基金
def run_code(past):
    fof1_p(past)
    fof2_p(past)
    fof3_p(past)
    fof4_p(past)
#检查爬取数据情况
def get_previous_workday(date):
    """
    获取给定日期的上一个工作日。
    如果给定日期是周一，则上一个工作日为上周五；
    如果给定日期是周末，则上一个工作日为上周五。
    """
    # 转换为日期对象
    date_obj = pd.to_datetime(date)
    # 先减去一天开始检查
    previous = date_obj - pd.Timedelta(days=1)
    
    # 如果是周一，减去三天得到上周五
    if date_obj.weekday() == 0:
        previous = date_obj - pd.Timedelta(days=3)
    # 如果是周日，减去两天得到上周五
    elif date_obj.weekday() == 6:
        previous = date_obj - pd.Timedelta(days=2)
    # 如果是周六，减去一天得到上周五
    elif date_obj.weekday() == 5:
        previous = date_obj - pd.Timedelta(days=1)
    return previous
#查看那些没更新净值的基金
def identify_mismatched_funds(reference_date):
    """
    确定'日期'不是给定'参考日期'前一个工作日的基金。
    
    :param funds_df: 包含基金数据的DataFrame
    :param reference_date: 用于比较前一个工作日的参考日期
    :return: 不匹配基金的DataFrame
    """
    funds_df = pd.read_csv(r'C:\Users\Administrator\Desktop\每日净值_ready.csv')
    # 将参考日期转换为datetime
    reference_date = pd.to_datetime(reference_date)
    # 计算参考日期前的最后一个工作日
    last_working_day = get_previous_workday(reference_date)
    # 筛选出日期不等于最后一个工作日的基金
    mismatched_funds = funds_df[pd.to_datetime(funds_df['日期']) != last_working_day]
    
    return mismatched_funds[['日期', '子基金名称']]
#综合
#去重
def fixdata():
    # 加载CSV文件
    file_path = r'C:\Users\Administrator\Desktop\每日净值.csv'
    data = pd.read_csv(file_path)
    df_deduplicated = data.drop_duplicates(subset=['日期', '子基金名称','累计净值'], keep='first')

    # 指定输出文件的路径
    output_file_path = r'C:\Users\Administrator\Desktop\每日净值_ready.csv'  # 替换为您想要保存CSV文件的具体路径和文件名

    # 将去重后的DataFrame保存为CSV文件，不保存行索引
    df_deduplicated.to_csv(output_file_path, index=False)
def date_check():
    fixdata()
    reference_date = datetime.now().strftime('%Y-%m-%d')
    print('今天的时间为:'+ reference_date)
    # 确定不匹配的基金
    mismatched_funds_df = identify_mismatched_funds(reference_date)
    if mismatched_funds_df.empty == False:
        # 显示不匹配的基金
        print('以下子基金还没有出来净值数据')
        print(mismatched_funds_df)
    else:
        print('今日基金净值数据均出')

def main():
    run_code()
    date_check()

def f1(past):
    fof1_p(past)
    date_check()

def f2(past):
    fof2_p(past)
    date_check()

def f3(past):
    fof3_p(past)
    date_check()

def f4(past):
    fof4_p(past)
    date_check()



