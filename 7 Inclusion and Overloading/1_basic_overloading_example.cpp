#include <iostream>
using namespace std;

void divide(int a, int b){
    cout << "At the first func"<< endl;
    cout << a<<"/"<<b<<": "<<a/b<< endl;
}

void divide(double a, double b){
    cout<< "At the second func"<< endl;
    cout << a<< "/"<< b<< ": "<< a/b<< endl;
}


int main(){
    divide(8,2);
    divide(5.2,2.5);
    return 0;
}

