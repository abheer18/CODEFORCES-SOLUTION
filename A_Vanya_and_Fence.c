#include<stdio.h>
int main(){
    int n, k, i;
    int frnd = n;
    scanf("%d %d", &n, &k);
    for (i = 0; i < n;i++){
        scanf("%d",&row);
        frnd = frnd + (row > k);
    }
    printf("%d", frnd);
}