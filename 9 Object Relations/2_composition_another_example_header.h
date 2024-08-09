#ifndef COMPOSITION_2
#define COMPOSITION_2
#include <iostream>

class A{
private:
    int a;
public:
    A(int a_given){
        std::cout<<"IN the constructor\n";
        a = a_given;}

    int get_value(){
        return a;}

};

class B{
private:
    A obj;
    int b;
    A& a_ref;
public:
    B(int a_given, int b_given, A& a_refe):obj(a_given), b(b_given), a_ref(a_refe){}
    //Notice that it only enters constructer twice. One from the main and one from B's construction.

};

#endif
