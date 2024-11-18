import os
import email
from imapclient import IMAPClient
from email.header import decode_header

# 邮件配置
username = 'hwqhzg@hwqh.com.cn'
password = 'Hwqh.135790'
host = 'imaphz.qiye.163.com'
# 输出目标文件夹
output_target_folder = r'D:\1.工作文件\5.基金绩效分析\6.全部估值表提取\估值表A'

#清理原有文件
def clear_directory_files(path):
    # 遍历指定路径下的所有文件
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        # 判断是否为文件
        if os.path.isfile(file_path):
            # 删除文件
            os.remove(file_path)

# 调用函数清除目录下的所有文件
clear_directory_files(output_target_folder)

# 要下载附件的文件夹列表
folders = ['INBOX/估值表/华睿稳健FOF一号', 'INBOX/估值表/华云琢玉FOF一号','INBOX/估值表/匠燃进取一号FOF','INBOX/估值表/华睿稳盛FOF一号','INBOX/估值表/华晟FOF一号','INBOX/估值表/华晟FOF二号','INBOX/估值表/华晟FOF五号','INBOX/估值表/华晟FOF七号','INBOX/估值表/华晟FOF十号','INBOX/估值表/华晟三号','INBOX/估值表/华睿平衡FOF一号','INBOX/估值表/华晟混合一号']

def clean_filename(filename):
    """清理文件名中的非法字符"""
    decoded_header = decode_header(filename)
    decoded_filename = ''
    for part, encoding in decoded_header:
        if isinstance(part, bytes):
            decoded_filename += part.decode(encoding or 'utf-8')
        else:
            decoded_filename += part

    cleaned_filename = ''.join(c for c in decoded_filename if c.isalnum() or c in (' ', '.', '_', '-')).strip()
    return cleaned_filename

try:
    # 连接到 IMAP 服务器
    with IMAPClient(host) as client:
        # 登录到邮件账户
        client.login(username, password)

        for folder_name in folders:
            # 选择指定的文件夹
            client.select_folder(folder_name)

            # 搜索所有邮件
            email_list = client.search(['ALL'])
            if not email_list:
                print(f"在文件夹 {folder_name} 中没有找到任何邮件")
            else:
                # 获取最新一封邮件的内容
                latest_email_id = email_list[-1]
                response = client.fetch([latest_email_id], ['RFC822'])
                email_data = response[latest_email_id]
                email_message = email.message_from_bytes(email_data[b'RFC822'])

                # 检查邮件是否包含附件
                if email_message.get_content_maintype() == 'multipart':
                    attachment_found = False
                    # 处理附件
                    for part in email_message.walk():
                        # 只处理附件部分
                        content_disposition = part.get("Content-Disposition", None)
                        if content_disposition and content_disposition.startswith('attachment'):
                            filename = part.get_filename()
                            if filename:
                                # 清理文件名
                                cleaned_filename = clean_filename(filename)
                                attachment_found = True
                                # 构建输出文件路径
                                output_file_path = os.path.join(output_target_folder, cleaned_filename)

                                # 确保输出文件夹存在
                                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                                # 将附件下载到输出文件路径
                                with open(output_file_path, 'wb') as file:
                                    file.write(part.get_payload(decode=True))

                                print(f"附件 {cleaned_filename} 已成功下载到 {output_file_path}")

                    if not attachment_found:
                        print(f"在邮件 {latest_email_id} 中没有找到任何附件")
                else:
                    print(f"邮件 {latest_email_id} 不包含附件")

except Exception as e:
    print(f"出现错误: {e}")