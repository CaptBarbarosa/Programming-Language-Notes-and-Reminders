#include <iostream>
#include "Coordinate.h"
#include "Line.h"

using namespace std;

int main(){
    int x, y;
    Line my_line;

    cout<< "Enter the x coordinate of the first coordinate: ";
    cin >>x;
    cout<< "Enter the y coordinate of the first coordinate: ";
    cin >>y;
    my_line.set_first_coordinate(x, y);

    cout<< "Enter the x coordinate of the second coordinate: ";
    cin >>x;
    cout<< "Enter the y coordinate of the second coordinate: ";
    cin >>y;
    my_line.set_second_coordinate(x, y);
    cout<<"Length of the line is: "<<my_line.calculate_length()<<"\n";
    return 0;
}


