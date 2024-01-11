Program inversa_modulo;
uses crt;
var n,n0,b,b0,t,r,q,t0,temp:longint;
Begin
 clrscr;
 write('n=');readln(n);
 write('a=');readln(b);
 n0:=n;b0:=b;
 t0:=0;t:=1;
 q:=trunc(n0/b);
 r:=n0-q*b;
 while r>0 do
  begin
   temp:=t0-q*t;
   if temp>=0 then temp:=temp mod n
     else temp:=n-((-temp) mod n);
   n0:=b0;b0:=r;t0:=t; t:=temp;
   q:=trunc(n0/b0); r:=n0-q*b0;
  end;
 if b0<>1 then writeln(b,' nu are inversa mod ',n)
      else writeln('inversa=',t);
 readkey;
End.