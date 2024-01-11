Program secret;
uses crt;
var i,j,q,k,n,a1:byte;
    s:longint;
    p1,l:real;
    g:boolean;
    a,x:array[1..20] of byte;
    b,y:array[1..20] of longint;
    f1,q1:text;

Function Putere(m:byte;z:byte):longint;
var p:longint;
    h:byte;
begin
 p:=1;
 for h:=1 to m do p:=p*z;
 Putere:=p;
end;
Function F(t:integer):longint;
var d:byte;
    w:longint;
begin
 w:=s;
 for d:=1 to k-1 do
   w:=w+a[d]*putere(d,t);
 F:=w;
end;
Begin
 clrscr;
 textcolor(14);
 writeln('Impartirea Secretului:');
 textcolor(10);
 assign(f1,'secret.txt');reset(f1);
 readln(f1,s);textcolor(11);
 {citim in cate parti va fi divizat secretul}
 readln(f1,n);
 {citim numarul de parti necesare pentru restabilirea secretului}
 readln(f1,k);
 {citim coeficientii polinomului secret}
 for i:=1 to k-1 do readln(f1,a[i]);
 close(f1);

 assign(q1,'umbre.txt');rewrite(q1);
 for i:=1 to n do b[i]:=F(i);
 textcolor(4);
 writeln('Perechile de numere in care a fost impartita cheia:');
 textcolor(15);
 for i:=1 to n do writeln(q1,i,' ',b[i]);
 textcolor(14);
 readkey;
 clrscr;
 close(q1);
 writeln('R E S T A B I L I R E A   S E C R E T U L U I:');
 textcolor(9);
 assign(f1,'restabil.txt');reset(f1);
 {citim din fisier perechile de numere care participa la restabilirea secretului}
 textcolor(12);
 for i:=0 to k-1 do readln(f1,x[i],y[i]);
 p1:=0;
 for i:=0 to k-1 do
  begin
    l:=1;
    for j:=0 to k-1 do
      if j<>i then l:=(-l*x[j])/(x[i]-x[j]);
    l:=l*y[i];
    p1:=p1+l;
  end;
 textcolor(14);
 close(f1);
 writeln('S E C R E T U L  R E S T A B I L I T A  E S T E: ',p1:8:0);
 readkey;
End.