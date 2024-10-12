public class Third_Casting_and_Hiding_graduate extends Third_Casting_and_Hiding_student{
    private int donation;


    /*-----------------------------------------------------------------*/
    public Third_Casting_and_Hiding_graduate(int year, String department, String blood_type, boolean gender, int age, int donation) {
        super(year, department, blood_type, gender, age);
        this.donation = donation;
        System.out.println("In the grad specific constructor");

    }
    public int getDonation() {
        return donation;}
    public void setDonation(int donation) {
        this.donation = donation;}
    public static void hide_this(){
        System.out.println("Nothing to see here.");
    }
}
