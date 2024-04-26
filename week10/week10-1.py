N = int(input('請輸入'))
#以前是用for迴圈寫, 今天用<函式呼叫式>來寫
def func(n):
  if n==1: return 1
  return n * func(n-1)
ans = func(N)
print(ans)