#include <iostream> 
#include "time.h" 
 
using std::cout; 
 
Time::Time() { 
    hour = 0;
    minute = 0;
    second = 0; 
} 
void Time::set_time(int h, int m, int s) { 
    hour = h;
    minute = m;
    second = s; 
} 

void Time::print_time(void){
    cout << ((hour < 10) ? "0" : "") << hour << ":";
    cout << ((minute < 10) ? "0" : "") << minute << ":";
    cout << ((second < 10) ? "0" : "") << second << "\n"; 
}
