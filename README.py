# A.-Coins
for _ in range(int(input())):
    n, k = map(int, input().split())
    count = 0
    if n % 2 == 0 and n % k == 0:
        count += 1
    elif n % 2 == 0 or n % k == 0:
        count += 1
    tot = n - k
    if tot % 2 == 0:
        count += 1
    if count >= 1:
        print("Yes")
    else:
        print("No")
