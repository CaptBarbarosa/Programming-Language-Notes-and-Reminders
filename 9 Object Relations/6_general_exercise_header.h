#ifndef GENERAL_EXERCISE
#define GENERAL_EXERCISE

class Salary{
    private:
        int base;
        int bonus;
    public:
        Salary();
        Salary(int , int);

        void set_base(int);
        int get_base(void);

        void set_bonus(int);
        int get_bonus(void);
};

class CompositeEmployee{
    private:
        Salary my_salary;
    public:
        CompositeEmployee(int,int);

        int get_salary(void);
};


#endif
