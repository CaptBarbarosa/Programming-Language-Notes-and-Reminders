#ifndef TIME_H
#define TIME_H

class Time{
    private:
        int hour;
        int minute;
        int second;
    public:
        Time(); // Constructor
        void set_time(int, int, int);
        void print_time();
};
#endif
