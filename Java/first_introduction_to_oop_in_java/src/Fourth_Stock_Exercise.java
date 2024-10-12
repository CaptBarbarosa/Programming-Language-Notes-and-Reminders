import static java.lang.Math.abs;

public class Fourth_Stock_Exercise {
    private String symbol;
    private String name;
    private double previous_closing_price;
    private double current_price;

    public Fourth_Stock_Exercise(String symbol, String name) {
        this.symbol = symbol;
        this.name = name;
    }

    public String getSymbol() {
        return symbol;}

    public void setSymbol(String symbol) {
        this.symbol = symbol;}

    public String getName() {
        return name;}

    public void setName(String name) {
        this.name = name;}

    public double getPrevious_closing_price() {
        return previous_closing_price;}

    public void setPrevious_closing_price(double previous_closing_price) {
        this.previous_closing_price = previous_closing_price;}

    public double getCurrent_price() {
        return current_price;}

    public void setCurrent_price(double current_price) {
        this.current_price = current_price;}

    public double getChangePrice(){
        return abs(this.current_price-this.previous_closing_price)/this.current_price;}
}
