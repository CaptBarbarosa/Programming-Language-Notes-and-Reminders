#include <stdio.h>

int Add(int a, int b){
    return a+b;
}

int main(){
    int (*p)(int, int); // p is a pointer to a function that gets two integer variables from the caller function and returns an integer.
    p=&Add; // P points to the address of Add.
    int a = p(2,3);
    printf("a=%d\n",a);
    return 0;
}
