class Taste{
    private String taste;
    Taste(String given){
        System.out.println("Reached");
        this.taste = given;
    }
    protected String get_Taste(){
        return this.taste;
    }
    protected void set_Taste(String given){
        this.taste = given;
    }
}

public class Food_composition{
    private Taste my_taste;
    private String food_name;

    public Food_composition(String taste, String food_name) {
        this.my_taste = new Taste(food_name);
        this.food_name = food_name;
    }

    public void print_name_and_taste(){
        System.out.println("Food name: "+this.food_name+ " taste: "+ my_taste.get_Taste());
    }
    
}