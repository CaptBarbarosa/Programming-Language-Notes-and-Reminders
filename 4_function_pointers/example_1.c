#include <stdlib.h>
#include <stdio.h>

typedef int (*specified_operation) (int, int);

int addition(int x, int y)  {return x+y;}
int multiply(int x, int y)  {return x*y;}

int do_some_operation(specified_operation op, int x, int y){
    return op(x,y);
}

int main(){
    int addition_result = do_some_operation(addition, 9,10);
    int production_result = do_some_operation(multiply, 9, 10);
    printf("Addition = %d\nMultiplication = %d\n",addition_result, production_result);
    return 0;
}
