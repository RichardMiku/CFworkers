import pandas as pd

# 读取 ip.csv 文件
file_path = 'ip.csv'
df = pd.read_csv(file_path)

# 更新 '数据中心' 列的值
df['数据中心'] = df.apply(lambda row: f"{row['数据中心']}-{row['下载速度']}", axis=1)

# 将更新后的数据写入 process_ip.csv
df.to_csv('process_ip.csv', index=False)

# 打印更新后的数据
print(df)