// Step 1: Define the Component interface
interface CoffeeComponent {
    String getDescription();
    double getCost();
}

// Step 2: Implement the ConcreteComponent class
class BasicCoffee implements CoffeeComponent {
    @Override
    public String getDescription() {
        return "Basic Coffee";
    }

    @Override
    public double getCost() {
        return 5.0;
    }
}

// Step 3: Create the abstract Decorator class
abstract class CoffeeDecorator implements CoffeeComponent {
    protected CoffeeComponent coffeeComponent;

    public CoffeeDecorator(CoffeeComponent coffeeComponent) {
        this.coffeeComponent = coffeeComponent;
    }

    @Override
    public String getDescription() {
        return coffeeComponent.getDescription();
    }

    @Override
    public double getCost() {
        return coffeeComponent.getCost();
    }
}

// Step 4: Create ConcreteDecorator classes
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(CoffeeComponent coffeeComponent) {
        super(coffeeComponent);
    }

    @Override
    public String getDescription() {
        return coffeeComponent.getDescription() + ", Milk";
    }

    @Override
    public double getCost() {
        return coffeeComponent.getCost() + 1.5;
    }
}

class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(CoffeeComponent coffeeComponent) {
        super(coffeeComponent);
    }

    @Override
    public String getDescription() {
        return coffeeComponent.getDescription() + ", Sugar";
    }

    @Override
    public double getCost() {
        return coffeeComponent.getCost() + 0.5;
    }
}

class VanillaDecorator extends CoffeeDecorator {
    public VanillaDecorator(CoffeeComponent coffeeComponent) {
        super(coffeeComponent);
    }

    @Override
    public String getDescription() {
        return coffeeComponent.getDescription() + ", Vanilla";
    }

    @Override
    public double getCost() {
        return coffeeComponent.getCost() + 2.0;
    }
}

// Step 5: Demonstrate the Decorator Pattern
public class First_Decorator_Example {
    public static void main(String[] args) {
        CoffeeComponent basicCoffee = new BasicCoffee();
        System.out.println(basicCoffee.getDescription() + " -> $" + basicCoffee.getCost());

        CoffeeComponent milkCoffee = new MilkDecorator(basicCoffee);
        System.out.println(milkCoffee.getDescription() + " -> $" + milkCoffee.getCost());

        CoffeeComponent milkSugarCoffee = new SugarDecorator(milkCoffee);
        System.out.println(milkSugarCoffee.getDescription() + " -> $" + milkSugarCoffee.getCost());

        CoffeeComponent deluxeCoffee = new VanillaDecorator(milkSugarCoffee);
        System.out.println(deluxeCoffee.getDescription() + " -> $" + deluxeCoffee.getCost());
    }
}
