#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>
int temp1=0,n;
char nt[10],pdt[10][50];
void addnterm(char);
void first(char);
void follow(char);
int flag=0;
void main()
{
int temp,i,j;
clrscr();
cout<<"\nEnter the number of productions:";
cin>>n;
cout<<"\nEnter the productions:";
for(i=0;i<n;i++)
gets(pdt[i]);
for(i=0;i<n;i++)
{
temp=strlen(pdt[i]);
for(j=0;j<temp;j++)
{
if(isupper(pdt[i][j])&&pdt[i][j]!='î')
30
{
addnterm(pdt[i][j]);
}
}
}
for(i=0;i<temp1;i++)
{
cout<<"\nFirst("<<nt[i]<<")={";
first(nt[i]);
cout<<"\b}";
}
for(i=0;i<temp1;i++)
{
cout<<"\nFollow("<<nt[i]<<")={";
if(i==0)
cout<<"$,";
follow(nt[i]);
cout<<"\b}";
}
getch();
}
void addnterm(char a)
{
int i=0,flag=1;
if(temp1==0)
{
nt[temp1]=a;
temp1++;
}
else
{
while(i<temp1&&flag)
{
if(a==nt[i])
flag=0;
else
i++;
}
if(flag)
{
nt[temp1]=a;
temp1++;
}
}
}
void first(char a)
31
{
int i;
for(i=0;i<n;i++)
{
if(pdt[i][0]==a)
{
if((isdigit(pdt[i][2])||islower(pdt[i][2])||pdt[i][2]=='('
||pdt[i][2]==')'||pdt[i][2]=='+'||pdt[i][2]=='-'||pdt[i][2]=='*' ||pdt[i][2]=='/'||pdt[i][2]=='%') &&
pdt[i][2]!='î')
cout<<pdt[i][2]<<",";
else if(pdt[i][2]=='î' && !flag)
cout<<pdt[i][2]<<",";
else
first(pdt[i][2]);
}
}
}
void follow(char a)
{
int i,j;
for(i=0;i<n;i++)
{
j=2;
while(pdt[i][j]!='\0')
{
if(pdt[i][j]==a)
{
if((isdigit(pdt[i][j+1])||islower(pdt[i][j+1])||pdt[i][j+1]=='('||pdt[i][j+1]==')'||pdt[i][j+1]=='+'||p
dt[i][j+1]=='-'||pdt[i][j+1]=='*'|| pdt[i][j+1]=='/'||pdt[i][j+1]=='%') && pdt[i][j+1]!='î')
cout<<pdt[i][j+1];
else if(pdt[i][j+1]=='\0')
{
if(i==0)
cout<<"$,";
if(pdt[i][j]==pdt[i][0]);
else
follow(pdt[i][0]);
}
else
{
flag=1;
first(pdt[i][j+1]);
}}
j++;
}}}