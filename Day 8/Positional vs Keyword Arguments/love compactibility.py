def calculate_love_score(he, she):
    count = 0
    counr = 0
    counu = 0
    coune = 0
    counl = 0
    couno = 0
    counv = 0
    coune2 = 0

    combined = he + she

    for i in combined:
        if i == 't':
            count += 1
        elif i == 'r':
            counr += 1
        elif i == 'u':
            counu += 1
        elif i == 'e':
            coune += 1

    total = count + counr + counu + coune

    for i in combined:
        if i == 'l':
            counl += 1
        elif i == 'o':
            couno += 1
        elif i == 'v':
            counv += 1
        elif i == 'e':
            coune2 += 1

    total2 = counl + couno + counv + coune2

    return int(str(total) + str(total2))


he = input("Enter his name:\n").lower()
she = input("Enter her name:\n").lower()

love_score = calculate_love_score(he, she)
print(f"Love Score = {love_score}")