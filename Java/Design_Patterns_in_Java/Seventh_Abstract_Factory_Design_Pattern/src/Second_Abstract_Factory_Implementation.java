// Second_Abstract_Factory_Implementation.java

public class Second_Abstract_Factory_Implementation {

    // Step 1: Concrete Product - Phone class
    public static class Phone {
        String description;
        public Phone(String model) {
            this.description = model;
        }
        public void getDescription() {
            System.out.println(this.description);
        }
    }

    // Step 2: Subfactories for different brands

    // Apple class for creating specific Apple phones
    public static class Apple {
        private Apple() {};
        public static Phone getPhone(String model) {
            if ("iphone14".equals(model)) 
                return new Phone("iPhone 14");
            else if ("iphone14 pro".equals(model)) 
                return new Phone("iPhone 14 Pro");
            else if ("iphone14 pro max".equals(model)) 
                return new Phone("iPhone 14 Pro Max");

            return new NullPhone();
        }
    }

    // Samsung class for creating specific Samsung phones
    public static class Samsung {
        private Samsung() {};
        public static Phone getPhone(String model) {
            if ("s23".equals(model)) 
                return new Phone("Samsung S23");
            else if ("s23 ultra".equals(model)) 
                return new Phone("Samsung S23 Ultra");

            return new NullPhone();
        }
    }

    // OnePlus class for creating specific OnePlus phones
    public static class OnePlus {
        private OnePlus() {};
        public static Phone getPhone(String model) {
            if ("onePlus7".equals(model)) 
                return new Phone("OnePlus 7");
            else if ("onePlus8".equals(model)) 
                return new Phone("OnePlus 8");

            return new NullPhone();
        }
    }

    // NullPhone class to handle unavailable phone models
    public static class NullPhone extends Phone {
        public NullPhone() {
            super("Invalid model");
        }
    }

    // Step 3: Super factory - PhoneStore class
    public static class PhoneStore {
        private PhoneStore() {}

        public static Phone getPhone(String brand, String model) {
            if ("Apple".equals(brand))
                return Apple.getPhone(model);
            else if ("OnePlus".equals(brand))
                return OnePlus.getPhone(model);
            else if ("Samsung".equals(brand))
                return Samsung.getPhone(model);

            return new NullPhone();
        }
    }

    // Step 4: Client code in the main method
    public static void main(String[] args) {
        Phone phone = PhoneStore.getPhone("Apple", "iphone14");
        phone.getDescription();

        System.out.println();

        Phone phone1 = PhoneStore.getPhone("Apple", "iphone13"); // This model doesn't exist
        phone1.getDescription();
    }
}
