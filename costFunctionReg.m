function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

J = 0;
grad = zeros(size(theta));

h = 1.0./(1+exp(-X*theta));
f = ones(size(theta));
f(1) = 0;
T = f.*theta;
J = 1.0/m*(-y'*log(h) - (1-y)'*log(1-h)) + lambda/(2*m)*T'*T;
grad = 1.0/m*X'*(h-y) + lambda/m*T;

end
