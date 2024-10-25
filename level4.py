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

        arr = [['.' for _ in range(x)] for _ in range(y)]

        for j in range(x):
            for i in range(y):
                if cnt % 3 == 0 and cnt // 3 == c:
                    break

                if i % 4 != 3 and j % 2 == 0 and (i < (y // 4)*4 or y % 4 == 3):
                    arr[i][j] = 'X'
                    cnt += 1

        for i in range(y):
            for j in range(x):
                if cnt % 3 == 0 and cnt // 3 == c:
                    break

                if i % 2 == 0 and j % 4 != 3 and (j < (x // 4)*4 or x % 4 == 3) and not (i < (y // 4)*4 or y % 4 == 3):
                    arr[i][j] = 'X'
                    cnt += 1

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                out += str(arr[i][j])
            out += "\n"
        out += "\n"

    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


if example:
    main("level4_example")
else:
    for i in range(1, 6):
        main("level4_" + str(i))
