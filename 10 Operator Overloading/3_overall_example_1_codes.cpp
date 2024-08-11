#include "3_overall_example_1_header.h"
#include <cmath>

int gcd_calculator(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;}
    return a;
}

Rational_Number::Rational_Number() : numerator(0), denominator(1) {}

Rational_Number::Rational_Number(int num, int denom) : numerator(num), denominator(denom){
    reduce();}

void Rational_Number::reduce() {
    int gcd = gcd_calculator(numerator, denominator);
    numerator /= gcd;
    denominator /= gcd;

    if (denominator < 0) {
        numerator = -numerator;
        denominator = -denominator;
    }
}

Rational_Number Rational_Number::operator+(const Rational_Number& other) const {
    int num = numerator * other.denominator + other.numerator * denominator;
    int denom = denominator * other.denominator;
    return Rational_Number(num, denom);
}

Rational_Number Rational_Number::operator-(const Rational_Number& other) const {
    int num = numerator * other.denominator - other.numerator * denominator;
    int denom = denominator * other.denominator;
    return Rational_Number(num, denom);
}

Rational_Number Rational_Number::operator*(const Rational_Number& other) const {
    int num = numerator * other.numerator;
    int denom = denominator * other.denominator;
    return Rational_Number(num, denom);
}

Rational_Number Rational_Number::operator/(const Rational_Number& other) const {
    int num = numerator * other.denominator;
    int denom = denominator * other.numerator;
    return Rational_Number(num, denom);
}

Rational_Number Rational_Number::operator^(int power) const {
    int num = std::pow(numerator, power);
    int denom = std::pow(denominator, power);
    return Rational_Number(num, denom);
}

bool Rational_Number::operator==(const Rational_Number& other) const {
    return numerator == other.numerator && denominator == other.denominator;
}

Rational_Number Rational_Number::operator-() const {
    return Rational_Number(-numerator, denominator);
}

Rational_Number& Rational_Number::operator++() {
    numerator += denominator;
    reduce();
    return *this;
}

Rational_Number Rational_Number::operator++(int) {
    Rational_Number temp = *this;
    numerator += denominator;
    reduce();
    return temp;
}

Rational_Number& Rational_Number::operator--() {
    numerator -= denominator;
    reduce();
    return *this;
}

Rational_Number Rational_Number::operator--(int) {
    Rational_Number temp = *this;
    numerator -= denominator;
    reduce();
    return temp;
}

Rational_Number Rational_Number::operator!() const {
    return Rational_Number(denominator, numerator);
}

std::ostream& operator<<(std::ostream& out, const Rational_Number& rational) {
    out << rational.numerator << "/" << rational.denominator;
    return out;
}

