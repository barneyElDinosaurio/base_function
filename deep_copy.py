# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import copy


def copy_case():
    list1 = [1, 2, 3, ['a', 'b', 'd', 'd']]
    list2 = list1
    print(list1)
    list1.append(5)
    print(list1)
    list1[3].append('e')
    print(list1)
    print(list1[3][2])

    print("list2", list2)
    print("list1", list1)
    print("Check address : list1: ", id(list1), " list2: ", id(list2))


def validate_case():
    dict1 = {"a": "apple", "o": "orange", 'b': ['a', 'b', 'c', 'd']}
    # 浅复制 dict2 = copy.copy(dict1)


    # 深复制
    dict2 = copy.deepcopy(dict1)

    dict1['b'].append('f')
    print(dict1)
    print(dict2)


def main():
    # copy_case()
    validate_case()


if __name__ == '__main__':
    main()
