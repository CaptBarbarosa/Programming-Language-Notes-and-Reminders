public class Fourth_Inner_Class_Main {
    public static void main(String [] args)
    {
        Fourth_Inner_Class_Exercise outerObject=new Fourth_Inner_Class_Exercise(10);
        Fourth_Inner_Class_Exercise.InnerClass innerObject= outerObject.new InnerClass();
        innerObject.print();

        Fourth_Inner_Class_Exercise.InnerStaticClass test = new Fourth_Inner_Class_Exercise.InnerStaticClass();
        test.print();
    }
}
