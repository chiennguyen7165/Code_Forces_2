n = int(input())
gia = list(map(int, input().split()))
giaMax = max(gia)
thuMax = gia.index(giaMax)
gia.remove(giaMax)
print(thuMax + 1, max(gia))
