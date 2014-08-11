% initialization
clear; close all; clc;

%% Load data
%  The first four columns contain the feature values
%  , the fifth column contains the label
%  and the last two column contains the userId and goodId.

data = load('./data/dataset.txt');
X = data(:,1:4);
y = data(:,5);
coordinate = data(:,6:7);

% polynomial features mapping

X = mapFeature(X,4);

% initial the parameters, lambda and the options

initial_theta = zeros(size(X,2),1);

lambda = 10000;

options = optimset('GradObj','on','MaxIter',400);

% use fminunc function to minizize the cost function

[theta,J,exit_flag] = ...
	fminunc(@(t)(costFunctionReg(t,X,y,lambda)),initial_theta,options);

% give the predicted behaviors

Z = 1.0./(1.0 + exp(-X*theta));
m = size(Z,1);
fw = fopen('./data/predict.txt','wt+');

for i = 1:m
	if Z(i,1) > 0.500001
		fprintf(fw,'%d %d\n',coordinate(i,1),coordinate(i,2));
	end
end

fclose(fw);
