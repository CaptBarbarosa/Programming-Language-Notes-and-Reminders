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

        float get_balance(void){
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
            delete[] this->account_name;
        }

};


int main(){
    return 0;
}

