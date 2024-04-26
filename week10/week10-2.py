#輾轉相除法 最大公因數
#a大的 b中的 c小的a%b


#include <stdio.h>
def gcd(a,b):
    if a==0: return b; #有人會省略這一條
    if b==0: return a; #老二生級變老大,老三變老二
    return gcd(b,a%b);


print("請輸入 a b 兩個數字:");
a=int(input('請輸入a:'))
b=int(input('請輸入b:'))

print("最大公因數是:",gcd(a,b));
