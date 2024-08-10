#include"2_operator_overload_header.h"

void invert(Beta b) {
    cout << "Beta value:" << b.dataBeta << endl;
}

void increment(Beta& b){
    b.dataBeta++;
}

void incrementPostfix(Beta& b, int){
    b.dataBeta++;
}

Beta add(Beta b1, Beta b2){
    Beta temp(0);
    temp.dataBeta = b1.dataBeta + b2.dataBeta;
    return temp;
}

void addAssign(Beta &b1, Beta b2){
    b1.dataBeta = b1.dataBeta + b2.dataBeta;
}

int main(){
    Alpha alpha1(10), alpha2(20);
    Beta beta1(10), beta2(20);

    Alpha alpha3 = alpha1.add(alpha2);
    Beta beta3 = add(beta1, beta2);

    alpha3.invert();
    invert(beta3);

    Alpha alpha4(10);
    alpha4.update(20);
    alpha4.invert();

    alpha4.update(10, 10);
    alpha4.invert();

    alpha4.update(3.14);
    alpha4.invert();

    return 0;
}

