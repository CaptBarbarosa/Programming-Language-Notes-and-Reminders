

// Product class
class House {
    // Required parameters
    private String foundation;
    private String structure;

    // Optional parameters
    private boolean garden;
    private boolean swimmingPool;
    private boolean garage;

    // Private constructor to restrict object creation
    private House(HouseBuilder builder) {
        this.foundation = builder.foundation;
        this.structure = builder.structure;
        this.garden = builder.garden;
        this.swimmingPool = builder.swimmingPool;
        this.garage = builder.garage;
    }

    // Getters for all attributes
    public String getFoundation() {
        return foundation;
    }

    public String getStructure() {
        return structure;
    }

    public boolean hasGarden() {
        return garden;
    }

    public boolean hasSwimmingPool() {
        return swimmingPool;
    }

    public boolean hasGarage() {
        return garage;
    }

    @Override
    public String toString() {
        return "House{" +
                "foundation='" + foundation + '\'' +
                ", structure='" + structure + '\'' +
                ", garden=" + garden +
                ", swimmingPool=" + swimmingPool +
                ", garage=" + garage +
                '}';
    }

    // Builder class
    public static class HouseBuilder {
        // Required parameters
        private String foundation;
        private String structure;

        // Optional parameters
        private boolean garden = false;
        private boolean swimmingPool = false;
        private boolean garage = false;

        // Constructor for mandatory attributes
        public HouseBuilder(String foundation, String structure) {
            this.foundation = foundation;
            this.structure = structure;
        }

        // Setter methods for optional attributes
        public HouseBuilder setGarden(boolean garden) {
            this.garden = garden;
            return this;
        }

        public HouseBuilder setSwimmingPool(boolean swimmingPool) {
            this.swimmingPool = swimmingPool;
            return this;
        }

        public HouseBuilder setGarage(boolean garage) {
            this.garage = garage;
            return this;
        }

        // Method to build the final House object
        public House build() {
            return new House(this);
        }

        public void builder_talk(){
            System.out.println("Hello. You are in the house.builder. How you doing?");
        }
    }
}

// Demonstration of Builder Pattern usage
public class First_Implementation_of_Builder {
    public static void main(String[] args) {
        // Creating a House object with a garden and garage
        House houseWithGardenAndGarage = new House.HouseBuilder("Concrete", "Wood")
                .setGarden(true)
                .setGarage(true)
                .build();

        System.out.println(houseWithGardenAndGarage);

        // Creating a House object with all features
        House luxuryHouse = new House.HouseBuilder("Concrete", "Steel")
                .setGarden(true)
                .setSwimmingPool(true)
                .setGarage(true)
                .build();
                
        System.out.println(luxuryHouse);
        House.HouseBuilder my_builder = new House.HouseBuilder("a","a");
        my_builder.builder_talk();
    }
}
