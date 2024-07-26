/*
    Function pointers alllow us to pass functions as arguments to other functions, return functions from functions and store functions in arrays or structures.
*/

#include<stdio.h>
#include<stdlib.h>
int add(int a, int b){
    return a+b;
}
int subtract(int a, int b) {
    return a - b;
}
// Here we go to the specified function, the function returns a value to the operate function and operate returns it to the caller function.
int operate(int x, int y, int (*operation)(int, int)) {
    return operation(x, y);
}
int main() {
    int (*func_ptr)(int, int) = add;
    int result = func_ptr(10, 20);
    printf("Result using function pointer: %d\n", result);

    int sum = operate(10, 5, add);
    int diff = operate(10, 5, subtract);
    printf("Sum: %d, Difference: %d\n", sum, diff);
    
    int (*operations[2])(int, int) = {add, subtract};
    sum = operations[0](10, 20);
    diff = operations[1](20, 10); 
    printf("Sum from array: %d, Difference from array: %d\n", sum, diff);
    
    typedef struct {
        int (*operation)(int, int);
    } Operation;
    Operation op;
    op.operation = add;
    result = op.operation(10, 20);
    printf("Result from structure: %d\n", result);
    return 0;
}
