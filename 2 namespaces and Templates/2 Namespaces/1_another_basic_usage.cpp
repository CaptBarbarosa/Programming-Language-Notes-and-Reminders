#include <iostream>
using namespace std;
namespace Square{
    double area(double r) {return r * r;}
    double perimeter(double r) {return 4 * r;}
}
using namespace Square;

int main() {
    double length;
    cout << "Enter length of the square: ";
    cin >> length;
    cout << "Area: " << Square::area(length) << endl;
    cout << "Perimeter: " << perimeter(length) << endl;
    return 0;
}
