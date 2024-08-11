#ifndef RATIONAL_NUMBER_H
#define RATIONAL_NUMBER_H

#include <iostream>

class Rational_Number {
    private:
        int numerator;
        int denominator;
        void reduce();

    public:
        Rational_Number();
        Rational_Number(int, int);

        Rational_Number operator+(const Rational_Number&) const;
        Rational_Number operator-(const Rational_Number&) const;
        Rational_Number operator*(const Rational_Number&) const;
        Rational_Number operator*(int) const;
        Rational_Number operator/(const Rational_Number&) const;

        Rational_Number operator^(int) const;

        bool operator==(const Rational_Number&) const;

        Rational_Number operator-() const;

        Rational_Number& operator++();
        Rational_Number operator++(int);
        Rational_Number& operator--();
        Rational_Number operator--(int);

        Rational_Number operator!() const;

        friend std::ostream& operator<<(std::ostream&, const Rational_Number&);
};
#endif
