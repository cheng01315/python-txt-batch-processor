import os
import re

def remove_first_p_tag(file_path):
    """
    从指定文件中删除第一段<p></p>标签内的内容
    """
    try:
        # 打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式查找并删除第一段<p></p>标签内的内容
        # 注意：正则表达式假设<p>和</p>之间没有嵌套标签
        content = re.sub(r'<p>.*?</p>', '', content, count=1)

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_files_in_directory(directory):
    """
    遍历指定目录中的所有文本文件并处理
    """
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # 假设文件扩展名为.txt，根据实际情况修改
            file_path = os.path.join(directory, filename)
            remove_first_p_tag(file_path)

# 示例：指定要处理的文件夹路径
directory_path = 'path/to/your/text/files'
process_files_in_directory(directory_path)
