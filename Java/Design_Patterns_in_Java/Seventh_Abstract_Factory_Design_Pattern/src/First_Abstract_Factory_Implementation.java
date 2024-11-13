// 1. Abstract Product Interfaces
interface Button {
    void paint();
}

interface Checkbox {
    void render();
}

// 2. Concrete Products for Windows
class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering Windows button.");
    }
}

class WindowsCheckbox implements Checkbox {
    @Override
    public void render() {
        System.out.println("Rendering Windows checkbox.");
    }
}

// 3. Concrete Products for MacOS
class MacOSButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering MacOS button.");
    }
}

class MacOSCheckbox implements Checkbox {
    @Override
    public void render() {
        System.out.println("Rendering MacOS checkbox.");
    }
}

// 4. Abstract Factory
interface UIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// 5. Concrete Factory for Windows
class WindowsFactory implements UIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

// 6. Concrete Factory for MacOS
class MacOSFactory implements UIFactory {
    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}

// 7. Client Code
class Application {
    private Button button;
    private Checkbox checkbox;

    public Application(UIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }

    public void renderUI() {
        button.paint();
        checkbox.render();
    }
}

// Main class to demonstrate
public class First_Abstract_Factory_Implementation  {
    public static void main(String[] args) {
        UIFactory factory;
        
        // Here we could dynamically choose a factory based on configuration or environment.
        String osType = "Windows"; // this could be fetched dynamically in a real app

        if (osType.equals("Windows")) {
            factory = new WindowsFactory();
        } else {
            factory = new MacOSFactory();
        }

        Application app = new Application(factory);
        app.renderUI();
    }
}
