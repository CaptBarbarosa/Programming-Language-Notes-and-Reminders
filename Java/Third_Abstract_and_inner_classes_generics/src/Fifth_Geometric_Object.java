import java.util.ArrayList;

public class Fifth_Geometric_Object{
    private String color="white";
    private boolean filled;
    private java.util.Date dateCreated;

    /** Construct a default geometric object */
    public Fifth_Geometric_Object() {
        dateCreated = new java.util.Date();
    }

    /** Construct a geometric object with the specified color
     *  and filled value */
    public Fifth_Geometric_Object(String color, boolean filled) {
        dateCreated = new java.util.Date();
        this.color = color;
        this.filled = filled;
    }

    /** Return color */
    public String getColor() {
        return color;
    }

    /** Set a new color */
    public void setColor(String color) {
        this.color = color;
    }

    /** Return filled. Since filled is boolean,
     its get method is named isFilled */
    public boolean isFilled() {
        return filled;
    }

    /** Set a new filled */
    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    /** Get dateCreated */
    public java.util.Date getDateCreated() {
        return dateCreated;
    }

    /** Return a string representation of this object */
    public String toString() {
        return "BeGeometricObject"+"created on " + dateCreated + "\ncolor: " + color +
                " and filled: " + filled;
    }

    //<E extends Comparable<E>>
    public static <T extends Comparable<T>> T min(T[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Array must not be null or empty");
        }

        T min = array[0];
        for (T element : array) {
            if (element.compareTo(min) < 0) {
                min = element;
            }
        }
        return min;
    }

}
