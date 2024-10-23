def main(name):
    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())
    c = int(in_file.readline())

    for cur in in_file.readlines():
        cur = cur.split(" ")
        cur = [int(x) for x in cur]

        br = False

        for num1 in cur:
            if br:
                break
            for num2 in cur:
                if not num1 + num2 in cur:
                    out += str(num1 + num2) + "\n"
                    br = True
                    break

    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


#main("level1_example")

for i in range(1, 6):
    main("level1_" + str(i))
