#ifndef COMPLEX_NUMBERS_EXAMPLE
#define COMPLEX_NUMBERS_EXAMPLE

#include <iostream>
using namespace std;

class Complex{
    private:
        float real;
        float ima;
    public:
        Complex(int, int);
        friend ostream& operator<<(ostream& , Complex &);
        Complex operator+(Complex);
        friend Complex operator-(Complex, Complex);
};


#endif
