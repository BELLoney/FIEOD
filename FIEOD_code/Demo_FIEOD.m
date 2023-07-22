clc;
clear all;
format shortG
% currentFolder = pwd;
% addpath(genpath(currentFolder));
data_nameori='Example';
data_name='Example';

eval(['load ' data_nameori ';']);

Dataori=Example;

trandata=Dataori;
trandata(:,2:3)=normalize(trandata(:,2:3),'range');
delta=1;

tic
out_factor=FIEOD(trandata,delta)
toc
tic
out_factor_v0=FIEOD_v0(trandata,delta)
toc

