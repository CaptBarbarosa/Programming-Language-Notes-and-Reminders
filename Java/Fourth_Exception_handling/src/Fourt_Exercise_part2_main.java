import java.util.Scanner;

public class Fourt_Exercise_part2_main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputPassword;

        while (true) {//Continues till correct password
            System.out.print("Enter a valid password: ");
            inputPassword = scanner.nextLine();

            try {
                Fourth_Password password = new Fourth_Password(inputPassword);
                System.out.println("Password accepted: " + password.getPassword());
                break;
            } catch (Fourth_InvalidPasswordException ex) {
                System.out.println(ex.getMessage());
            }
        }

        scanner.close();
    }
}
