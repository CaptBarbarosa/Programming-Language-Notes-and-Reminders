#include "3_composition_and_overloading_header.h"
#include <string.h>
#include <iostream>
using namespace std;

Student::Student(const char *name, int stdno){
    this->name = new char[strlen(name) + 1];
    strcpy(this->name, name);
    this->stdno = stdno;
}

Student::Student(const Student &student){
    this->name = new char[strlen(student.name) + 1];
    strcpy(this->name, student.name);
    this->stdno = student.stdno;
}

void Student::operator=(const Student &student){
    delete [] this->name;
    this->name = new char[strlen(student.name) + 1];
    strcpy(this->name, student.name);
    this->stdno = student.stdno;
}

Student::~Student(){
    delete [] this->name;
}

void Student::enrol(Course &c) {
    if(c.numberofstudents == 20)
        cout << "Full";
    else
        c.students[c.numberofstudents++] = this;
}

ostream& operator<<(ostream &os, const Student &s){
    os << s.stdno << ", " << s.name << endl;
    return os;
}

Course::Course(const char *code){
    this->code = new char[strlen(code) + 1];
    strcpy(this->code, code);
    this->numberofstudents = 0;
    for(int i=0; i<20; i++){
        this->students[i] = NULL;
    }
}

Course::Course(const Course &course){
    this->code = new char[strlen(course.code) + 1];
    strcpy(this->code, course.code);
    this->numberofstudents = course.numberofstudents;
    for(int i=0; i<20; i++){
        this->students[i] = course.students[i];
    }
}

void Course::operator=(const Course &course){
    delete [] this->code;
    this->code = new char[strlen(course.code) + 1];
    strcpy(this->code, course.code);
    this->numberofstudents = course.numberofstudents;
    for(int i=0; i<20; i++){
        this->students[i] = course.students[i];
    }
}

Course::~Course(){
    delete [] this->code;
}

//To make it composition
/*Course::~Course(){
    delete [] this->code;
    for(int i=0; i<numberofstudents; i++){
        delete students[i];
    }
}*/

void Course::registerer(Student &s){
    if (this->numberofstudents == 20)
        cout << "Full";
    else
        students[numberofstudents++] = &s;
}

//To make it composition
/*void Course::registerer2(const char *name, int stdno) {
    if (this->numberofstudents == 20)
        cout << "Full";
    else
        students[numberofstudents++] = new Student(name, stdno);
}*/

void Course::listStudents(){
    cout << code << endl;
    for(int i=0; i<numberofstudents; i++){
        cout << *students[i];
    }
}
