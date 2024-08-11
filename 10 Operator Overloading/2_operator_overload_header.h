#ifndef OPERATOROVERLOADING_HEADER_H
#define OPERATOROVERLOADING_HEADER_H

#include<iostream>
using namespace std;

class Alpha {
private:
    int dataAlpha;
public:
    Alpha(int);
    void invert();
    void increment();
    void incrementPostfix(int);
    Alpha add(Alpha other);
    void assign(Alpha other);
    void addAssign(Alpha other);
    void update(int a = 5, int b = 10, int c = 5);
    void update(double x);
};

class Beta {
private:
    int dataBeta;
public:
    Beta(int);
    friend void invert(Beta);
    friend void increment(Beta&);
    friend void incrementPostfix(Beta&,int);
    friend Beta add(Beta b1, Beta b2);
    void assign(Beta &other);
    friend void addAssign(Beta &b1, Beta b2);
};

#endif

