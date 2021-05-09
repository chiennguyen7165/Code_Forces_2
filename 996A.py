n = int(input())
bill = [100, 20, 10, 5, 1]
thuong100 = int(n / 100)
du100 = n % 100
thuong50 = int(du100 / 20)
du50 = du100 % 20
thuong10 = int(du50 / 10)
du10 = du50 % 10
thuong5 = int(du10 / 5)
du5 = du10 % 5
thuong1 = int(du5 / 1)
print(thuong100 + thuong50 + thuong10 + thuong5 + thuong1)