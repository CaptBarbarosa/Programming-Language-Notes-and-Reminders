#include "1_composition_example_header.h"
    A::A(int a_given){
        a = a_given;}

    int A::get_value(void){
        return a;}

    B::B(int b_given){
        b = b_given;}

    int B::get_value(void){
        return b;}

    C::C(int a_given, int b_given, int c_given): class_a(a_given), class_b(b_given){
        c = c_given;}

    int C::get_value(void){
        return c;}

