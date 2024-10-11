public class Main {
    public static void main(String[] args) {
        ACircle circle = new ACircle(5.0);
        double area = circle.getArea();
        System.out.println("The area of the circle with radius 5 is: " + area);
        ACircle second_circle = new ACircle();
        System.out.println("From circle object the number of circle object are: "+ circle.getNumberOfObjects()+"\nFrom " +
                "the second_circle object the number of circle object are: "+ second_circle.getNumberOfObjects() +
                "\nFrom the general main the number of circle object are: " + ACircle.getNumberOfObjects()
                //It is a better practice to reach static via class reference
        );

        String str1, str2;
        str1 = "Free the bound periodicals.";
        String str4= new String("Free the bound periodicals.");
        System.out.println("String1: " + str1);
        System.out.println("String2: " + str4);
        System.out.println("Same object? " + (str1 == str4)); //To compare strings use .equals method.
        System.out.println("Same value? " + str1.equals(str4));
    }
}