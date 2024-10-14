import java.util.ArrayList;
import java.util.Random;

public class Third_Main {
    public static void main(String[]args){
        Third_imaginary_class my_ima = new Third_imaginary_class(3,5);
        Third_print_the_given<Third_imaginary_class> print_this = new Third_print_the_given<Third_imaginary_class>(my_ima);
        print_this.print();

        Third_print_the_given<Integer> print_this_2 = new Third_print_the_given<Integer>(12);
        print_this_2.print();
        ArrayList<Third_print_the_given> my_array = new ArrayList<>();
        int i, a, b;
        Random rand = new Random();

        for(i=0; i<10; i++){
            a= rand.nextInt(2);
            if( a == 1) {
                a = rand.nextInt(1000);
                b = rand.nextInt(1000);
                Third_imaginary_class imag_to_add = new Third_imaginary_class(a, b);
                Third_print_the_given <Third_imaginary_class>to_add = new Third_print_the_given<Third_imaginary_class>(imag_to_add);
                my_array.add(to_add);
            }
            else {
                a = rand.nextInt(10);
                Third_print_the_given <Integer>to_add = new Third_print_the_given<Integer>(a);
                my_array.add(to_add);
            }
        }
        for(i=0; i<10; i++){
            my_array.get(i).print();
        }
        //Without the <E extends Comparable<E>> you would have been able to compile and run this code
        //Even though you'd get an error.
        //Third_safe_generics.max("Welcome", 123);
    }
}
