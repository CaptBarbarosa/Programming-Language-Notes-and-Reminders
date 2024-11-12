class Shape{
    protected void print(){
        System.out.println("Hello bitcho. I am a shape");
    }
}

class Rectangle_inheritence extends Shape{
    public void print_rect(){
        System.out.println("Hi I am a rectangle");
        Taste taste_test = new Taste(null);
    }

    public void print_shape(){
        this.print();
    }
    
}