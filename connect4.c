#include <stdio.h>
#include <stdlib.h>

#define BOARD_SIZE 10

int board[BOARD_SIZE][BOARD_SIZE]={{0}};
int check_free(board,user,start){
 

    while(board[start][user]==1){
        start--;

    }
    return start;
    

}
void print_board(){
    int i,j;
    printf("\n");
    for(i=0;i<BOARD_SIZE;i++){
        for(j=0;j<BOARD_SIZE;j++){
            printf("%d | ",board[i][j]);
            }
            printf("\n");
            }
    printf("\n");
    for(i=0;i<39;i++){
        printf("*");
    }
    printf("\n");
    printf("");
    for(i=0;i<BOARD_SIZE;i++){
        printf("%i | ",i);
 
    }
    printf("\n");

}

int main(){
    print_board();
}