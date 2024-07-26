#include<stdio.h>

void print_ii(int a, int b) { printf("int, int\n"); }
void print_di(double a, int b) { printf("double, int\n"); }
void print_iii(int a, int b, int c) { printf("int, int, int\n"); }
void print_default(void) { printf("unknown arguments\n"); }

#define print(...) _Generic((__VA_ARGS__), \
                           ((int, int), print_ii), \
                           ((double, int), print_di), \
                           (default: print_iii)(__VA_ARGS__)

int main(void) {
    print(44, 47);   // prints "int, int"
    print(4.4, 47);  // prints "double, int"
    print(1, 2, 3);  // prints "int, int, int"
//    print("");       // prints "unknown arguments"

    return 0;
}

