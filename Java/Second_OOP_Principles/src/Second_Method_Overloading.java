public class Second_Method_Overloading {
    public int add(int a, int b) {
        return a + b;}

    public double add(double a, double b) {
        return a + b;}

    public static void main(String[] args) {
        Second_Method_Overloading calc = new Second_Method_Overloading();
        System.out.println(calc.add(5, 10));       // Calls add(int, int)
        System.out.println(calc.add(5.0, 10.0));   // Calls add(double, double)
    }


}
