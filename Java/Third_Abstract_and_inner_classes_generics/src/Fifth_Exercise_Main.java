import java.util.ArrayList;
import java.util.List;

public class Fifth_Exercise_Main {
    public static void main(String[]args){
        Fifth_Exercise_part1_Square my_square = new Fifth_Exercise_part1_Square("Blue", false);
        List<Fifth_Exercise_part1_Square> squares_array = new ArrayList<>();
        squares_array.add(new Fifth_Exercise_part1_Square());
        squares_array.add(new Fifth_Exercise_part1_Square("Blue", false));
        squares_array.add(new Fifth_Exercise_part1_Square("White", true));
        for(Fifth_Exercise_part1_Square squares: squares_array){
            System.out.print("--> Color: "+ squares.getColor() + " howToColor: ");
            squares.howToColor();
            System.out.print("\n");
        }

        String[] stringArray = {"apple", "banana", "grape", "orange", "kiwi", "peach", "lemon", "mango", "pear", "plum"};
        String smallestString = (String) Fifth_Geometric_Object.min(stringArray);
        System.out.println("Smallest string: " + smallestString);

    }
}
