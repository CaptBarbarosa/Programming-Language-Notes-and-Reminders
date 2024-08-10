#ifndef OPERATOROVERLOADING_HEADER_H
#define OPERATOROVERLOADING_HEADER_H

#include<iostream>
using namespace std;

class Alpha {
private:
    int dataAlpha;
public:
    Alpha(int);
    void invert();                  // Renamed from negate to invert()
    void increment();               // Renamed operator++ to increment()
    void incrementPostfix(int);     // Renamed operator++(int) to incrementPostfix()
    Alpha add(Alpha other);         // Renamed operator+ to add()
    void assign(Alpha other);       // Renamed operator= to assign()
    void addAssign(Alpha other);    // Renamed operator+= to addAssign()
    void update(int a = 5, int b = 10, int c = 5); // Renamed operator() to update()
    void update(double x);          // Same here for double
};

class Beta {
private:
    int dataBeta;
public:
    Beta(int);
    friend void invert(Beta);                // Renamed from negate to invert()
    friend void increment(Beta&);            // Renamed operator++ to increment()
    friend void incrementPostfix(Beta&,int); // Renamed operator++(int) to incrementPostfix()
    friend Beta add(Beta b1, Beta b2);       // Renamed operator+ to add()
    void assign(Beta &other);                // Renamed operator= to assign()
    friend void addAssign(Beta &b1, Beta b2);// Renamed operator+= to addAssign()
};

#endif

