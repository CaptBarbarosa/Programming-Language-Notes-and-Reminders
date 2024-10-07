#ifndef HIDING
#define HIDING
class A{
    private:
        int a;
    public:
        A(int a);
        virtual void print(void);
};

class B: public A{
    private:
        int b;
    public:
        B(int, int);
        void print(void);
        void b_exclusive(void);
};

#endif
