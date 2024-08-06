#ifndef LINE_H
#define LINE_H
#include "Coordinate.h"

class Line{
    private:
        Coordinate c1;
        Coordinate c2;
    public:
        Line();
        void set_first_coordinate(int x, int y);
        void set_second_coordinate(int x, int y);
        float calculate_length();
};

#endif
