#include "3_overall_example_1_header.h"
#include <iostream>

int main() {
    Rational_Number r1(1, 2);
    Rational_Number r2(3, 4);

    Rational_Number r3 = r1 + r2;
    std::cout << "r1 + r2 = " << r3 << std::endl;
    r3 = r1 - r2;
    std::cout << "r1 - r2 = " << r3 << std::endl;
    r3 = r1 * r2;
    std::cout << "r1 * r2 = " << r3 << std::endl;
    r3 = r1 / r2;
    std::cout << "r1 / r2 = " << r3 << std::endl;
    r3 = r1 ^ 2;
    std::cout << "r1 ^ 2 = " << r3 << std::endl;
    if (r1 == r2) {
        std::cout << "r1 and r2 are equal." << std::endl;
    } else {
        std::cout << "r1 and r2 are not equal." << std::endl;
    }
    std::cout << "-r1 = " << -r1 << std::endl;
    std::cout << "++r1 = " << ++r1 << std::endl;
    std::cout << "r1++ = " << r1++ << std::endl;
    std::cout << "After r1++ = " << r1 << std::endl;
    std::cout << "--r1 = " << --r1 << std::endl;
    std::cout << "r1-- = " << r1-- << std::endl;
    std::cout << "After r1-- = " << r1 << std::endl;
    std::cout << "!r1 = " << !r1 << std::endl;
    return 0;
}

