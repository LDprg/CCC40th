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
            val = 0

            while val != num:
                for num1 in cur_max:
                    if num - val >= num1:
                        cnt[cur_max.index(num1)] += 1
                        val += num1
                        break

            for i in range(c):
                if cnt[i] > 0:
                    out += str(cnt[i]) + "x" + str(cur_max[i]) + " "
            out += "\n"


    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


main("level3_1")

#for i in range(1, 6):
#    main("level3_" + str(i))
