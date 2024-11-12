// Subsystem 1: Product Inventory
class ProductInventory {
    public boolean checkAvailability(String productId) {
        // Assume it checks product availability in the inventory
        System.out.println("Checking availability for product ID: " + productId);
        return true;
    }
}

// Subsystem 2: Authentication
class Authentication {
    public boolean authenticateUser(String userId) {
        // Assume it authenticates the user
        System.out.println("Authenticating user ID: " + userId);
        return true;
    }
}

// Subsystem 3: Payment Processing
class PaymentProcessor {
    public boolean processPayment(String paymentDetails) {
        // Assume it processes the payment
        System.out.println("Processing payment with details: " + paymentDetails);
        return true;
    }
}

// Subsystem 4: Order Fulfillment
class OrderFulfillment {
    public void fulfillOrder(String productId, String userId) {
        // Assume it fulfills the order
        System.out.println("Fulfilling order for product ID: " + productId + " for user ID: " + userId);
    }
}

// Facade: eCommerceFacade
class eCommerceFacade {
    private ProductInventory inventory;
    private Authentication auth;
    private PaymentProcessor payment;
    private OrderFulfillment fulfillment;

    public eCommerceFacade() {
        this.inventory = new ProductInventory();
        this.auth = new Authentication();
        this.payment = new PaymentProcessor();
        this.fulfillment = new OrderFulfillment();
    }

    public void placeOrder(String productId, String userId, String paymentDetails) {
        System.out.println("Starting order placement process...");
        
        if (!auth.authenticateUser(userId)) {
            System.out.println("Authentication failed for user ID: " + userId);
            return;
        }
        
        if (!inventory.checkAvailability(productId)) {
            System.out.println("Product with ID " + productId + " is not available in inventory.");
            return;
        }
        
        if (!payment.processPayment(paymentDetails)) {
            System.out.println("Payment processing failed.");
            return;
        }

        fulfillment.fulfillOrder(productId, userId);
        System.out.println("Order placed successfully for product ID: " + productId);
    }
}

// Client code
public class First_Facade_Pattern_Example {
    public static void main(String[] args) {
        // Facade object
        eCommerceFacade facade = new eCommerceFacade();

        // Client interacts only with the facade to place an order
        String productId = "12345";
        String userId = "user01";
        String paymentDetails = "Card Payment";
        
        facade.placeOrder(productId, userId, paymentDetails);
    }
}
