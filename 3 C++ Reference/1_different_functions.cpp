#include <iostream>
using namespace std;

int *fun1(int *y){
    (*y)++;
    return y;
}

int &fun2(int &x){
    x++;
    return x;
}

int &func3(){
    static int a = 1, &b = a; //Without static keyword this would lead undefined behavior
    //Because when defined with static keyword, the variable gets created once and retains its value between function calls. And destroyed when the program terminates.
    return b;
}



int main(){
    int x = 5;
    int *y = fun1(&x);
    std::cout<<"*Y: "<< *y;
    int &z = x;
    int &j = fun2(z);
    std::cout<<"\nZ:"<<z << " X:"<< x<< " J:"<<j <<"\n";
    int &a = func3();
    std::cout<< "A:"<<a <<"\n";
    return 0;
}

