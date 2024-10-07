#include <iostream> 
#include "time.h" 

using namespace std; 

int main(){ 
    Time mytime1;
    mytime1.set_time(13, 15, 10);
    mytime1.print_time();
    Time *mytime2 = new Time();
    mytime2->set_time(5, 13, 45);
    mytime2->print_time();
    delete mytime2; 
    return 0; 
} 
