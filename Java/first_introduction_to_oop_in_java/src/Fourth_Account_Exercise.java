import java.util.Date;

public class Fourth_Account_Exercise {
    private int id=0;
    private double balance = 0;
    private double annualInterestRate = 0;
    private Date dateCreated;
    public double getMonthlyInterestRate(){
        return this.annualInterestRate/12;}

    public double getMonthlyInterest(){
        return (this.annualInterestRate/12)*balance;}
    public void deposit(double money){
        this.balance += money;}

    public int getId() {
        return id;}

    public void setId(int id) {
        this.id = id;}

    public double getBalance() {
        return balance;}

    public void setBalance(double balance) {
        this.balance = balance;}

    public double getAnnualInterestRate() {
        return annualInterestRate;}

    public void setAnnualInterestRate(double annualInterestRate) {
        this.annualInterestRate = annualInterestRate;}

    public Date getDateCreated() {
        return dateCreated;}

    public void setDateCreated(Date dateCreated) {
        this.dateCreated = dateCreated;}
}
