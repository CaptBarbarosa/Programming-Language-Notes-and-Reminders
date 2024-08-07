#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

class Account{
    private:
        int account_number;
        float account_balance;
        char *account_name;

    public:
        Account(){
            this-> account_number = 0;
            this-> account_balance = 0;
            this->account_name = new char [15];
            strcpy(this-> account_name, "unspecified");}

        Account(int account_number, float account_balance, char* name){
            this-> account_number = account_number;
            this-> account_balance = account_balance;
            this->account_name = new char [strlen(name)];}

        Account(const Account& acc){
            this-> account_number = acc.account_number;
            this-> account_balance = acc.account_balance;
            this-> account_name = new char[strlen(acc.account_name)+1];
            strcpy(this-> account_name, acc.account_name);
        }

        void set_account_number(int number){
            this-> account_number = number;}

        int get_account_number(void){
            return this-> account_number;}

        void set_account_balance(int balance){
            this-> account_balance = balance;}

        float get_account_balance(void){
            return this-> account_balance;}

        void set_account_name(char *name){
            delete[] this-> account_name;
            this->account_name = new char[strlen(name)+1];
            strcpy(this-> account_name, name);}

        char *get_account_name(){
            return this-> account_name;
        }

        void input_transaction(char transaction_type, float amount){
            if((transaction_type == 'w' || transaction_type == 'W') && amount > this-> account_balance){
                throw "Insufficient amount of money in the account\n";}
            else if(transaction_type == 'w' && transaction_type == 'W'){
                this-> account_balance -= amount;}
            else if(transaction_type == 'd' || transaction_type == 'D'){
                this-> account_balance += amount;}
            else{
                throw "Unknown operation entered\n";}
        }

        float calculate_future_balance(float interest_rate, float years){
            return account_balance = pow(this->account_balance*(1 + interest_rate),years);}

        Account& operator=(const Account& acc){
            if(this == &acc){
                return *this;}
            this-> account_number = acc.account_number;
            this-> account_balance = acc.account_balance;
            delete this->account_name;
            this-> account_name = new char[strlen(acc.account_name)+1];
            strcpy(this-> account_name, acc.account_name);}

        ~Account(){
            delete[] this->account_name;}
};

    int Menu(){
        int selection;
        cout<<"\n\n------------------------------------\n";
        cout<<"1. Change the account balance\n2. Get the current balance\n3.Deposit\n4. Withdrawal\n5. Plan your future balance\n6. Mortgage plan\n7.Exit\nEnter your selection: ";
        cin>> selection;
        return selection;
    }

int main(){
    Account my_account;
    int selection;
    float balance, amount;
    do{
        selection = Menu();
        if(selection == 1){
            cout<<"Enter a new account balance: ";
            cin>>balance;
            my_account.set_account_balance(balance);
            cout<<"New account balance is: "<<my_account.get_account_balance()<<endl;}
        else if (selection == 2){
            cout<<"Account balance is"<<my_account.get_account_balance()<<" TL"<<endl;}

        else if(selection == 3){
            cout<< "Enter an amount for deposit: ";
            cin>>amount;
            my_account.input_transaction('d', amount);
            cout<<"New account balance is "<<my_account.get_account_balance()<<" TL\n";}

        else if(selection == 4){
            cout<< "Enter an amount for withrawal: ";
            cin>>amount;
            my_account.input_transaction('w', amount);
            cout<<"New account balance is "<<my_account.get_account_balance()<<" TL\n";}

    }while(selection!=7);
    return 0;
}

