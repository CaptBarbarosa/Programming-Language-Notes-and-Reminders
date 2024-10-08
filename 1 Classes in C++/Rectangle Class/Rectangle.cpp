#include <iostream>
#include "Rectangle.h"
Rectangle::Rectangle(){
    fill_char = '-';
    perimeter_char = '*';
    length = 1;
    width = 1;
}
void Rectangle::set_length(float length) {
    if(length < 0 || length > 20){
        throw std::out_of_range("Width must be between 0 and 20");}
    this->length = length;
}
float Rectangle::get_length(void){
    return length;
}
void Rectangle::set_width(float width){
    if(width < 0 || width > 20){
        throw std::out_of_range("Width must be between 0 and 20");}
    this->width = width;
}
float Rectangle::get_width(void){
    return width;
}

void Rectangle::set_fill_character(char character){
    fill_char = character;
}

void Rectangle::set_perimeter_character(char character){
    perimeter_char = character;
}

void Rectangle:: draw(void){
    int row, column;
    for(row = 0; row<width; row++){
        for(column = 0; column < length; column ++){
            if(row == 0 || row == width-1 || column == 0 || column == length-1){
                std::cout<<perimeter_char;
            }
            else{
                std::cout<<fill_char;
            }
        }
        std::cout<<"\n";
    }
}





