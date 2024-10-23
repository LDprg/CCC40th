def main(name):
    in_file = open(name + ".in", "r")
    out_file = open(name + "_.out", "w")

    out = ""

    n = int(in_file.readline())
    c = int(in_file.readline())
    a = int(in_file.readline())

    for i in range(n):
        cur = in_file.readline()
        cur = cur.split(" ")
        cur = [int(x) for x in cur]

        amo = in_file.readline()
        amo = amo.split(" ")
        amo = [int(x) for x in amo]

        for num in amo:
            br = False
            for num1 in cur:
                if br:
                    break
                for num2 in cur:
                    if num1 + num2 == num:
                        out += str(num1) + " " + str(num2) + "\n"
                        br = True
                        break

    print(out)
    out_file.write(out)

    out_file.close()
    in_file.close()


#main("level2_example")

for i in range(1, 6):
    main("level2_" + str(i))
