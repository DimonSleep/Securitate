Program exponentiere_modulara;
uses crt;
var
  cif:array[1..100] of byte;
  c,a,x,y,x1,n:longint;

Procedure Trans_baza(n1:longint;var k:longint);
var i,j:integer;
begin
 i:=0;
 while n1<>0 do
  begin
   inc(i);
   cif[i]:=n1 mod 2;
   n1:=n1 div 2;
 end;
 k:=i;
 for j:=i downto 1 do write(cif[j]);
 writeln;
end;

Procedure Inv(n,b:longint;var t:longint);
var n0,b0,r,q1,t0,temp:longint;
Begin
 n0:=n;b0:=b;
 t0:=0;t:=1;
 q1:=trunc(n0/b);
 r:=n0-q1*b;
 while r>0 do
  begin
   temp:=t0-q1*t;
   if temp>=0 then temp:=temp mod n
     else temp:=n-((-temp) mod n);
   n0:=b0;b0:=r;t0:=t; t:=temp;
   q1:=trunc(n0/b0); r:=n0-q1*b0;
  end;
 if b0<>1 then  begin
   t:=0;writeln(b,' nu are inversa mod ',n) end
      else writeln('inversa=',t);
end;

Function Criptare(M_c:longint):longint;
var z,q,m:longint;
begin
 write('c=');readln(c);
 Trans_baza(c,m);
 z:=1;
 for q:=m downto 1 do
  begin
   if cif[q]=0 then z:=(z*z) mod n
     else begin
            z:=(z*z) mod n;
            z:=(z*x) mod n;
          end;
 end;
 Criptare:=z;
end;

Function Decriptare(x:longint):longint;
var q,m,z:longint;
begin
 inv(n-1,c,a);
 Trans_baza(a,m);
 z:=1;
 for q:=m downto 1 do
  begin
   if cif[q]=0 then z:=(z*z) mod n
     else begin
            z:=(z*z) mod n;
            z:=(z*x) mod n;
          end;
 end;
 Decriptare:=z;
end;

Begin
 clrscr;
 write('n=');readln(n);
 write('x=');readln(x);
 y:=Criptare(x);
 writeln('mesajul criptat: ',y);
 x1:=Decriptare(y);
 writeln('mesajul decriptat: ',x1);
 readkey;
End.