public class Second_interface_implementation implements Second_interface_eat, Second_interface_sound{
    private String eats;
    private String sound;
    Second_interface_implementation(){}
    @Override
    public void eat(String eats) {
        this.eats = eats;}

    @Override
    public void sound(String sounds) {
        this.sound=sounds;}

    public void print(){
        System.out.println("Sounds: "+ sound + " and eats: " + eats);
    }
}
