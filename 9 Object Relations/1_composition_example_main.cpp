#include <iostream>
#include "1_composition_example_header.h"
using namespace std;

int main(){
    C class_c(1,2,3);
    cout << class_c.get_value()<< endl;
    return 0;
}
