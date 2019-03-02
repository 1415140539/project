def locate_pass(list):
    left_right = 0
    up_down = 0
    for i in list:
        if i == "":
            continue
        if i[0] == "A":
            if i[1:].strip().isdigit():
                left_right -= int(i[1:])
        if i[0] == "D":
            if i[1:].strip().isdigit():
                left_right += int(i[1:])
        if i[0] == "W":
            if i[1:].strip().isdigit():
                up_down += int(i[1:])
        if i[0] == "S":
            if i[1:].strip().isdigit():
                up_down -= int(i[1:])
    return left_right,up_down

locate = input("").strip()
locate = locate.split(";")
left_right,up_down = locate_pass(locate)
print(str(left_right)+","+str(up_down))