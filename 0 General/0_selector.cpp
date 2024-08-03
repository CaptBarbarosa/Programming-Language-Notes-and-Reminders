#include <iostream>
using namespace std;

int &my_func(int &x){
    return x;
}

int main(){
    int a=3, b= my_func(a);
    my_func(a)=0;
    std::cout<<"a: "<<a<<" b: "<<b<<"\n";
    return 0;
}
