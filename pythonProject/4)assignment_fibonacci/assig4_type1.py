def fid(number):
    global third_num
    first_num = 0
    second_num = 1
    # print(first_num)
    # print(second_num)
    for i in range(2, number + 1):
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
    print(" The fibonacci value of {} is".format(number), third_num)


fid(6)
