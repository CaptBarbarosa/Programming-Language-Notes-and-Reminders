#include <iostream>
using namespace std;

namespace MathFunctions{ // We use the namespace to package. Packaging grants us to reuse
    double add(double a, double b) {
        return a + b;
    }

    double multiply(double a, double b) {
        return a * b;
    }
}

int main() {
    using namespace MathFunctions;
    cout << "Addition: " << add(2.5, 3.0) << std::endl;
    cout << "Multiplication: " << multiply(2.5, 3.0) << std::endl;
    return 0;
}

