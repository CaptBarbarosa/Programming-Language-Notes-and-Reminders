#include "4_hiding_header.h"
#include <iostream>

A::A(int a_given){
    a = a_given;}

void A:: print(void){
    std::cout<<"Printing A\n";
}


B::B(int a_given, int b_given):A(a_given){
    b = b_given;}

void B:: print(void){
    std:: cout<< "Printing B\n";}

void B:: b_exclusive(void){
    std::cout << "Exclusive for B\n";
}
