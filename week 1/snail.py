H = int(input())
A = int(input())
B = int(input())
D = A - B
print(1 + (H - A) // (A - B) + ((H - A) % (A - B) + A - B - 1) // (A - B))
