public class First_Simple_Factory_Pattern_Implementation_Notification_Factory {
    public First_Simple_Factory_Pattern_Implementation_interface createNotification(String type) {
        if ("email".equalsIgnoreCase(type)) {
            return new First_Simple_Factory_Pattern_Implementation_Email_Notification();
        } else if ("sms".equalsIgnoreCase(type)) {
            return new First_Simple_Factory_Pattern_Implementation_SMS_Notification();
        } else if ("push".equalsIgnoreCase(type)) {
            return new First_Simple_Factory_Pattern_Implementation_Push_Notification();
        } else {
            throw new IllegalArgumentException("Unknown notification type: " + type);
        }
    }
}
