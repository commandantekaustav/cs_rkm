// Minesweeper - Space Efficient Version
// Created by Kaustav on 7/9/2019.
// /A/CPL/A1/C

#include <stdio.h>
int main() {
    int n,m,i,j;
    int flag =1; // to adjust the increment of j. This happened because the inner loop is always running on its own in the first iteration
    char c;
    scanf("%d %d", &n, &m);
    //printf("n=%d m=%d\n",n,m);
    int field[3][m];

    for (i = 0; i < 3; i++) {
        for (j = 0; j < m; j++) {
            field[i][j] = 0;
        }
    }

//    printf("buffer array:\n");
//    for (i = 0; i < 3; i++) {
//        for (j = 0; j < m; j++) {
//            printf("%d",field[i][j]);
//        }
//        printf("\n");
//    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if(flag==1){
                --j;
                flag=0;
            }
//            printf("%d %d\n",i,j);
            c = getchar();
            //scanf("%c",&c);
            if (c != '*')
                continue;
            else {

                if (i == 0) {
                    if (j == 0) {
                        field[(i + 1) % 3][j]++;field[i % 3][j + 1]++;field[(i + 1) % 3][j + 1]++;
                    } else if (j == n - 1) {
                        field[i % 3][j - 1]++;field[(i + 1) % 3][j - 1]++;field[(i + 1) % 3][j]++;
                    } else {
                        field[i % 3][j - 1]++;field[i % 3][j + 1]++;field[(i + 1) % 3][j - 1]++;
                        field[(i + 1) % 3][j]++;field[(i + 1) % 3][j + 1]++;
                    }
                } else if (j == 0) {
                    if (i == n - 1) {
                        field[(i - 1) % 3][j]++;field[(i - 1) % 3][j + 1]++;field[i % 3][j + 1]++;
                    } else {
                        field[(i - 1) % 3][j]++;field[(i - 1) % 3][j + 1]++;field[i % 3][j + 1]++;
                        field[(i + 1) % 3][j]++;field[(i + 1) % 3][j + 1]++;
                    }
                } else if (i == n - 1) {
                    if (j == n - 1) {
                        field[(i - 1) % 3][j - 1]++;field[(i - 1) % 3][j]++;field[i % 3][j - 1]++;
                    } else {
                        field[(i - 1) % 3][j - 1]++;field[(i - 1) % 3][j]++;field[(i - 1) % 3][j + 1]++;
                        field[i % 3][j - 1]++;field[i % 3][j + 1]++;
                    }
                } else if (j == n - 1) {
                    field[(i - 1) % 3][j - 1]++;field[(i - 1) % 3][j]++;field[i % 3][j - 1]++;
                    field[(i + 1) % 3][j - 1]++;field[(i + 1) % 3][j]++;
                } else {
                    field[(i - 1) % 3][j - 1]++;field[(i - 1) % 3][j]++;field[(i - 1) % 3][j + 1]++;
                    field[i % 3][j - 1]++;field[i % 3][j + 1]++;field[(i + 1) % 3][j - 1]++;
                    field[(i + 1) % 3][j]++;field[(i + 1) % 3][j + 1]++;
                }
                field[i%3][j] = 9;
            }

        }
        getchar();
        if (i>=1){
//            printf("line# %d\n",i%3);
            for(j=0;j<m;j++){
                if(field[(i-1)%3][j] > 8)
                    printf("*");
                else{
                    printf("%d",field[(i-1)%3][j]);
                }
            field[(i-1)%3][j]=0;
            }
            printf("\n");
        }
    }
    for(j=0;j<m;j++){
        if(field[(i-1)%3][j] > 8)
            printf("*");
        else
            printf("%d",field[(n-1)%3][j]);
    }

    return 0;
}