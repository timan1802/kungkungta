import pandas as pd

#UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 40-41: unexpected end of data
# df = pd.read_excel("../dict_xls/951675_420000.xls", engine='xlrd')
df = pd.read_excel("../dict_xls/951675_420000-encoding.xls")
print("전체 사이즈", df.size)
print(df)