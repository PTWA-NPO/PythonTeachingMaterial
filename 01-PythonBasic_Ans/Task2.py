# Task 2 
"""
1. 根據使用者的生日，計算出使用者的年齡
2. 如果大於18歲，根據性別用哥哥姊姊作為稱呼 ex: Kylin 是哥哥
3. 如果小於12歲，用弟弟妹妹來稱呼 ex: Kylin 是弟弟
"""
name = "Kylin"
gender = "Male"
year = "1993"
month = 8
date = 15

print(name," 的生日是 ",year,"/",month,"/",date)
age = 2020-int(year)
print(name,"今年",age,"歲")
if age>18:
    if gender =="Male":
        print(name,"是哥哥")
    else:
        print(name,"是姊姊")
elif age<12:
    if gender =="Male":
        print(name,"是弟弟")
    else:
        print(name,"是妹妹")
