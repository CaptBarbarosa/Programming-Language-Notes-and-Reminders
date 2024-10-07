#include "1_complex_numbers_example_header.h"
#include <iostream>
using namespace std;

int main() {
    
    Complex c1(5,4);
    cout << c1;
    Complex c2(2,2);
    c2 = c2 + c1;
    cout << c2;
    c2 = c2 - c1;
    cout << c2;
    return 0;
}
