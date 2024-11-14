
// Abstract class defining the template method
abstract class BeverageTemplate {

    // Template method, final so subclasses can't override
    public final void prepareRecipe() {
        boilWater();
        brew();
        pourInCup();
        if (addCondiments()) {
            addCondimentsToDrink();
        }
    }

    // Step 1: Boil water (common for all beverages)
    private void boilWater() {
        System.out.println("Boiling water");
    }

    // Step 2: Brew or steep (abstract method, to be implemented by subclasses)
    abstract void brew();

    // Step 3: Pour in cup (common for all beverages)
    private void pourInCup() {
        System.out.println("Pouring into cup");
    }

    // Step 4: Optionally add condiments
    boolean addCondiments() {
        return true; // Hook method, can be overridden to skip adding condiments
    }

    // Step 5: Adding condiments (abstract method, to be implemented by subclasses)
    abstract void addCondimentsToDrink();
}

// Concrete class for Tea
class Tea extends BeverageTemplate {

    @Override
    void brew() {
        System.out.println("Steeping the tea");
    }

    @Override
    void addCondimentsToDrink() {
        System.out.println("Adding lemon to tea");
    }

    @Override
    boolean addCondiments() {
        return true; // We add condiments to tea
    }
}

// Concrete class for Coffee
class Coffee extends BeverageTemplate {

    @Override
    void brew() {
        System.out.println("Brewing coffee grounds");
    }

    @Override
    void addCondimentsToDrink() {
        System.out.println("Adding sugar and milk to coffee");
    }

    @Override
    boolean addCondiments() {
        return true; // We add condiments to coffee
    }
}

// Main class to test the template pattern
public class First_Implementation_of_Template {
    public static void main(String[] args) {
        System.out.println("Preparing Tea...");
        BeverageTemplate tea = new Tea();
        tea.prepareRecipe();

        System.out.println("\nPreparing Coffee...");
        BeverageTemplate coffee = new Coffee();
        coffee.prepareRecipe();
    }
}

