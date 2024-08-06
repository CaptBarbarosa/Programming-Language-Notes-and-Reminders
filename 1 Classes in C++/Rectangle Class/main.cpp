#include <iostream>
#include "Rectangle.h"
using namespace std;

int main(){
    Rectangle normal_rectangle;
    float length,width;
    char fill_char;
    char per_char;

    cout<<"Enter a length: ";
    cin >> length;
    normal_rectangle.set_length(length);

    cout<<"Enter a width: ";
    cin >> width;
    normal_rectangle.set_width(width);

    cout<<"Enter filling character: ";
    cin>>fill_char;
    normal_rectangle.set_fill_character(fill_char);

    cout<<"Enter perimeter character: ";
    cin>>per_char;
    normal_rectangle.set_perimeter_character(per_char);

    normal_rectangle.draw();
}
