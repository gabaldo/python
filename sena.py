import random
from operator import itemgetter


def build_list():
    i = 0
    l = []
    while i < 1000000:
        l.append(random.randrange(1, 61))
        i += 1
    return l


if __name__ == '__main__':
    dic = {}
    end_list = build_list()
    for element in end_list:
        if element not in dic:
            dic[element] = 1
        else:
            dic[element] += 1


    all_elements = sorted(dic.items(), key=itemgetter (1), reverse=True)

    print(all_elements[0])
    print(all_elements[1])
    print(all_elements[2])
    print(all_elements[3])
    print(all_elements[4])
    print(all_elements[5])