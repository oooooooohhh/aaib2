///week13-5a.cpp SOIT106_ADVANCE_009
#include <stdio.h>
#include <string.h>
int main()
{
	char line[20];
	scanf("%s",line);
	int N = strlen(line);
	for(int i=N-1;i>=0;i--){
		printf("%c",line[i]);
	}
	printf("\n");
}
