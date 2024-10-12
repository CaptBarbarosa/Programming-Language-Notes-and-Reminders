public class Third_Casting_and_Hiding_student extends Third_Casting_and_Hiding_person {
    private int year = 0;
    private String department = null;

    /*-----------------------------------------------------------------*/

    public Third_Casting_and_Hiding_student(int year, String department, String blood_type, boolean gender, int age) {
        super(blood_type, gender, age);
        /*
        super.setBlood_type(blood_type);
        super.setGender(gender);
        super.setAge(age);
        */
        this.year = year;
        this.department = department;
        System.out.println("In the student specific constructor");
        }


    public int getYear() {
        return year;}
    public void setYear(int year) {
        this.year = year;}
    public String getDepartment() {
        return department;}
    public void setDepartment(String department) {
        this.department = department;}

    public static void hide_this(){
        System.out.println("What you looking at. I'm just a student.");
    }
}
