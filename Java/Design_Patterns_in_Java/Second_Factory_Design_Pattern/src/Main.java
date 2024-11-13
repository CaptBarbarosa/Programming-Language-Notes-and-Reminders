public class Main {
    public static void main(String[] args) {
        First_Simple_Factory_Pattern_Implementation_Notification_Factory factory = new First_Simple_Factory_Pattern_Implementation_Notification_Factory();

        // Client code only knows about the Notification interface
        First_Simple_Factory_Pattern_Implementation_interface notification = factory.createNotification("email");
        notification.notifyUser();  // Output: Sending an email notification
        System.out.println(notification instanceof First_Simple_Factory_Pattern_Implementation_interface);
        System.out.println(notification instanceof First_Simple_Factory_Pattern_Implementation_Email_Notification);
        System.out.println(notification instanceof First_Simple_Factory_Pattern_Implementation_SMS_Notification);


        First_Simple_Factory_Pattern_Implementation_interface smsNotification = factory.createNotification("sms");
        smsNotification.notifyUser();  // Output: Sending an SMS notification
    }
}