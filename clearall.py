import os

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 检查文件是否为CSV文件
    if filename.endswith(".csv"):
        # 构建文件路径
        file_path = os.path.join(current_directory, filename)
        # 打开文件并清空其内容
        with open(file_path, 'w') as file:
            file.truncate(0)