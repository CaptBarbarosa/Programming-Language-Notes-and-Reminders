public class ACircle {
    static int numberOfObjects = 0;
    double radius;

    public ACircle() {
        numberOfObjects ++;
        radius = 1.0;
    }

    public ACircle(double newRadius) {
        radius = newRadius;
        numberOfObjects ++;
    }

    public static int getNumberOfObjects() {
        return numberOfObjects;
    }

    public double getArea() {
        return radius * radius * Math.PI;
    }

    /*You need main to run the program*/
    /*
    public static void main(String[] args){
        ACircle circle = new ACircle(5.0);
        double area = circle.getArea();
        System.out.println("In the ACircle.java\nThe area of the circle with radius 5 is: " + area);
    }*/
}