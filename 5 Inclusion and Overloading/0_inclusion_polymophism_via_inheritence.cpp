#include <iostream>
using namespace std;

class Language{
    public:
        virtual void sound(){
            cout<<"Language"<<endl;
        }
};

class Spanish: public Language{
    public:
        void talk(){
            cout<< "Spanish"<<endl;
        }
        void unimportant_function(){
            cout << "Unimportant function"<<endl;
        }
};

class Turkic: public Language{
    public:
        void talk(){
            cout << "Old Turkic" << endl;
        }
        virtual ~Turkic() = default;
};

class Turkey_Turkic: public Language{
    public:
        void talk(){
            cout << "Turk"<<endl;
        }
};

int main(){
    Turkey_Turkic my_lang;
    my_lang.talk();
    Turkey_Turkic *my_lang_2;
    my_lang_2 = &my_lang;
    my_lang_2->talk();
    Turkic my_lang_3;
    my_lang_3.talk();
    return 0;
}
