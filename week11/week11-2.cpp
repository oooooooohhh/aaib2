///week11-2.cpp 要用篩子法
///以前的寫法,只要30萬*30萬=900億次
///用篩子法,只要30萬+殺掉的那些格子,快20萬倍
#include <stdio.h>
int table[20000] = {}; ///給初始,都補0
int main()
{
   int BOUND = 20000, ans = 0;
   for(int i=2;i<BOUND;i++){
       if(table[i]==0){ ///還留著,沒有被殺掉
            ans ++;
            for(int k=i*i;k<BOUND;k+=i){
                table[k] = -1; ///殺死它的兄弟
            }
       }
   }
   printf("質數有: %d個\n",ans);
}
