public class First_circle_class extends First_Abstract_geometric_object{
    private double radius;

    public First_circle_class(){}

    public First_circle_class(double radius, String color, boolean filled) {
        super(color, filled);
        this.radius = radius;}

    public double getRadius() {
        return radius;}

    public void setRadius(double radius) {
        this.radius = radius;}

    public double getArea() {
        return radius * radius * Math.PI;}

    public double getDiameter() {
        return 2 * radius;}

    public double getPerimeter() {
        return 2 * radius * Math.PI;}

    public void printCircle() {
        System.out.println("The circle is created " + getDateCreated() + " and the radius is " + radius);}

}
