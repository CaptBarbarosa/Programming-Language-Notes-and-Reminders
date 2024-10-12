public class First_Inheritence_Geometric_Object {
    protected String color="white";
    private boolean filled;
    private java.util.Date dateCreated;

    /** Construct a default geometric object */
    public First_Inheritence_Geometric_Object() {
        dateCreated = new java.util.Date();
    }

    public First_Inheritence_Geometric_Object(String color, boolean filled) {
        dateCreated = new java.util.Date();
        this.color = color;
        this.filled = filled;
    }

    public String getColor() {
        return color;}

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isFilled() {
        return filled;
    }

    protected void setFilled(boolean filled) {
        this.filled = filled;
    }

    /** Get dateCreated */
    public java.util.Date getDateCreated() {
        return dateCreated;
    }

    /** Return a string representation of this object */
    public String toString() {
        return "\n-->Created on: " + dateCreated + "\ncolor: " + color +
                " and filled: " + filled;
    }

    public void override_this(){
        System.out.println("In the Gerometric Object");
    }
}
