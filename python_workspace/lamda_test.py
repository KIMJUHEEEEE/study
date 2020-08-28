# def increase(value):
#     return 10+value

# def under_3(value):
#     return value<30
# def decrease(value):
#     return value-10
original_list=[10,20,30,40,50]
print("original_data : {}".format(original_list))

# def decrease(value,original):
#     return original-value

# def call_changedata(func,decrease_v):
#     new_list=[]
#     for index,value in enumerate(original_list):
#        new_list.append(func(value))
#     return new_list

print("original_data : {0}".format(original_list))
print("new_list : {0}".format(list(map(lambda value:value+10,original_list))))
print("new_list : {0}".format(list(map(lambda value:value-10,original_list))))
print("new_list : {0}".format(list(filter(lambda value:value<40,original_list))))