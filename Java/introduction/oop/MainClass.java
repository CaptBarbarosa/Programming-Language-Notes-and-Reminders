public class MainClass {
    public static void main(String[] args) {
        ACircle circle = new ACircle(5.0);
        double area = circle.getArea();
        System.out.println("The area of the circle with radius 5 is: " + area);
    }
}
