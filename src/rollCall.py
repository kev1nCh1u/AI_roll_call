import os
import pandas as pd

dirname, _= os.path.split(os.path.abspath(__file__))    #取得檔案路徑
path = r"" + dirname
cl = ["四電四丙", "四電四丙", "四電四丙", "四電四丙"]  
name = ["邱暐凱","吳定軒","劉建廷","林舒潔"]
num = ["1105192113","1105105340","1105448787","6644666666"]
att = ["X", "X", "X", "X"]
student_list = {"班級": cl,  
        "學生": name,
        "學號":num,
        "出缺席":att
        }
select_df = pd.DataFrame(student_list)

def create():
    select_df.to_csv('/home/user/AI_roll_call/data/student.csv',index=False,encoding='utf_8_sig')
    #select_df.to_csv(r"" + path + "\\student.csv",index=False,sep=',',encoding='utf_8_sig')

    print("---student_list")
    print(select_df) # 回傳資料內容

def checkStudent(student):    
    for i in range(0, len(num)):
        if  student == num[i]:
            print(num[i])
    out_df = select_df[select_df.loc[:,"學號"] == student].index
    select_df.iloc[out_df.values,3] = "V" 
    out_df1 = select_df[select_df.loc[:,"學號"] == student] #印出確認
    #print(out_df1)
    select_df.to_csv('/home/user/AI_roll_call/data/student.csv',index=False,encoding='utf_8_sig')

create()

#for i in ["1105192113","1105105340","1105448787","6644666666"]:
#    checkStudent(i)