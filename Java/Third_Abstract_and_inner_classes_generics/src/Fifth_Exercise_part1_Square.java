public class Fifth_Exercise_part1_Square extends Fifth_Geometric_Object implements Fifth_Exercise_part1_Colourable{
    Fifth_Exercise_part1_Square(){}
    Fifth_Exercise_part1_Square(String color, boolean filled){
        super(color,filled);
    }
    public void howToColor(){
        System.out.println("Color all four sides");
    }
}
