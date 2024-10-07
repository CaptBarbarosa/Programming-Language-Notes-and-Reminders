#include <iostream>
#include "3_composition_and_overloading_header.h"

int main() {
    Student s1("John Smith", 1);
    Student s2("Alan Iverson", 2);
    Student s3("John Jovi", 3);
    Course c1("CNG242");
    c1.registerer(s1);
    c1.registerer(s2);
    s3.enrol(c1);
    c1.listStudents();
    return 0;
}
