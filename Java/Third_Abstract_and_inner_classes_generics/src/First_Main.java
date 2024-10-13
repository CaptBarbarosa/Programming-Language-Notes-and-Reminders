public class First_Main {
    public static void main(String[] args) {
        // Declare and initialize two geometric objects

        First_Abstract_geometric_object geoObject1 = new First_circle_class(5, "Black", false);
        First_Abstract_geometric_object geoObject2 = new First_rectangle_class(5, 3);

        System.out.println("Circle:" + geoObject1);
        System.out.println("Rectangle:" + geoObject2);

        System.out.println("Equal Area" + equalArea(geoObject1, geoObject2));
        displayGeometricObject(geoObject2);
    }

    public static boolean equalArea(First_Abstract_geometric_object object1, First_Abstract_geometric_object object2) {
        return object1.getArea() == object2.getArea();}

    public static void displayGeometricObject(First_Abstract_geometric_object object) {
        System.out.println();
        System.out.println("The area is " + object.getArea());
        System.out.println("The perimeter is " + object.getPerimeter());
    }
}
