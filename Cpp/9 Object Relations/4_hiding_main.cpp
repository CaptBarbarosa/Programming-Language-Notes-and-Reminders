#include <iostream>
#include "4_hiding_header.h"
using namespace std;

int main(){
    B first_b(4, 5);
    first_b.print();

    A first_a(1);
    first_a.print();

    A *second_a;
    second_a = new B(1,2);
    second_a->print();
    //second_a->b_exclusive(); This will
    return 0;
}
