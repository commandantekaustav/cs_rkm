//
// Created by User on 7/10/2019.
//

#include <stdio.h>
int main(){
    int n,m,i,j;
    scanf("%d%d",&n,&m);
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            printf("%d%d\n",i,j);
            getchar();
        }
        
    }
}