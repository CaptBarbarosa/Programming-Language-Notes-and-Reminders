public class First_Inheritence_Rectangle extends First_Inheritence_Geometric_Object{
    private double width;
    private double height;

    public First_Inheritence_Rectangle() {}

    public First_Inheritence_Rectangle(double width, double height) {
        this.width = width;
        this.height = height;}

    public First_Inheritence_Rectangle(double width, double height, String color, boolean filled) {
        this.width = width;
        this.height = height;
        super.setColor(color);
        super.setFilled(filled);}

    public double getWidth() {
        return width;}

    public void setWidth(double width) {
        this.width = width;}

    public double getHeight() {
        return height;}

    public void setHeight(double height) {
        this.height = height;}

    public double getArea() {
        return width * height;}

    public double getPerimeter() {
        return 2 * (width + height);}

    public void print_all_info(){
        System.out.println("Created at: " + super.getDateCreated() + "Width: "+ this.width + "\nHeight: "+ this.height +
                "\nColor:" + super.color + "\nIs filled: "+super.color);
    }

}
