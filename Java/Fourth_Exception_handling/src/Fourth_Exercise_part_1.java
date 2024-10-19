import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Fourth_Exercise_part_1 {
    public static void main(String[] args){
        int[] my_list = new int[50];
        int index;
        Random rand = new Random();
        Scanner my_scanner = new Scanner(System.in);
        for(int i=0; i<50; i++){
            my_list[i] = rand.nextInt(100);
        }
        try{
            System.out.println("Enter the index of array: ");
            index = my_scanner.nextInt();
            if(index < 0){
                throw new IllegalArgumentException("Index can't be negative");}
            else if(index>50){
                throw new IllegalArgumentException("Index can't be longer than the array size");}
            System.out.println("The number in the index" + index + " is: "+my_list[index]);
        }catch (IllegalArgumentException ex){
            System.out.println(ex.getMessage());
        }
        catch (Exception ex){
            System.out.println(ex);}
        finally {
            my_scanner.close();
        }
    }
}
