class Rational_Number{
    private:
        int numerator;
        int denominator;
    public:
        Rational_Number();
        Rational_Number(int, int);
        int gcd_calculator(int, int);
        Rational_Number operator+(Rational_Number);
        friend Rational_Number operator-(Rational_Number, Rational_Number);
        Rational_Number operator*(Rational_Number);
        friend Rational_Number operator/()
};
