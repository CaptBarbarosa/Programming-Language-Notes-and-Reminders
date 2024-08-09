#include <iostream>
#include "2_composition_another_example_header.h"

int main() {
    A my_class_a(1);
    A &class_ref = my_class_a;
    B my_class_b(1, 2, class_ref);
    return 0;
}
