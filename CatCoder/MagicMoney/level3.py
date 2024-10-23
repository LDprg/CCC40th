import time
from copy import deepcopy


def coins(cur, cnt, num, i):
    cnt = deepcopy(cnt)
    num = deepcopy(num)

    if num == 0:
        return cnt

    cnt1 = None
    cnt2 = None

    if num >= cur[i]:
        cnt_tmp = deepcopy(cnt)

        cnt_tmp[cur.index(cur[i])] += 1

        cnt1 = coins(cur, cnt_tmp, num - cur[i], i)

        # noinspection PyChainedComparisons
        if i < len(cur)-1 and num >= cur[i+1] and num < (cur[i+1] + cur[i])*cur[i+1]:
            cnt_tmp = deepcopy(cnt)

            cnt_tmp[cur.index(cur[i+1])] += 1

            cnt2 = coins(cur, cnt_tmp, num - cur[i+1], i)

            if sum(cnt1) <= sum(cnt2):
                return cnt1
            else:
                return cnt2

        return cnt1

    return coins(cur, cnt, num, i + 1)


def main(name):
    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())
    c = int(in_file.readline())

    for cur in in_file.readlines():
        cur = cur.split(" ")
        cur = [int(x) for x in cur]

        cur_max = cur.copy()
        cur_max.reverse()

        for num in range(1, 101):

            cnt = [0 for i in range(c)]

            cnt = coins(cur_max, cnt, num, 0)

            for i in range(c):
                if cnt[i] > 0:
                    out += str(cnt[i]) + "x" + str(cur_max[i]) + " "
            out = out[:-1]
            out += "\n"

    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


#main("level3_example")

for i in range(1, 6):
    main("level3_" + str(i))
