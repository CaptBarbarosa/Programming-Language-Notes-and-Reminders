#include<stdio.h>

int main(){ // A void pointer can hold data in other data tyoes as well. 
    int a = 10;
    void *ptr = &a ;
    printf("ptr is holding the value %d and its size is: %zu (because it holds an address its 8 bytes(addresses are 8 bytes)) and its address is: %p\n",*(int *)ptr,sizeof(ptr),ptr);
    void *ptr2 = 0x0x7ffd609af09c;
    printf("Integer value at address %p is: %d\n",ptr2,*(int *)ptr2);

    //void *ptr3;
    //*(int *)ptr3=0xDEADBEEF;
    //printf("Address of p is: ");
    return 0;
}

