n = int(input())
n1 = n // 1000
n4 = n % 10
n2 = (n // 100) % 10
n3 = ((n // 10) % 100) % 10
# print(n1,n2,n3,n4)
print((n1 * 10 + n2) - (n4 * 10 + n3) + 1)
