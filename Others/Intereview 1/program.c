#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_TOTAL 10000
#define MAX_LINE_LENGTH 1000

int lines = 0;

void solve(char *expression, FILE *file_output){

  int parenthesisCounter = 0;
  int i = 0;

  while(expression[i]!= '\0' && i < 1000){
    if(expression[i]=='\n') lines++;
    if(expression[i]=='(') parenthesisCounter++;     
    else if(expression[i]==')'){  
      parenthesisCounter--;
      if(parenthesisCounter<0)  
      break;  
    }  
    i++;
  }  

  if(parenthesisCounter==0) fprintf(file_output, "%s", "correct\n"); 
  else fprintf(file_output, "%s", "incorrect\n");  
}

int main(){

  char line[MAX_LINE_LENGTH] = {0};
  clock_t start_clock = clock();

  FILE *file_input, *file_output;
  file_input = fopen("input.txt", "r");
  file_output = fopen("output.txt", "w");

  if (file_input == NULL || file_output == NULL){   
    printf("Error! Could not open file\n"); 
    exit(-1);
  } 

  while(fgets(line, MAX_LINE_LENGTH, file_input) != NULL){
    solve(line, file_output);
    if(lines > MAX_LINE_TOTAL){
      printf("Limite excedido.\n");
      break;
    }
  }

  fclose(file_input);
  fclose(file_output);

  printf("%d.%d seconds", (clock() - start_clock) / CLOCKS_PER_SEC, ((clock() - start_clock)*1000) / CLOCKS_PER_SEC);
}