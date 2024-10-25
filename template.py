example = False


def main(name):
    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())
    c = int(in_file.readline())

    for line in in_file.readlines():
        break

    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


if example:
    main("level1_example")
else:
    for i in range(1, 6):
        main("level1_" + str(i))
