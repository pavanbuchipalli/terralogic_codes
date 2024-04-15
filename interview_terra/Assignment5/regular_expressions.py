data ="https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
import re
#
#
pattern = r'(\d{4})/(\d{2})/(\d{2})'
s = re.search(pattern,data).group()
c = s.split("/")
d = ["year","month","day"]
for i in range(len(c)):
    print("The mentioned {} in the url is {}".format(d[i],c[i]))









# text = " i am pavan "
#
# t=  "a"
# result = re.findall(t,text)
# print(result)

