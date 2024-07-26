#include<stdio.h>
int main(){
	int x = 0xFEEDBEEF;
	void *p;
	int *ip = &x;
	p=ip;
	*ip = 0x00C0FFEE;
	*(int *)p = 0xDEADBEEF;
	printf("sizeof(void*) = %zu\n",sizeof(p));
	printf("p-> %p (%x)\n",p,*(int *)p);
    return 0;
}

