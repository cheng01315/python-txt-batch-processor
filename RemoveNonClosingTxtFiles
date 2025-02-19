import os

def delete_txt_files_without_ul(folder_path):
    """
    删除指定文件夹中不以</ul>结尾的.txt文件
    :param folder_path: 文件夹路径
    """
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"指定的路径 {folder_path} 不是一个有效的文件夹！")
        return

    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否为.txt
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # 打开文件并读取内容
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                # 检查文件内容是否以</ul>结尾
                if not content.strip().endswith("</ul>"):
                    # 删除文件
                    os.remove(file_path)
                    print(f"已删除文件：{file_path}")
            except Exception as e:
                print(f"处理文件 {file_path} 时发生错误：{e}")

    print("处理完成！")

# 示例用法
if __name__ == "__main__":
    folder_path = input("请输入文件夹路径：")
    delete_txt_files_without_ul(folder_path)
