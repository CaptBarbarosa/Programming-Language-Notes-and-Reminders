#include <iostream>
using namespace std;

class Shape{
protected:
    double width, height;
public:
    void setdims(double w, double h){
        width = w;
        height = h;
    }
};

class Rectangle: public Shape{
protected:
    double area;
public:
    void calculateArea(){
        area = width * height;
    }
};

class PaintCost: public Rectangle{
private:
    double cost;
    double totalcost;
public:
    void setCost(double c){
        cost = c;
    }
    void calculateTotal(){
        totalcost = cost * area;
    }
    void printTotalCost(){
        cout << "Total cost:" << totalcost;
    }
};

int main() {
    PaintCost p;
    p.setdims(5, 10);
    p.calculateArea();
    p.setCost(2);
    p.calculateTotal();
    p.printTotalCost();
    return 0;
}
