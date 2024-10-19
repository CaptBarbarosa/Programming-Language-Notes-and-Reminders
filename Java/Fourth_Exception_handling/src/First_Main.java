public class First_Main {
    public static void main(String[] args) {
        try {
        First_Class_Example c1 = new First_Class_Example(5);
        First_Class_Example c2 = new First_Class_Example(-5);
        First_Class_Example c3 = new First_Class_Example(0);
        }
    catch (IllegalArgumentException ex) {
      System.out.println(ex);
    }

    System.out.println("Number of objects created: " + First_Class_Example.getNumberOfObjects());
    }
}
