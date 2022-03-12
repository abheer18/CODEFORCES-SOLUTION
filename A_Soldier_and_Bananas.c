#include<stdio.h>
int main(){
    int k, n, w, cost=0;
    scanf("%d %d %d", &k, &n, &w);
    for (int i = 1; i <= w;i++){
     cost += (i * k);
    }
    int y = cost - n;
    if(y <= 0){
        printf("0\n");
    }
    else{
        printf("%d", y);
    }
}