import pandas
## PIP Install을 먼저 진행 후 출력가능
## pip install pandas
# 그 후 엑셀에서 csv 다운로드 받은 후 폴더에 넣고 불러오자.
house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))
print(house.describe())



