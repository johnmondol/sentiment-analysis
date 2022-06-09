import requests 
import pandas as pd 
from bs4 import BeautifulSoup

def clean_para(para):
    file1 = open("words/StopWords_Auditor.txt","r+")
    a = file1.read().split()
    file1.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)
    
    file2 = open("words/StopWords_Currencies.txt","r+")
    a = file2.read().split()
    file2.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)

    file3 = open("words/StopWords_DatesandNumbers.txt","r+")
    a = file3.read().split()
    file3.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)

    file4 = open("words/StopWords_Generic.txt","r+")
    a = file4.read().split()
    file4.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)

    file5 = open("words/StopWords_GenericLong.txt","r+")
    a = file5.read().split()
    file5.close()
    for i in para:
        if i.lower() in a:
            para.remove(i)

    file6 = open("words/StopWords_Geographic.txt","r+")
    a = file6.read().split()
    file6.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)

    file7 = open("words/StopWords_Names.txt","r+")
    a = file7.read().split()
    file7.close()
    for i in para:
        if i.upper() in a:
            para.remove(i)
    return para
    
def get_word_count(fn):
    file = open("output_files/{}.txt".format(fn),"r+")
    para = file.read().split()
    file.close()
    cpara = clean_para(para)
    file.close()
    wc=0
    for i in cpara:
        wc = wc + 1
    return wc

def calc_positive_score(fn):
    file = open("output_files/{}.txt".format(fn),"r+")
    file2 = open("words/positive-words.txt","r+")
    para = file.read().split()
    file.close()
    cpara = clean_para(para)
    positive = file2.read().split()
    file2.close()
    pscore=0
    for i in cpara:
        if i in positive:
            pscore=pscore+1
    return pscore

def calc_negative_score(fn):
    file = open("output_files/{}.txt".format(fn),"r+")
    file2 = open("words/negative-words.txt","r+")
    para = file.read().split()
    file.close()
    cpara = clean_para(para)
    negative = file2.read().split()
    file2.close()
    nscore=0
    for i in cpara:
        if i in negative:
            nscore=nscore+1
    return nscore

#Extracting title and article paragraphs from the links and storing them into txt file
df = pd.read_excel(r'links.xlsx')
df["URL_ID"] = df["URL_ID"].astype(int)
for i in range(len(df)) :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    URL = df.iloc[i, 1]
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(class_="article__title")
    para = soup.find(class_="article-content")
    article = ''
    for data in para.find_all("p"):
        t = data.get_text()
        article = article + t

    fn=df.iloc[i, 0].astype(str)
    print()
    #Name of the output txt files are same as their URL ID like if URL ID is 99 then output file is 99.txt
    file = open("output_files/{}.txt".format(fn),"w")
    file.write(title.text.strip())
    file.write("\n")
    file.write(article)
    file.close()


#Text Analysis of data to result.csv file
output = pd.DataFrame({"URL":[],"Positive Words":[],"Negative Words":[],"Polarity Score":[],"Word Count":[]})
df = pd.read_excel(r'links.xlsx')
df["URL_ID"] = df["URL_ID"].astype(int)
for i in range(len(df)):
    URL_ID = df.iloc[i, 0]
    url = df.iloc[i, 1]
    ps = calc_positive_score(i+1)
    ns = calc_negative_score(i+1)
    pls = (ps - ns) / (ps + ns) + 0.000001
    wc = get_word_count(i+1)
    output.loc[URL_ID] = [url,ps,ns,pls,wc]
print(output)
output.to_csv("result.csv")
