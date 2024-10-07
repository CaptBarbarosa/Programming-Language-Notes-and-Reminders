//
// Created by Sukru Eraslan on 18.05.2023.
//

#ifndef COURSESTUDENT_COURSE_H
#define COURSESTUDENT_COURSE_H
#include <iostream>

using namespace std;
class Course;

class Student{
private:
    char *name;
    int stdno;

public:
    Student(const char *name, int stdno);
    Student(const Student &student);
    void operator=(const Student &student);
    ~Student();
    friend ostream& operator<<(ostream &os, const Student &s);
    void enrol(Course &c);
};

class Course{
private:
    char *code;
    int numberofstudents;
    Student *students[20];
public:
    Course(const char *code);
    Course(const Course &course);
    void operator=(const Course &course);
    ~Course();
    void registerer(Student &s);
    //void registerer2(const char* name, int stdno);
    void listStudents();
    friend void Student::enrol(Course &c); // We allowed the Student class to reach this.
};
#endif
