Program chei_fluide_2022_;
uses crt;
var a,n,cod:longint;
    s,tc:string;
    alfabet:array[0..200] of char;
    Im,c:array[1..255] of integer;
    f,f1,g,alf:text;

Procedure Init;
{initierea alfabetului}
var i:integer;
    x:char;
begin
 i:=0;
 while not(eof(alf)) do
  begin
   read(alf,x);
   alfabet[i]:=x;
   inc(i);
  end;
    n:=i;
end;
Procedure Numar_ordine(s1:string);
var i,j,k:integer;
begin
  k:=length(s1);
  for i:=1 to k do
   begin
    for j:=0 to n-1 do
     if s1[i]=alfabet[j] then Im[i]:=j;
    {write(Im[i],' ');}
   end;
   writeln;
end;

Procedure Cript;
var i,k,j:integer;
begin
 k:=length(s); cod:=a;
 for i:=1 to k do begin
   c[i]:=(Im[i]+cod) mod n;
   cod:=c[i];end;
 tc:='';
 for i:=1 to k do
  for j:=0 to n-1 do
   if c[i]=j then tc:=tc+alfabet[j];
 writeln(g,tc);
end;

Procedure Decript;
var i,k,j:integer;
begin
 k:=length(tc);
 cod:=a;
 for i:=1 to k do begin
   c[i]:=(Im[i]-cod) mod n;
   if c[i]<0 then c[i]:=c[i]+n;
   cod:=Im[i];end;
 tc:='';
 for i:=1 to k do
  for j:=0 to n-1 do
   if c[i]=j then tc:=tc+alfabet[j];
 writeln(f1,tc);
end;

Begin
 clrscr;
 write('Introdu cheia k=');readln(a);
 assign(alf,'alfabet.txt');
 reset(alf);
 Init;
 close(alf);
 assign(f,'clar.txt');reset(f);
 assign(g,'cript.txt');rewrite(g);
 while not(eof(f)) do
  begin
   readln(f,s);
   Numar_ordine(s);
   Cript;
  end;
 close(f);close(g);
 assign(g,'cript.txt');reset(g);
 assign(f1,'clar1.txt');rewrite(f1);
 while not(eof(g)) do
  begin
   readln(g,tc);
   Numar_ordine(tc);
   Decript;
  end;
 close(f1);close(g);
 readkey;
End.