#ifndef COORDINATE_H
#define COORDINATE_H
class Coordinate{
    private:
        int x;
        int y;
    public:
        Coordinate();
        void set_coordinates(int x, int y);
        int get_x(void);
        int get_y(void);
};
#endif
