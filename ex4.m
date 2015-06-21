clear ; close all; clc

input_layer_size  = 400;  % 20x20 Input Images of Digits
hidden_layer_size = 30;   % 25 hidden units
num_labels = 26;          % 10 labels, from 1 to 10   

fprintf('Loading and Visualizing Data ...\n')

load('ex4data1.mat');
im = imread("img");
im = double(im(:)');
X = [X; im];
y = [y; 1];
m = size(X, 1);

sel = randperm(size(X, 1));
sel = sel(1:100);

%displayData(X(sel, :));

%fprintf('Program paused. Press enter to continue.\n');
%pause;


fprintf('\nInitializing Neural Network Parameters ...\n')

initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

fprintf('\nTraining Neural Network... \n')
%pause;

options = optimset('MaxIter', 50);
lambda = 1;


costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, X, y, lambda);


[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);


Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));



%load("grads.mat") %comment to train neural nets

pred = predict(Theta1, Theta2, X)

predRowSize = size(pred,1);
alphabet = pred(predRowSize);
save -text result.txt alphabet

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);
