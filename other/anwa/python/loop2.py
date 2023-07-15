line = int(input('enter line : '))
m_line = line

for i in range(line + 1):
    print("\t" * line, end='')
    j = 1
    d = m_line - line
    for x in range(d):
        print(j, "\t", end="")
        j *= 2
    j //= 2
    if d > 1:
        for x in range(d - 1):
            j //= 2
            print(j, "\t", end="")
    line -= 1
    print()