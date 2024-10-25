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

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j - len(arr[i]) % 3 >= 0:
                    arr[i][j] += (cnt // 3) + 1
                    cnt += 1
                else:
                    arr[i][j] += 0

        for j in range(len(arr[i])):
            for i in range(len(arr)):
                if j - len(arr[i]) % 3 < 0 and i - len(arr) % 3 >= 0:
                    arr[i][j] += (cnt // 3) + 1
                    cnt += 1
                else:
                    arr[i][j] += 0

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                out += str(arr[i][j]) + " "
            out += "\n"
        out += "\n"



    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


if example:
    main("level3_test")
    main("level3_example")
else:
    for i in range(1, 6):
        main("level3_" + str(i))
