public abstract class First_Abstract_geometric_object {
    private String color = "white";
    private boolean filled;
    private java.util.Date dateCreated;

    protected First_Abstract_geometric_object() {
        System.out.println("In the default constructor of abstract class");
        dateCreated = new java.util.Date();}

    protected First_Abstract_geometric_object(String color, boolean filled) {
        System.out.println("In the specific constructor of abstract class");
        dateCreated = new java.util.Date();
        this.color = color;
        this.filled = filled;}

    public String getColor() {
        return color;}

    public void setColor(String color) {
        this.color = color;}

    public boolean isFilled() {
        return filled;}

    public void setFilled(boolean filled) {
        this.filled = filled;}

    public java.util.Date getDateCreated() {
        return dateCreated;}

    public String toString() {
        return "created on " + dateCreated + "\ncolor: " + color + " and filled: " + filled;}

    //Abstract methods can only be in abstract classes.
    public abstract double getArea();

    public abstract double getPerimeter();
}
