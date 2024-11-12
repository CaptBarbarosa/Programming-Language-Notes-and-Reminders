public class first_singleton_example {
    // Private static instance of the Singleton class, initially set to null.
    private static first_singleton_example instance; // The static keyword makes it belong to the class and not the instance.

    // Private constructor prevents instantiation from other classes. VITAL FOR SINGLETON
    private first_singleton_example() {}

    // Public method to provide global access to the instance.
    public static first_singleton_example getInstance() {
        if (instance == null) {
            System.out.println("Creating for the first and only time");
            instance = new first_singleton_example();
        }
        return instance;
    }

    // Example method to demonstrate controlled access.
    public void showMessage() {
        System.out.println("Hello from the Singleton instance!");
    }
}

