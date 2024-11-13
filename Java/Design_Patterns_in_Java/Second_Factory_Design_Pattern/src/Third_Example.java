// Step 1: Define the Product Interface
interface Dish {
    void prepare();
    void serve();
}

// Step 2: Create Concrete Products
class Pizza implements Dish {
    @Override
    public void prepare() {
        System.out.println("Preparing pizza...");
    }

    @Override
    public void serve() {
        System.out.println("Serving pizza...");
    }
}

class Sushi implements Dish {
    @Override
    public void prepare() {
        System.out.println("Preparing sushi...");
    }

    @Override
    public void serve() {
        System.out.println("Serving sushi...");
    }
}

// Step 3: Define the Factory Interface
interface DishFactory {
    Dish createDish();
}

// Step 4: Create Concrete Factories
class PizzaFactory implements DishFactory {
    @Override
    public Dish createDish() {
        return new Pizza();
    }
}

class SushiFactory implements DishFactory {
    @Override
    public Dish createDish() {
        return new Sushi();
    }
}

// Step 5: Client Code
public class Third_Example {
    public static void main(String[] args) {
        // Order a pizza using the PizzaFactory
        DishFactory pizzaFactory = new PizzaFactory();
        Dish pizza = pizzaFactory.createDish();
        pizza.prepare();
        pizza.serve();

        // Order sushi using the SushiFactory
        DishFactory sushiFactory = new SushiFactory();
        Dish sushi = sushiFactory.createDish();
        sushi.prepare();
        sushi.serve();
    }
}
