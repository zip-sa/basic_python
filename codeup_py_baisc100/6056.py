a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))
# print('a =', c, '\nb =', d)
# print('not a =', not c, '\nnot b =', not d)
# print()