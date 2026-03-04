import re
r="Admin@gmail.com"
r1=re.findall(r"[a-zA-Z0-9_.%+-]+@[a-z]+\.[a-z.]{2,}",r)
print(r1)

