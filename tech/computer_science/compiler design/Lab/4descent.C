#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<conio.h>
char input[10];
int pos=-1,l,st=-1;
char id,num;
void E();
void T();
void F();
void advance();
void Td();
void Ed();
void advance()
{
pos++;
if((input[pos]>='a'||input[pos]>='A')&&(input[pos]<='z'||input[pos]<='Z'))
{
id=input[pos];
}
}
void E()
{
T();
Ed();
}
void Ed()
{
if(input[pos]=='+')
{
advance();
T();
Ed();
}
if(input[pos]=='-')
{
advance();
T();
Ed();
}
}
void T()
{
F(); Td();
}
void Td()
{
if(input[pos]=='*')
{
advance();
F();
Td();
}
}
void F()
{
if((islower(input[pos]))&&(isalpha(input[pos])))
{
advance();
if(input[pos]=='(')
{
advance();
E();
if(input[pos]==')')
advance();
}
}             }
void main()
{
int i;
printf("Enter input string");
scanf("%s",input);
l=strlen(input);
input[l]='$';
advance();
E();
if(pos==l)
{
printf("string accepted\n");
}
else
{
printf("string rejected\n");
}
getch();
}