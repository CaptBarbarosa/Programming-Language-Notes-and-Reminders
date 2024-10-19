public class Fourth_Password {
    private String password;

    public Fourth_Password(String password) throws Fourth_InvalidPasswordException {
        if (!isValid(password)) {
            throw new Fourth_InvalidPasswordException("Invalid password: " + getInvalidReason(password));
        }
        this.password = password;
    }

    private boolean isValid(String password) {
        return password.length() >= 7 && containsLetter(password) && containsNumber(password);
    }

    private String getInvalidReason(String password) {
        if (password.length() < 7) {
            return "Password should be at least 7 characters long.";}
        if (!containsLetter(password)) {
            return "Password should contain at least a letter.";}
        if (!containsNumber(password)) {
            return "Password should contain at least a number.";}
        return "Unknown reason";
    }

    private boolean containsLetter(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isLetter(c)) {
                return true;}
        }
        return false;
    }

    private boolean containsNumber(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) {
                return true;
            }
        }
        return false;
    }

    public String getPassword() {
        return password;
    }
}
