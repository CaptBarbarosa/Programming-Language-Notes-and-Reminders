#ifndef MULTIPLE_INHERITENCE_EXAMPLE
#define MULTIPLE_INHERITENCE_EXAMPLE

#include <iostream>
#include <cstring>
using namespace std;

class Person{
    protected:
        char *name;
        int age;
        bool gender;
    public:
        Person(){
            this->name = new char[10];
            strcpy(this->name, "Unknown");
            this->age = -1;}

        Person(const char *name, int age){
            this->name = new char [strlen(name) + 1];
            strcpy(this->name, name);
            this->age = age;}

        void set_name(const char *name){
            delete [] this->name;
            this->name = new char[strlen(name)+1];
            strcpy(this->name, name);}

        void set_age(int age){
            this->age = age;
        }
};

class Student: virtual public Person{ // Without virtual keyword, only one class could inherit
    protected:
        int student_id;
    public:
        Student(int student_id, const char *name, int age):Person(name, age){
            this->student_id = student_id;}
};

class Teacher: virtual public Person{
    protected:
        int ssn;
    public:
        Teacher(int ssn, const char *name, int age): Person(name, age){
            this->ssn = ssn;}
};

class School: public Student, public Teacher{
    private:
        char *school_name;
    public:
        School(const char *school_name, const char *name, int age, int student_id, int ssn): Person(name, age), Student(student_id, name, age), Teacher(ssn, name, age){
            this->school_name = new char [strlen(school_name)+1];
            strcpy(this->school_name, school_name);
        }
        void print(void){
            cout<<"Student ID: "<<this->student_id<<"\nSSN: "<< this->ssn<< "\nAge: "<<this->age<< "\n Name: "<<this->name<< endl;
        }
};
#endif
