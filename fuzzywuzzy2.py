from difflib import SequenceMatcher
import pandas as pd
#s_1 = 'Mohen.Mehta'
#s_2 = 'Mohan.Mehte'

df=pd.read_excel('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\Sample.xlsx')

df1=pd.read_excel('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\Sample1.xlsx')
keywords=df['Name List ECI']

actual=df1['Name List myneta']
final=[]

for i in keywords:
    maxi=0.0
    s=i
    for j in actual:
        x=SequenceMatcher(a=str(i),b=str(j)).ratio()
        #print(x)
        if(x>maxi):
            maxi=x
            s=j
            #print(s)
    final.append(s)

df2=pd.DataFrame({'Best Match':final})

writer=pd.ExcelWriter('a.xlsx')
df2.to_excel(writer,'Sheet1')
writer.save()


#print(SequenceMatcher(a=s_1,b=s_2).ratio())
