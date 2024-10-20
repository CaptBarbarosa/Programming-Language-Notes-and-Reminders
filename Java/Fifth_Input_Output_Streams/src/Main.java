import java.io.File;

public class Main {
    public static void main(String[] args) {
        File file = new File("src/examples/0_test"); //This is not an input or output file stuff. This is just a handle.
        System.out.println("Does it exist? " + file.exists());
        System.out.println("The file has " + file.length() + " bytes");
        System.out.println("Can it be read? " + file.canRead());
        System.out.println("Can it be written? " + file.canWrite());
        System.out.println("Is it a directory? " + file.isDirectory());
        System.out.println("Is it a file? " + file.isFile());
        System.out.println("Is it absolute? " + file.isAbsolute());
        System.out.println("Is it hidden? " + file.isHidden());
        System.out.println("Absolute path is " + file.getAbsolutePath());
        System.out.println("Last modified on " + new java.util.Date(file.lastModified()));
        System.out.println("Seperator:"+java.io.File.separator);

        file = new File("src/examples");
        listRecursive(file);
    }
    public static void listRecursive(File dir) {
        if (dir.isDirectory()) {
            File[] items = dir.listFiles();
            for (File item : items) {
                if(!item.isDirectory())
                    System.out.println(item.getAbsolutePath());
                if (item.isDirectory()) listRecursive(item);
            }
        }
    }
}