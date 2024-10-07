#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include "include_example.h"

int main(){
    pthread_t my_thread[2];
    int i;
    for(i=0; i<2; i++){
        if(i==1){
           if(pthread_create(&my_thread[0], NULL, &print_for_thread_1, NULL) != 0){
                printf("Failed to create thread 0\n");
                exit(1);
            }
        }
        else{
            if(pthread_create(&my_thread[1], NULL, &print_for_thread_2, NULL) != 0){
                printf("Failed to create thread 1\n");
                exit(1);
            }
        }
    }

    for(i=0;i<2;i++){
        pthread_join(my_thread[i], NULL);}
    return 0;
}

void *print_for_thread_1(void *args){
    printf("->Hello this is thread 1\n");
    return NULL;
}

void *print_for_thread_2(void *args){
    printf("--> Hello this is thread 2\n");
    return NULL;
}
