import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class First_File_Streams {
    public static void main(String[]args) throws IOException {
        FileOutputStream output = new FileOutputStream("src/examples/First_example.dat");
        for(int i=1; i <= 10; i++){
            output.write(i);}
        output.close();

        FileInputStream input = new FileInputStream("src/examples/First_example.dat");
        int val;
        while((val = input.read())!=-1)
            System.out.println("Value is: "+val);
        input.close();
    }
}
