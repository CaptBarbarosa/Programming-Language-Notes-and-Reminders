#include"2_operator_overload_header.h"

Alpha::Alpha(int n) { this->dataAlpha = n; }

void Alpha::invert(){
    cout << "Alpha value:" << this->dataAlpha << endl;
}

void Alpha::increment(){
    this->dataAlpha++;
}

void Alpha::incrementPostfix(int){
    this->dataAlpha++;
}

Alpha Alpha::add(Alpha other){
    Alpha temp(0);
    temp.dataAlpha = this->dataAlpha + other.dataAlpha;
    return temp;
}

void Alpha::assign(Alpha other){
    this->dataAlpha = other.dataAlpha;
}

void Alpha::addAssign(Alpha other){
    this->dataAlpha = this->dataAlpha + other.dataAlpha;
}

void Alpha::update(int a, int b, int c){
    this->dataAlpha = a + b + c;
}

void Alpha::update(double x){
    this->dataAlpha = x;
}

Beta::Beta(int n) { this->dataBeta = n; }

void Beta::assign(Beta &other){
    this->dataBeta = other.dataBeta;
}

