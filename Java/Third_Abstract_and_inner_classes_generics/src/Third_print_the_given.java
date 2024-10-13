public class Third_print_the_given <T> {
    T thing_To_Print;
    public Third_print_the_given(T thing_To_Print){
        this.thing_To_Print=thing_To_Print;}
    public void print(){
        if(thing_To_Print instanceof Third_imaginary_class){
            System.out.println("What is given is imaginary number. A: " + ((Third_imaginary_class) thing_To_Print).getA() +
                    " and b: "+((Third_imaginary_class) thing_To_Print).getB());
        }
        else{
            System.out.println("What is given is not imaginary. It is: "+thing_To_Print);
        }
    }
}

