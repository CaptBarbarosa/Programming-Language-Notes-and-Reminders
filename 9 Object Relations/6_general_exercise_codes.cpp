#include "6_general_exercise_header.h"

Salary::Salary(){
    this-> base = 0;
    this-> bonus = 0;
}

Salary::Salary(int base, int bonus){
    this-> base = base;
    this-> bonus = bonus;
}

void Salary:: set_base(int base){
    this-> base = base;
}

int Salary:: get_base(void){
    return this-> base;
}

void Salary:: set_bonus(int bonus){
    this-> bonus = bonus;
}

int Salary:: get_bonus(void){
    return this-> bonus;
}

CompositeEmployee:: CompositeEmployee (int base, int bonus)/*:my_salary(base, bonus)*/{
    //this->my_salary(base, bonus); // Fails because the salary is already constructed until it comes here.
    //Either do the ones below or comment the below and uncomment the my_salary(base, bonus) at the top
    my_salary.set_base(base);
    my_salary.set_bonus(bonus);
}

int CompositeEmployee::get_salary(void){
    return my_salary.get_base() + my_salary.get_bonus();
}


