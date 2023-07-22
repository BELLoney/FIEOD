clc;
clear all;

data_nameori='hepatitis_2_9_variant1';
data_name='hepatitis_2_9_variant1';

eval(['load ' data_nameori ';']);

Dataori=trandata;

trandata=Dataori;
%trandata(:,2:3)=normalize(trandata(:,2:3),'range');
delta=1;

tic
out_factor_v0=FIEOD_v0(trandata,delta)
toc
tic
out_factor=FIEOD(trandata,delta)
toc
