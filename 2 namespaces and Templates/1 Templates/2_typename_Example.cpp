#include <iostream>
#include <string>
template <typename T>
class Box {
private:
    T value; 
public:
    Box(T value_given){
        value=value_given;
    }
    T getValue() const {
        return value;
    }
    void setValue(T val) {
        value = val;
    }
};
int main() {
    Box<int> intBox(123);
    std::cout << "Integer Box contains: " << intBox.getValue() << std::endl;

    Box<double> doubleBox(456.789);
    std::cout << "Double Box contains: " << doubleBox.getValue() << std::endl;

    Box<std::string> stringBox("Hello, Templates!");
    std::cout << "String Box contains: " << stringBox.getValue() << std::endl;

    intBox.setValue(999);
    std::cout << "Integer Box now contains: " << intBox.getValue() << std::endl;

    int a = 10;
    Box <int> b1(a);

    return 0;
}

