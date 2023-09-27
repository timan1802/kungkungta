import os
import pickle
import re

import pandas as pd

# 사전 xls 파일에서 3글자만 가져와서 pickle로 저장.

only_3word_list = []
xls_dir_path = "../dict_xls"

for (root, directories, files) in os.walk(xls_dir_path):
    for file in files:
        if '.xls' in file:
            xls_file_path = os.path.join(root, file)
            print(xls_file_path)
            df = pd.read_excel(xls_file_path)
            print("전체 사이즈", df.size)

            df = df.loc[(df['구성 단위'] == '단어', ['어휘'])]  # 구성 단위가 '단위'만 필터, 어휘만 저장.

            word_list = [re.sub('[^가-힣]', '', s) for s in df['어휘']]  # 한글만, 특수문자 제거

            word_set = set(word_list)  # set으로 중복 제거
            word_list = list(word_set)  # 다시 list로 변환

            # 3글자 단어만 필터
            filtered_iter = filter(lambda x: len(x) == 3, word_list)
            filtered_list = list(filtered_iter)

            print("단어 사이즈", len(filtered_list))
            print(filtered_list)
            only_3word_list.extend(filtered_list)
            print(len(only_3word_list))

with open('../dict_pkl/only_3word.pkl', 'wb') as f:
    pickle.dump(only_3word_list, f)
