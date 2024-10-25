example = False
example = True

cnt = 0


def calc(arr, x, y, c):
    global cnt

    if x % 2 != 0:
        for j in range(x):
            for i in range(y):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 3 != 2 and j % 2 == 0 and (i < (y // 3) * 3 - 3 + y % 3 or y % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1

        for i in range(y):
            for j in range(x):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 2 != y % 2 and j % 3 != 2 and (j < (x // 3) * 3 or x % 3 == 2) and not (
                        i < (y // 3) * 3 - 3 + y % 3 or y % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1
    elif y % 2 != 0:
        for i in range(y):
            for j in range(x):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 2 == 0 and j % 3 != 2 and (j < (x // 3) * 3 - 3 + x % 3 or x % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1

        for j in range(x):
            for i in range(y):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 3 != 2 and j % 2 == 1 and not (j < (x // 3) * 3 - 3 + x % 3 or x % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1
    elif y > 5 and x > 5:
        for i in range(y):
            for j in range(x):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 2 == 0 and j < 2 and i < y - 3:
                    arr[i][j] = 'X'
                    cnt += 1

                if i % 2 == 1 and x - j < 3 and i > 2:
                    arr[i][j] = 'X'
                    cnt += 1

        for j in range(x):
            for i in range(y):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if j % 2 == 1 and i < 2 and j > 2:
                    arr[i][j] = 'X'
                    cnt += 1

                if j % 2 == 0 and j < x - 3 and i > y - 3:
                    arr[i][j] = 'X'
                    cnt += 1

        if x > 6 and y > 6:
            arr1 = [['.' for _ in range(3, x - 3)] for _ in range(3, y - 3)]

            calc(arr1, x - 6, y - 6, c)

            for i in range(len(arr1)):
                for j in range(len(arr1[i])):
                    arr[i + 3][j + 3] = arr1[i][j]
    else:
        for j in range(x):
            for i in range(y):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 3 != 2 and j % 2 == 0 and (i < (y // 3) * 3 or y % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1

        for i in range(y):
            for j in range(x):
                if cnt % 2 == 0 and cnt // 2 == c:
                    break

                if i % 2 != y % 2 and j % 3 != 2 and (j < (x // 3)*3 or x % 3 == 2) and not (i < (y // 3) * 3 or y % 3 == 2):
                    arr[i][j] = 'X'
                    cnt += 1
def main(name):
    global cnt

    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())

    for line in in_file.readlines():
        line = line.split(" ")
        x, y, c = int(line[0]), int(line[1]), int(line[2])

        cnt = 0

        arr = [['.' for _ in range(x)] for _ in range(y)]

        calc(arr, x, y, c)

        if cnt // 2 != c:
            out += "Invalid " + str(cnt // 2) + " " + str(c) + "\n"

        out += str(x) + "x" + str(y) + "\n"

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
    main("level5_example")
else:
    for i in range(1, 6):
        main("level5_" + str(i))
