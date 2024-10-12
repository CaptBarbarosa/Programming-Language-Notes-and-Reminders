public class Fourt_Main_Exercise {
    public static void main(String []args){
        Fourth_Stock_Exercise oracle_stock = new Fourth_Stock_Exercise("ORCL","ORACLE");
        oracle_stock.setCurrent_price(34.35);
        oracle_stock.setPrevious_closing_price(34.5);
        System.out.println("Percentage change is: "+oracle_stock.getChangePrice());
    }
}
