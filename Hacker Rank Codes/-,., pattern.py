row, col = map(int, input().split())

i = 1

# Top part
while i < row:
    pattern_len = 3 * i
    dashes = (col - pattern_len) // 2

    print("-" * dashes + ".|." * i + "-" * dashes)
    i += 2

# Middle part
welcome = "WELCOME"
dashes = (col - len(welcome)) // 2
print("-" * dashes + welcome + "-" * dashes)

# Bottom part
i = row - 2
while i >= 1:
    pattern_len = 3 * i
    dashes = (col - pattern_len) // 2

    print("-" * dashes + ".|." * i + "-" * dashes)
    i -= 2


