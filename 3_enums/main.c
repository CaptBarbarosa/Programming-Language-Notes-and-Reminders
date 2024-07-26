#include <stdio.h>

// Main reason why we use enums instead of defines is that enums are easier to debug.

enum Cars{
    TOYOTA,
    FORD,
    FERRARI,
    TESLA=100,
    NISSAN
};

typedef enum fruits{
    APPLE,
    CARROT
}fruits; // Just like in the structs, if we want to use the name of enum, we use typedef.

int main(){
    enum Cars ford = FORD; 
    printf("ford = %d\n", ford); // It prints 1 because the FORD is in the index 1.
    
    enum Cars tesla = TESLA; // We can allocate to the enum variables
    printf("tesla = %d\n", tesla);
    
    enum Cars nissan = NISSAN; // Sİnce we allocated 100 to tesla (which was one previous) we get 101
    printf("nissan = %d\n", nissan);

    fruits carrot = CARROT;
    printf("carrot = %d\n",carrot);
    return 0;
}

