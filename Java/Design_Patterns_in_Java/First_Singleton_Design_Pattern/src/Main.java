public class Main {
    public static void main(String[] args) throws Exception {
        first_singleton_example singleInstance = first_singleton_example.getInstance();
        singleInstance.showMessage();
        first_singleton_example anotherReference = first_singleton_example.getInstance();
        System.out.println(singleInstance == anotherReference);

        //Please observe that if we comment out the "private first_singleton_example() {}" part of the first_singleton_example we are able to create multiple instances of it. 
        //If we don't have that part we can create a new singleton object and it makes it non-singleton
        //first_singleton_example third= new first_singleton_example();
        //System.out.println(third == singleInstance);
        
    }
}

