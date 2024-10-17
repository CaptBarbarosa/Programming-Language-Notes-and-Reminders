public class Third_Generic_Classes <T>{
    private T object_given;
    public Third_Generic_Classes(){}
    public Third_Generic_Classes(T content){
        this.object_given = content;
    }
    public void setObject_given(T content){
        this.object_given = content;}

    public T getObject_given(){
        return object_given;}
}
