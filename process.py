import os
import re
import pandas as pd

# 获取当前目录
current_directory = os.getcwd()

# 获取当前目录下的所有CSV文件
csv_files = [f for f in os.listdir(current_directory) if f.endswith(".csv")]

# 提取文件名中的数字并按其排序
csv_files.sort(key=lambda x: int(re.search(r'AS(\d+)', x).group(1)) if re.search(r'AS(\d+)', x) else float('inf'))

# 读取 ip.csv 文件
file_path = 'ip.csv'
df = pd.read_csv(file_path)

# 更新 '数据中心' 列的值
df['数据中心'] = df.apply(lambda row: f"{row['数据中心']}-{row['下载速度']}", axis=1)

# 查找第一个空的CSV文件
for csv_file in csv_files:
    csv_file_path = os.path.join(current_directory, csv_file)
    if os.path.getsize(csv_file_path) == 0:
        # 将更新后的数据写入空的CSV文件
        df.to_csv(csv_file_path, index=False)
        break

# 打印更新后的数据
# print(df)