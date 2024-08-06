#include <cmath>
#include <iostream>
#include "Line.h"

Line :: Line() {}

void Line :: set_first_coordinate(int x, int y){
    this->c1.set_coordinates(x, y);
}

void Line :: set_second_coordinate(int x, int y){
    this->c2.set_coordinates(x, y);
}

float Line :: calculate_length(void){
    float length = sqrt((((float) this->c1.get_x() - (float) this->c2.get_x()) * ((float) this->c1.get_x() - (float) this->c2.get_x())) + (((float) this->c1.get_y() - (float) this->c2.get_y()) * ((float) this->c1.get_y() - (float) this->c2.get_y())));
    return length;
}
