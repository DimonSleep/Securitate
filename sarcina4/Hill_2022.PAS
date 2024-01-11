Program cript_Hill;
uses crt;
type
    vector=array[1..255] of integer;
    matrice=array[1..20,1..20] of integer;
var b,lung,supl,a,n,k,i,j:byte;
    s,tc:string;
    alfabet:array[0..200] of char;
    n_o,c,lin:vector;
    f,g,h,alf:text;
    M_cript, M_decript:matrice;

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
    n:=i-1;
end;
Procedure Numar_ordine(s1:string);
var i,j:integer;
begin
  b:=length(s1);
  for i:=1 to b do
   begin
    for j:=0 to n do
     if s1[i]=alfabet[j] then n_o[i]:=j;
   end;
{  for i:=1 to b do write(n_o[i],' ');
  writeln;}
end;

Procedure Inmultire_lin_matr(m:matrice);
var lin1:vector;
    i:byte;
    S:integer;
begin
  for i:=1 to k do
    begin
      S:=0;
      for j:=1 to k do
        S:=S+lin[j]*m[j,i];
      lin1[i]:=S mod n;
    end;
 lin:=lin1;
end;

Procedure Cript;
var i,j,t:integer;
    mc:string;
begin
 i:=1;tc:='';
 while i<= b-2 do
  begin
    for j:=1 to k do lin[j]:=n_o[j+i-1];
    Inmultire_lin_matr(M_cript);
    for t:=1 to k do tc:=tc+alfabet[lin[t]];
    i:=i+3;
  end;
 writeln(h,tc);
end;

Procedure Decript;
var i,j,t:integer;
    mc:string;
begin
 i:=1;tc:='';
 while i<= b-2 do
  begin
    for j:=1 to k do lin[j]:=n_o[j+i-1];
    Inmultire_lin_matr(M_decript);
    for t:=1 to k do tc:=tc+alfabet[lin[t]];
    i:=i+3;
  end;
 writeln(f,tc);
end;

Begin
 clrscr;
 assign(alf,'alfabet.txt'); reset(alf);
 Init;
 writeln('n=',n);
 close(alf);
 assign(f,'clar.txt');reset(f);
 assign(g,'cheia.txt');reset(g);
 readln(g,k);
 for i:=1 to k do begin
  for j:=1 to k do
   read(g,M_cript[i,j]);
  readln(g); end;
 for i:=1 to k do begin
  for j:=1 to k do
   read(g,M_decript[i,j]);
  readln(g); end;

{ for i:=1 to k do begin
  for j:=1 to k do
   write(M_decript[i,j]);
  writeln; end;
  readkey;}

 assign(h,'cript.txt');rewrite(h);
 while not(eof(f)) do
  begin
   readln(f,s);
   lung:=length(s);
   supl:=lung mod k;
   if supl<>0 then
     for i:=1 to k-supl do s:=s+'Q';
   Numar_ordine(s);
   Cript;
  end;
 close(f);close(g);close(h);

 assign(h,'cript.txt');reset(h);
 assign(f,'clar1.txt');rewrite(f);
 while not(eof(h)) do
  begin
   readln(h,s);
   lung:=length(s);
   Numar_ordine(s);
   Decript;
  end;
 close(f);close(h);
 readkey;
End.