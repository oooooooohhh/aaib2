#include <stdio.h>

int main()

{
    int a,b;
    printf("�п�J��Ӿ��:"); ///���L���崣�ܧA��J
    scanf("%d %d", &a,&b); ///scanf()�n�[ & �Ÿ�
    printf("�A��J�F2�ӼƦr,�����[�k:\n");
    printf("5d\n",a); ///�L�X��, 5�檺���, �᭱\n����
    printf("%5d\n",b);
    printf("------\n"); ///�L�X------�, �᭱\n����
    printf("%5d\n",a+b);
}
