#include "1_complex_numbers_example_header.h"

Complex:: Complex(float real, float ima){
    this-> real = real;
    this-> ima = ima;
}

ostream& operator<<(ostream& o, Complex &c){
    o<<"Real: "<< c.real<<" Imaginary: "<< c.ima<< endl;
    return o;
}

Complex Complex::operator+(Complex other){
    Complex to_return(0,0);
    to_return.real = this->real + other.real;
    to_return.ima = this->ima + other.ima;
    return to_return;
}

Complex operator-(Complex c1, Complex c2){
    Complex to_return(0,0);
    to_return.real = c1.real - c2.real;
    to_return.ima = c1.ima - c2.ima;
    return to_return;
}
