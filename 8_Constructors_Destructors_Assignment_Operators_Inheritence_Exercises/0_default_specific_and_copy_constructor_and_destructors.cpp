#include <iostream>
#include <cstring>
using namespace std;

class Classroom{
    private:
        char *classroom_name;
        int number_of_seats;
        bool electronic_table_exists;
    public:
         Classroom(){ // Default constructor
             this->classroom_name= new char[15];
             strcpy(this->classroom_name, "unspecified");
             this-> number_of_seats = 40;
             this-> electronic_table_exists = true;
         }

         Classroom(char *classroom_name, int number_of_seats, bool electronic_table_exists){ //Specified Constructors
             this->classroom_name= new char[strlen(classroom_name)+1];
             strcpy(this->classroom_name, classroom_name);
             this-> number_of_seats = number_of_seats;
             this-> electronic_table_exists = electronic_table_exists;
         }

         Classroom (const Classroom& clsr){ // Copy constructor
             classroom_name = new char[strlen(clsr.classroom_name)+1];
             strcpy(this->classroom_name,clsr.classroom_name);
             this-> number_of_seats = clsr.number_of_seats;
             this-> electronic_table_exists = clsr.electronic_table_exists;
         }

         void get_infos(){
             cout<<"Classroom name: "<< classroom_name<< endl;
             cout<<"Number of seats: "<< number_of_seats<< endl;
             cout<<"Electronic table exists: "<< electronic_table_exists<<endl;
         }
         ~Classroom(){
             cout<< "\n-->Entered the delete function for: "<<this->classroom_name<<endl;
             delete[] classroom_name;
         }
};

int main(){
    Classroom *default_class = new Classroom();
    default_class-> get_infos();
    delete default_class;

    Classroom *specified_class = new Classroom("Algorithms", 85, true);
    specified_class->get_infos();

    Classroom specified_class_2("Databases", 75, false);
    specified_class_2.get_infos();

    Classroom copy_constructor(specified_class_2);
    copy_constructor.get_infos();

    return 0;
}

