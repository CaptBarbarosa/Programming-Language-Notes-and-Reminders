#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle{
    private:
        float length;
        float width;
        char fill_char;
        char perimeter_char;
    public:
        Rectangle();
        void set_length(float length);
        float get_length(void);

        void set_width(float width);
        float get_width(void);

        void set_fill_character(char character);
        void set_perimeter_character(char character);

        void draw(void);
};
#endif
