example = True
example = False


def main(name):
    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())

    for line in in_file.readlines():
        line = line.split(" ")
        x, y, c = int(line[0]), int(line[1]), int(line[2])

        cnt = 0

        arr = [[0 for _ in range(x)] for _ in range(y)]

        for y in arr:
            for x in y:
                out += str((cnt // 3)+1) + " "
                cnt+=1
            out += "\n"
        out += "\n"


    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


if example:
    main("level2_example")
else:
    for i in range(1, 6):
        main("level2_" + str(i))
