public class First_Inheritence_Circle extends First_Inheritence_Geometric_Object{
    private double radius;

    public First_Inheritence_Circle() {
        this.radius = 0;}

    public First_Inheritence_Circle(double radius) {
        this.radius = radius;}

    public First_Inheritence_Circle(double radius, String color, boolean filled){
        super(color, filled); //With the super we set the color of its super class.
        this.radius = radius;}

    public double getRadius() {
        return radius;}

    //Method overriding
    public void override_this() {
        System.out.println("\n\n-->In the Circle Object. You have override it.");}

    public void setRadius(double radius) {
        this.radius = radius;}

    public double getArea() {
        return radius * radius * Math.PI;}

    public double getDiameter() {
        return 2 * radius;}

    public double getPerimeter() {
        return 2 * radius * Math.PI;}

    //Note that from the inheriting class we can reach protected and public data.
    /*
    public void setColor(String color){
        this.color = color;}
    */

    public void printCircle() {
        System.out.println(toString() + "Created at: " + super.getDateCreated() + "\nRadius: " + radius +
                "\nColor: "+ super.color + "\nIs filled: "+super.isFilled());}

}
