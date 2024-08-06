#include <iostream>
using namespace std;

int divide(int a, int b){
    if (b == 0){
        throw "Can't divide by zero\n";
    }
    return a/b;
}

int main(){
    int a, b;
    cout<< "Enter a and b: ";
    cin>>a;
    cin>>b;
    try{
        int res = divide (a, b);
        cout<< "Result is: "<< res;}
    catch(const char *msg){
        cerr<< msg;
    }
}
