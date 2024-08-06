#include <iostream>
using namespace std;

void swap_ints(int &a, int &b){ //Notice that this wouldn't work on C.
    int temp=a;
    a=b;
    b=temp;
} // This function swaps the values of two integers.
//But the thing is, if we want to swap the values of 2 chars or strings we need to define new functions over and over again
//So, to deal with this we use templates.
//Templates are type safe and used mainly for code reusability. 
//They give you to chance to write a single function that works with all data types.

template <class T>
void swapp(T &x, T &y){
    T temp;
    temp = x;
    x = y;
    y=temp;
}



int main(){
    int a=1,b=2;
    swap_ints(a, b);
    std::cout <<"A: "<<a<<" B: "<<b<<"\n";
    char x = 'a', y = 'b';
    swap(x,y);
    std::cout<<"X: "<<x<<"\nY: "<<y<<"\n\n";
    return 0;
}

