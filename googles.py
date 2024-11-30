from googlesearch import search as s
keywords=input("enter your query")

reasult=s(keywords,20)
for i in reasult:
    print(i)