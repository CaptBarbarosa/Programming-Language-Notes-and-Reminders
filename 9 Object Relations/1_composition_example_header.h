#ifndef COMPOSITION_EXAMPLE1
#define COMPOSITION_EXAMPLE1

class A{
    private:
        int a;
    public:
        A(int);
        int get_value(void);
};

class B{
private:
    int b;
public:
    B(int);
    int get_value(void);
};

class C{
private:
    A class_a;
    B class_b;
    int c;
public:
    C(int, int, int);
    int get_value(void);
};

#endif
