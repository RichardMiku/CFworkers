import os
import re

# 获取当前目录
current_directory = os.getcwd()

# 获取当前目录下的所有CSV文件
csv_files = [f for f in os.listdir(current_directory) if f.endswith(".csv")]

# 提取文件名中的数字并按其排序
csv_files.sort(key=lambda x: int(re.search(r'AS(\d+)', x).group(1)))

# 打印排序后的CSV文件列表
for csv_file in csv_files:
    print(csv_file)
