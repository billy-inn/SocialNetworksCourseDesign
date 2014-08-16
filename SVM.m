% initialization
clear; close all; clc;

% load data
data = load('./data/dataset.txt');
X = data(:,1:4);
y = data(:,5);
coordinate = data(:,6:7);

% polynoimal features mapping

X = mapFeature(X,2);

% train by SVM

model = svmtrain(y,X);

predict = svmpredict(y,X,model);

% give the predict behaviors
fw = fopen('./data/SVMpredict.txt','wt+');

for i = 1:size(predict,1)
	if predict(i) == 1
		fprintf(fw, '%d %d\n', coordinate(i,1),coordinate(i,2));
	end
end

fclose(fw);
