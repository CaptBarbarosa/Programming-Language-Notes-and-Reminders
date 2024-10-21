import java.io.*;
public class Third_Copy_Example {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.out.println(
                    "Usage: java Copy sourceFile targetfile");
            System.exit(0);
        }

        File infile = new File(args[0]), outfile = new File(args[1]);
        if(!infile.exists()){
            System.out.println("Input File "+args[0]+" doesn't exist");
            System.exit(1);
        }
        if(outfile.exists()){
            System.out.println("Output File "+args[1]+" already exists");
            System.exit(1);
        }
        FileInputStream in = new FileInputStream(args[0]);
        FileOutputStream out = new FileOutputStream(args[1]);
        int r;
        while((r = in.read())!=-1){
            out.write(r);
        }
    }
}
