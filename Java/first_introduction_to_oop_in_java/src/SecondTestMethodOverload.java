public class SecondTestMethodOverload {

    public static void main(String[] args){
        System.out.println("\n->The maximum between 3 and 4 is " + max(3, 4));
        System.out.println("\n-->The maximum between 3.0 and 5.4 is " + max(3.0, 5.4));
        System.out.println("\n--->The maximum between 3.0, 5.4, and 10.14 is " + max(3.0, 5.4, 10.14));
        /*
            Output of the last println is last, second and second because it first goes to last.
            Then it goes to second twice. Once for max(3.0, 5.4) and once for (5.4, 10.14).
        */
    }

    public static int max(int num1, int num2) {
        System.out.println("first");
        return Math.max(num1, num2);
    }

    public static double max(double num1, double num2) {
        System.out.println("second");
        return Math.max(num1, num2);
    }

    /** Return the max among three double values */
    public static double max(double num1, double num2, double num3) {
        System.out.println("last");
        return max(max(num1, num2), num3);
    }
}
