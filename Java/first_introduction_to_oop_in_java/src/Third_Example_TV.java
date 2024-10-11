public class Third_Example_TV {
    //We set the default values.
    int channel = 1;
    int volumeLevel = 1;
    boolean on = false;

    public void turnOn() {
        on = true;}
    public void turnOff() {
        on = false;}
    public void setVolume(int newVolumeLevel) {
        if (on && newVolumeLevel >= 1 && newVolumeLevel <= 7)
            volumeLevel = newVolumeLevel;}
    public void channelUp() {
        if (on && channel < 120)
            channel++;}
    public void channelDown() {
        if (on && channel > 1)
            channel--;}
    public void volumeUp() {
        if (on && volumeLevel < 7)
            volumeLevel++;}
    public void volumeDown() {
        if (on && volumeLevel > 1)
            volumeLevel--;}

    public static void main(String[] args) {
        Third_Example_TV tv1 = new Third_Example_TV();
        tv1.channel=30;
        tv1.turnOn();
        tv1.setVolume(3);

        Third_Example_TV tv2 = new Third_Example_TV();
        tv2.turnOn();
        tv2.channelUp();
        tv2.channelUp();
        tv2.volumeUp();

        System.out.println("tv1's channel is " + tv1.channel + " and volume level is " + tv1.volumeLevel);
        System.out.println("tv2's channel is " + tv2.channel + " and volume level is " + tv2.volumeLevel);
    }
}
