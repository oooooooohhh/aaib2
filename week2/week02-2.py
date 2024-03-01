class Solution {
public:
    string maximumOddBinaryNumber(string s) {
     int N = s.length(); //C++ 字串的長度
     int one = 0; //s裡面, 有幾個1呢?等遺下會慢慢數出來
     for(int i=0; i<N; i++){
         if(s[i]=='1') one += 1;
     }
     //print("N:%d one:%d",N,one);
     string ans;
     for(int i=0; i<one-1; i++) ans +='1';
     for(int i=0; i<N-one; i++) ans +='0';
     ans += '1';

     return ans;
    }
};