def panduan(s):
    if len(s) <= 8:
        return "NG"
    import re
    num = 0
    result = re.findall(r"[a-z]", s)
    result1 = re.findall(r"[0-9]", s)
    result2 = re.findall(r"[A-Z]", s)
    result3 = re.findall(r"[^\w]", s)
    if result:
        num += 1
    if result1:
        num += 1
    if result2:
        num += 1
    if result3:
        num += 1
    if num >= 3:
        for i in range(len(s) - 3):
            result = s[i:i + 3]
            if s[i+1:].count(result)>=1:
                return "NG"
        return "OK"
    else:
        return "NG"


while True:
    try:
        s = input("请输入长度:").strip()
        print(panduan(s))
    except:
        break
