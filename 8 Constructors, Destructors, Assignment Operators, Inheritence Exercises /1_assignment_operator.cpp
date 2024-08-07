#include <iostream>
#include <cstring>
using namespace std;


class Classroom{
    private:
        int number_of_seats;
        bool electronic_table_exists;
    public:
         Classroom(){ // Default constructor
             this-> number_of_seats = 40;
             this-> electronic_table_exists = true;
         }

         Classroom(int number_of_seats, bool electronic_table_exists){
             this-> number_of_seats = number_of_seats;
             this-> electronic_table_exists = electronic_table_exists;
         }

         void get_infos(){
             cout<<"Number of seats: "<< number_of_seats<< endl;
             cout<<"Electronic table exists: "<< electronic_table_exists<<endl;
         }

         Classroom& operator=(const Classroom& cls){
             cout<< "Entered the assignment operator\n"<<endl;
             if(this == &cls){
                 cout<< "Classroom& operator=(const CLassroom& cls) is called"<< endl;}
             this-> number_of_seats = cls.number_of_seats;
             this-> electronic_table_exists = cls.electronic_table_exists;
             return *this;
         }
};

int main(){
    Classroom first(50,false);
    Classroom second;
    second = first;
    second.get_infos();
    return 0;
}

