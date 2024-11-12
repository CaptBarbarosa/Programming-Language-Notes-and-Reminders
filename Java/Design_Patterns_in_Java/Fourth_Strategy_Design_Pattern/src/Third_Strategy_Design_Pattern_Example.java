import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

// Strategy interface
interface SortStrategy {
    void sort(List<Product> products);
}

// Concrete strategies for different sorting criteria
class SortBySize implements SortStrategy {
    @Override
    public void sort(List<Product> products) {
        products.sort(Comparator.comparing(Product::getSize));
        System.out.println("Sorted by size:");
        products.forEach(System.out::println);
    }
}

class SortByColor implements SortStrategy {
    @Override
    public void sort(List<Product> products) {
        products.sort(Comparator.comparing(Product::getColor));
        System.out.println("Sorted by color:");
        products.forEach(System.out::println);
    }
}

class SortByPrice implements SortStrategy {
    @Override
    public void sort(List<Product> products) {
        products.sort(Comparator.comparing(Product::getPrice));
        System.out.println("Sorted by price:");
        products.forEach(System.out::println);
    }
}

// Product class with properties for size, color, and price
class Product {
    private String name;
    private String color;
    private String size;
    private double price;

    public Product(String name, String color, String size, double price) {
        this.name = name;
        this.color = color;
        this.size = size;
        this.price = price;
    }

    public String getColor() { return color; }
    public String getSize() { return size; }
    public double getPrice() { return price; }

    @Override
    public String toString() {
        return "Product{name='" + name + "', color='" + color + "', size='" + size + "', price=" + price + "}";
    }
}

// Context class that uses a SortStrategy
class ProductSorter {
    private SortStrategy sortStrategy;

    // Set the sorting strategy at runtime
    public void setSortStrategy(SortStrategy sortStrategy) {
        this.sortStrategy = sortStrategy;
    }

    // Execute the sorting strategy
    public void sortProducts(List<Product> products) {
        if (sortStrategy == null) {
            throw new IllegalStateException("Sort strategy not set");
        }
        sortStrategy.sort(products);
    }
}

// Main class to demonstrate the Strategy Pattern
public class Third_Strategy_Design_Pattern_Example{
    public static void main(String[] args) {
        List<Product> products = new ArrayList<>();
        products.add(new Product("T-shirt", "Red", "M", 15.99));
        products.add(new Product("Jeans", "Blue", "L", 49.99));
        products.add(new Product("Jacket", "Black", "S", 89.99));
        products.add(new Product("Sneakers", "White", "M", 59.99));

        ProductSorter sorter = new ProductSorter();

        // Sort by size
        sorter.setSortStrategy(new SortBySize());
        sorter.sortProducts(products);

        // Sort by color
        sorter.setSortStrategy(new SortByColor());
        sorter.sortProducts(products);

        // Sort by price
        sorter.setSortStrategy(new SortByPrice());
        sorter.sortProducts(products);
    }
}
