str="   Hello Python   "

print("upper: 대문자로 변경>>",str.upper())
print("lower: 소문자로 변경>>",str.lower())
print("strip: 양쪽 공백문자 제거>>",str.strip())
print("lstrip: 왼쪽 공백문자 제거>>",str.lstrip())
print("rstrip: 오른쪽 공백문자 제거>>",str.rstrip())


split_data="10|20|30|40|50"
print(split_data.split("|"))