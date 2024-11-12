public class App {
    public static void main(String[] args) throws Exception {
        Rectangle_inheritence my_rect = new Rectangle_inheritence();
        my_rect.print_shape();
        my_rect.print();

        Food_composition my_food = new Food_composition("TASTY", "Sugary food");
        my_food.print_name_and_taste();
        //System.out.println(my_food.get_Taste());
    }
}
