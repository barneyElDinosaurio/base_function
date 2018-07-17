#-*-coding=utf-8-*-

# 常见的排序算法

# 冒泡
def buble_sort(orgn_list):
    l = len(orgn_list)

    for i in range(l):
        for j in range(i+1,l-1):
            if orgn_list[i]>orgn_list[j]:
                t = orgn_list[i]
                orgn_list[i]=orgn_list[j]
                orgn_list[j]=t

    return orgn_list

# 交换
def swap_sort(origin_list):
    l = len(origin_list)
    for i in range(l):
        for j in range(i+1,l-1):
            if origin_list[i]>origin_list[l]:
                m = origin_list[l]
        t= origin_list[i]
        origin_list[i]=m
        # t =
def main():
    L= [ 1,2,3,9,7,7,2,5,10,8,6,4,9]
    print(swap_sort(L))

def case1():
    print(sorted({8: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))


#case1()
main()