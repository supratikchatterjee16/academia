#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
int isKeyword(char buff[])
{
char keywords[32][10]={"void","int","main","float"};
int flag=0;
 for(int i=0;i<32;i++)
 {
  if(strcmp(keywords[i],buff)==0)
  {
  flag=1;
  break;
  }
 }
return flag;
}
int main()
{
clrscr();
char ch,buff[10],op[]="+-*/=";
int j=0;
ifstream fin("xyz.txt");
if(!fin)
{
cout<<"error opening the file";
exit(0);
}
while(!fin.eof())
{
ch=fin.get();
for(int i=0;i<6;++i)
{
if(ch==op[i])
cout<<ch<<"is operator\n";  }
if(isalnum(ch))
{
buff[j++]=ch;
}
else if((ch==' '||ch=='\n')&&(j!=0))
{
buff[j]='\0';
j=0;
if(isKeyword(buff)==1)
cout<<buff<<"is a keyword \n";
else
cout<<buff<<"is an identifier \n";
}
}
fin.close();
system("pause");
return 0;
}