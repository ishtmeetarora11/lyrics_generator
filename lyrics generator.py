import random
text1=open("untitled1.txt","r").read()
text2=open("untitled2.txt","r").read()
def create_table(text1,text2,k=3):
    t={}
    for i in range(len(text1)-k):
        u=text1[i:i+k]
        y=text1[i+k]
        if u in t:
            if y in t[u]:
                t[u][y]+=1
            else:
                t[u][y]=1
        else:
            t[u]={
                y:1}
    for key,value in t.items():
        total=sum(t[key].values())
        for key1 in t[key]:
            t[key][key1]/=total
    for i in range(len(text1)-k):
        a=text1[i:i+k]
        b=text1[i+k]
        if a in t:
            if b in t[a]:
                t[a][b]+=1
            else:
                t[a][b]=1
        else:
            t[a]={
                b:1}
    for key,value in t.items():
        total=sum(t[key].values())
        for key1 in t[key]:
            t[key][key1]/=total        
            
    return t
table=create_table(text1,text2)
def next(inp,table):
    inp=inp[-3:]
    if inp in table:
        outcomes=list(table[inp].keys())
        probs=list(table[inp].values())
        return random.choices(outcomes, weights=probs)[0]
    else:
        return " "
def generate(start,table,length=1000):
    for _ in range(length):
        start+=next(start,table)
    return start 
