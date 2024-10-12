public class Third_Casting_and_Hiding_person {
    private String blood_type;
    private boolean gender;
    private int age;

    /*-------------------------------------------------------------------*/
    public Third_Casting_and_Hiding_person(){
        System.out.println("In the person default constructor");
        this.blood_type="None";
        this.gender=false;
        this.age= 0;
    }
    public Third_Casting_and_Hiding_person(String blood_type, boolean gender, int age) {
        System.out.println("In the person specific constructor");
        this.blood_type = blood_type;
        this.gender = gender;
        this.age = age;
    }
    public String getBlood_type() {
        return blood_type;}
    public void setBlood_type(String blood_type) {
        this.blood_type = blood_type;}
    public boolean isGender() {
        return gender;}
    public void setGender(boolean gender) {
        this.gender = gender;}
    public int getAge() {
        return age;}
    public void setAge(int age) {
        this.age = age;}

    public static void hide_this(){
        System.out.println("Cops are looking for me maan. Hide me for gods sake.");
    }

}
