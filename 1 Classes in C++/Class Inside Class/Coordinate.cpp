#include "Coordinate.h"
#include <iostream>

Coordinate::Coordinate(){
    x = 0;
    y = 0;
}

void Coordinate :: set_coordinates(int x, int y){
    this->x = x;
    this->y = y;
}

int Coordinate :: get_x (void){
    return this->x;
}

int Coordinate :: get_y (void){
    return this->y;
}

