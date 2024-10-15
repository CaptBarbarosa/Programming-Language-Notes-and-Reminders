public class Fourth_Inner_Class_Exercise{

    int x; //outer field

    Fourth_Inner_Class_Exercise(int x){
        this.x=x;
    }

    public class InnerClass{

        int y=2*x; //inner field

        void print(){
            System.out.println("y="+y);
        }
    }

    public static class InnerStaticClass{
        void print(){
            System.out.println("This is the static inner class");
        }
    }
}
