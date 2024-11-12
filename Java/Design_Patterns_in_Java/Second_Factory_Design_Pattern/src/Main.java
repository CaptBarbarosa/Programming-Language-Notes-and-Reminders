public class Main {
    public static void main(String[] args) {
        First_Simple_Factory_Pattern_Implementation_Notification_Factory factory = new First_Simple_Factory_Pattern_Implementation_Notification_Factory();

        // Client code only knows about the Notification interface
        First_Simple_Factory_Pattern_Implementation_interface notification = factory.createNotification("email");
        notification.notifyUser();  // Output: Sending an email notification

        First_Simple_Factory_Pattern_Implementation_interface smsNotification = factory.createNotification("sms");
        smsNotification.notifyUser();  // Output: Sending an SMS notification
    }
}