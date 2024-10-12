public class Main {
    public static void main(String[] args) {
        First_Inheritence_Rectangle my_rect = new First_Inheritence_Rectangle(5, 6, "White", false);
        System.out.println(my_rect.getArea());
        my_rect.print_all_info();

        First_Inheritence_Circle my_circ = new First_Inheritence_Circle();

        // The class inherits the public and private classes as well.
        my_circ.setColor("Blue");
        my_circ.setFilled(true);
        my_circ.printCircle();
        my_circ.override_this();
    }
}