public class Second_Main {
    public static void main(String[] args) {
        Second_interface_implementation dog = new Second_interface_implementation();
        dog.eat("Meat");
        dog.sound("Woof");
        Second_interface_implementation cat = new Second_interface_implementation();
        cat.eat("Meat");
        cat.sound("Meow");

        dog.print();
        cat.print();
    }
}
