public class Third_Main {
    public static void main(String []args){
        Third_Casting_and_Hiding_graduate my_grad = new Third_Casting_and_Hiding_graduate(2001, "CNG", "AB+", true, 40, 10000);
        Third_Casting_and_Hiding_student first_student = new Third_Casting_and_Hiding_student(2005, "EEE", "A0+", true, 35);
        my_grad.hide_this();
        first_student.hide_this();
        Third_Casting_and_Hiding_student second_student = (Third_Casting_and_Hiding_student)my_grad;
    }
}
