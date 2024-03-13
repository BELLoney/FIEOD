clc;
clear all;
format short

load Example.mat

Dataori=Example;

trandata=Dataori;
trandata(:,2:3)=normalize(trandata(:,2:3),'range');

delta=1;
out_factors=FIEOD(trandata,delta)
