# 3. Write a program that display following output:
#  SHIFT
#  HIFTS
#  IFTSH
#  FTSHI
#  TSHIF
#  SHIFT


str="SHIFT"

for i in range(len(str)):
    print(str[i:] + str[:i])
