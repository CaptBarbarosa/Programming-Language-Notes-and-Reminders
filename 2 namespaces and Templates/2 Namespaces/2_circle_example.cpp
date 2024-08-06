#include <iostream>
using namespace std;

namespace Circle{
    const double pi = 3.14;
    double area(double r) {return pi * r * r;}
    double perimeter(double r) {return 2 * pi * r;}
}

using namespace Circle;

int main() {
    double radius;
    cout << "Enter radius: ";
    cin >> radius;
    cout << "Area: " << Circle::area(radius) << endl;
    cout << "Perimeter: " << perimeter(radius) << endl;
    return 0;
}
