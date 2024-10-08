#include <iostream>
#include <cstring>
#include "5_multiple_inheritence_example_header_and_codes.cpp"

int main(){
    //char *name = "John", *school_name = "METU";
    //int age = 25
    School my_school("METU", "Atilla", 1, 2, 3);
    my_school.print();
    return 0;
}


