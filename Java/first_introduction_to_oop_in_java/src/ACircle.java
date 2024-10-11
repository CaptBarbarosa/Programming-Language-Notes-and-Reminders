public class ACircle {
    double radius;

    public ACircle() {
        radius = 1.0;
    }

    public ACircle(double newRadius) {
        radius = newRadius;
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