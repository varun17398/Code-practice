import requests
from bs4 import BeautifulSoup
import pandas as pd

df1=pd.read_excel('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\WebID.xlsx')
id1=df1['ID']

#constituency=[]
name=[]
position=[]
party=[]
term=[]
DOB=[]
sex=[]
edu=[]
prof=[]
presentadd=[]
permadd=[]
telephone=[]

for i in range(0,len(id1)):
    try:
        print(str(i)+"     ")
        c=str(id1[i])
        print(c)
        url='http://www.parliament.gov.bd/index.php/en/mps/members-of-parliament/current-mp-s/list-of-10th-parliament-members-english?layout=edit&id='+c
        print(url)
        page=requests.get('http://www.parliament.gov.bd/index.php/en/mps/members-of-parliament/current-mp-s/list-of-10th-parliament-members-english?layout=edit&id='+c)
        soup=BeautifulSoup(page.content,'html.parser')
        s=soup.find("div",class_="item-page")
        #constituency.append(s.find('p',class_='style3').get_text())
        #x=c.get_text()
        #constituency.append(x)
        #d=s.find_all('li')
        a=s.find_all('li')[0].get_text()
        b=s.find_all('li')[1].get_text()
        c=s.find_all('li')[2].get_text()
        d=s.find_all('li')[3].get_text()
        e=s.find_all('li')[4].get_text()
        f=s.find_all('li')[5].get_text()
        g=s.find_all('li')[6].get_text()
        h=s.find_all('li')[7].get_text()
        i=s.find_all('li')[8].get_text()
        j=s.find_all('li')[9].get_text()
        k=s.find_all('li')[10].get_text()
        name.append(a)
        position.append(b)
        party.append(c)
        term.append(d)
        DOB.append(e)
        sex.append(f)
        edu.append(g)
        prof.append(h)
        presentadd.append(i)
        permadd.append(j)
        telephone.append(k)

    except Exception as e:
        #constituency.append('0')
        name.append('0')
        position.append('0')
        party.append('0')
        term.append('0')
        DOB.append('0')
        sex.append('0')
        edu.append('0')
        prof.append('0')
        presentadd.append('0')
        permadd.append('0')
        telephone.append('0')


df=pd.DataFrame({'ID of cand':id1,'Name':name,'Position':position,'Party':party,'Term':term,'DOB':DOB,'Gender':sex,'Education':edu,'Profession':prof,
                 'Present Address':presentadd,'Permanent Address':permadd,'Telephone':telephone})

writer=pd.ExcelWriter('C:\\Users\\rakesh.bachu\\Desktop\\Long Forms\\fulldata.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

#print(s.find_all('li')[11].get_text())

