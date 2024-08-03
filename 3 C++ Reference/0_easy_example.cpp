#include <iostream>
using namespace std;


int main(){
    int a=5, &b=a, c=10;
    b=c;
    cout<<"B: "<<b<<" C:"<<c<<"\n";
    b=11;
    cout<<"B: "<<b<<" C:"<<c<<"\n";
    return 0;
}

