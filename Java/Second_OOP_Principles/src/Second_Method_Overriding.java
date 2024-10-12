public class Second_Method_Overriding {
    class Animal {
        public void sound() {
            System.out.println("Animal makes a sound");}
    }

    class Dog extends Animal {
        @Override
        public void sound() {
            System.out.println("Dog barks");}
    }

    class Cat extends Animal {
        @Override
        public void sound() {
            System.out.println("Cat meows");}
    }

    public static void main(String[] args) {
        Second_Method_Overriding secondMethodOverriding = new Second_Method_Overriding();

        Animal myAnimal = secondMethodOverriding.new Animal();
        Animal myDog = secondMethodOverriding.new Dog();
        Animal myCat = secondMethodOverriding.new Cat();

        myAnimal.sound();  // Output: Animal makes a sound
        myDog.sound();     // Output: Dog barks
        myCat.sound();     // Output: Cat meows
    }
}
