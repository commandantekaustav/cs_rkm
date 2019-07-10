//
// Created by User on 7/8/2019.
//

#include <stdio.h>

int main() {
    int n, m, c;
    scanf("%d%d", &n, &m);

    int field[3][m];

    for (int k = 0; k < 3; k++) {
        for (int l = 0; l < m; l++) {
            field[k][l] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            c = getchar();

            if (c != '*') continue;
            else {
                field[i%3][j] = 9;
                if (i == 0) {
                    if (j == 0) {
                        field[(i + 1) % 3][j]++;
                        field[i % 3][j + 1]++;
                        field[(i + 1) % 3][j + 1]++;
                    } else if (j == n - 1) {
                        field[i % 3][j - 1]++;
                        field[(i + 1) % 3][j - 1]++;
                        field[(i + 1) % 3][j]++;
                    } else {
                        field[i % 3][j - 1]++;
                        field[i % 3][j + 1]++;
                        field[(i + 1) % 3][j - 1]++;
                        field[(i + 1) % 3][j]++;
                        field[(i + 1) % 3][j + 1]++;
                    }
                } else if (j == 0) {
                    if (i == n - 1) {
                        field[(i - 1) % 3][j]++;
                        field[(i - 1) % 3][j + 1]++;
                        field[i % 3][j + 1]++;
                    } else {
                        field[(i - 1) % 3][j]++;
                        field[(i - 1) % 3][j + 1]++;
                        field[i % 3][j + 1]++;
                        field[(i + 1) % 3][j]++;
                        field[(i + 1) % 3][j + 1]++;
                    }
                } else if (i == n - 1) {
                    if (j == n - 1) {
                        field[(i - 1) % 3][j - 1]++;
                        field[(i - 1) % 3][j]++;
                        field[i % 3][j - 1]++;
                    } else {
                        field[(i - 1) % 3][j - 1]++;
                        field[(i - 1) % 3][j]++;
                        field[(i - 1) % 3][j + 1]++;
                        field[i % 3][j - 1]++;
                        field[i % 3][j + 1]++;
                    }
                } else if (j == n - 1) {
                    field[(i - 1) % 3][j - 1]++;
                    field[(i - 1) % 3][j]++;
                    field[i % 3][j - 1]++;
                    field[(i + 1) % 3][j - 1]++;
                    field[(i + 1) % 3][j]++;
                } else {
                    field[(i - 1) % 3][j - 1]++;
                    field[(i - 1) % 3][j]++;
                    field[(i - 1) % 3][j + 1]++;
                    field[i % 3][j - 1]++;
                    field[i % 3][j + 1]++;
                    field[(i + 1) % 3][j - 1]++;
                    field[(i + 1) % 3][j]++;
                    field[(i + 1) % 3][j + 1]++;
                }
            }
        }

        if (i > 0) {
            for (int y = 0; y < m; y++) {
                if (field[(i - 1) % 3][y] > 8)
                    printf("*");
                else
                    printf("%d", field[(i - 1) % 3][y]);
            }
            printf("\n");
        }
    }


    return 0;
}