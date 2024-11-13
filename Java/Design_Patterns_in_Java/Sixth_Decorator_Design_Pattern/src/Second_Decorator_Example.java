// Step 1: Define the Message interface
interface Message {
    String getContent();
}

// Step 2: Implement two concrete classes, PlainTextMessage and HTMLMessage
class PlainTextMessage implements Message {
    private String text;

    public PlainTextMessage(String text) {
        this.text = text;
    }

    @Override
    public String getContent() {
        System.out.println("In the plaintext");
        return text;
    }
}

class HTMLMessage implements Message {
    private String htmlContent;

    public HTMLMessage(String htmlContent) {
        this.htmlContent = "<html><body>" + htmlContent + "</body></html>";
    }

    @Override
    public String getContent() {
        System.out.println("In the HTMLMessage");
        return htmlContent;
    }
}

// Step 3: Implement a real decorator, EncryptionDecorator, that wraps a Message and "encrypts" it
class EncryptionDecorator implements Message {
    private Message message;

    public EncryptionDecorator(Message message) {
        this.message = message;
    }

    @Override
    public String getContent() {
        System.out.println("In the EncryptionDecorator");
        return encrypt(message.getContent());
    }

    // A simple "encryption" by reversing the string (for demonstration purposes)
    private String encrypt(String content) {
        return new StringBuilder(content).reverse().toString();
    }
}

// Step 4: Demonstrate how the decorator wraps the concrete message classes
public class Second_Decorator_Example{
    public static void main(String[] args) {
        // Plain Text Message without encryption
        Message plainMessage = new PlainTextMessage("Hello, World!");
        System.out.println("Plain Message: " + plainMessage.getContent());

        System.out.println("--->Back in main 1");
        // HTML Message without encryption
        Message htmlMessage = new HTMLMessage("Hello, World!");
        System.out.println("HTML Message: " + htmlMessage.getContent());

        System.out.println("--->Back in main 2");
        // Plain Text Message with encryption
        Message encryptedPlainMessage = new EncryptionDecorator(plainMessage);
        System.out.println("Encrypted Plain Message: " + encryptedPlainMessage.getContent());

        System.out.println("--->Back in main 3");
        // HTML Message with encryption
        Message encryptedHtmlMessage = new EncryptionDecorator(htmlMessage);
        System.out.println("Encrypted HTML Message: " + encryptedHtmlMessage.getContent());
    }
}
