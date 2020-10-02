t = int(input())
ans = [0]*t
for i in range(t):
  a, b=input().split()
  n = int(a)
  k = int(b)
  if k == 0 and n == 0:
    ans[i] = 0
  elif k == 0 and n != 0:
    if n%2 == 0:
      ans[i] = 0
    else:
      ans[i] = 1
  elif k>n:
    ans[i] = k-n
  elif (n%2 == 0 and k%2 != 0):
    ans[i] = 1
  elif (n%2 != 0 and k%2 == 0):
    ans[i] = 1
  else:
    ans[i] = 0

for i in range(t):
  print(ans[i])
