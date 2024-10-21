import java.io.*;

public class Second_Data_Stream {
    public static void main(String[] args) throws IOException {
        DataOutputStream output = new DataOutputStream(new FileOutputStream("src/examples/second_temp.txt"));

        output.writeUTF("John");
        output.writeDouble(85.5);
        output.writeUTF("Jim");
        output.writeDouble(185.5);
        output.writeUTF("George");
        output.writeDouble(105.25);
        output.close();

        DataInputStream input = new DataInputStream(new FileInputStream("src/examples/second_temp.txt"));

        System.out.println(input.readUTF() + " " + input.readDouble());
        System.out.println(input.readUTF() + " " + input.readDouble());
        System.out.println(input.readUTF() + " " + input.readDouble());
        input.close();
    }
}
