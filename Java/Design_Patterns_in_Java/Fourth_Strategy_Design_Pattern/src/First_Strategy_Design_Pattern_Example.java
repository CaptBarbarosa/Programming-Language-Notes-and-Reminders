
import java.util.Arrays;
import java.util.Collections;

interface SortStrategy {
    void sort(int[] items);
}

// Concrete Strategy for sorting by Ascending order
class AscendingSortStrategy implements SortStrategy {
    @Override
    public void sort(int[] items) {
        Arrays.sort(items);
        System.out.println("Sorted in ascending order: " + Arrays.toString(items));
    }
}

// Concrete Strategy for sorting by Descending order
class DescendingSortStrategy implements SortStrategy {
    @Override
    public void sort(int[] items) {
        Integer[] itemsBoxed = Arrays.stream(items).boxed().toArray(Integer[]::new);
        Arrays.sort(itemsBoxed, Collections.reverseOrder());
        System.out.println("Sorted in descending order: " + Arrays.toString(itemsBoxed));
    }
}

// Context class using a Strategy
class ProductSorter {
    private SortStrategy strategy;

    // Set the strategy at runtime
    public void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    // Execute the strategy
    public void sortProducts(int[] items) {
        strategy.sort(items);
    }
}

// Client code
public class First_Strategy_Design_Pattern_Example {
    public static void main(String[] args) {
        ProductSorter sorter = new ProductSorter();

        int[] items = {5, 2, 8, 3, 1};

        // Sort in ascending order
        sorter.setStrategy(new AscendingSortStrategy());
        sorter.sortProducts(items);

        // Sort in descending order
        sorter.setStrategy(new DescendingSortStrategy());
        sorter.sortProducts(items);
    }
}
