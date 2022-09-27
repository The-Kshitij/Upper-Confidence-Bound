import pandas as pd;
import numpy as np;
import math;

import matplotlib.pyplot as plt;

path = input("Enter the path: ");
dataset = pd.read_csv(path);

variables = len(dataset.iloc[1,:]);
sum_of_rewards = [0] * variables;
num_of_selections = [0] * variables;
total_rewards = 0;
selected_ads = [];
iterations = int(input("Enter the number of iterations: "));

#applying the ucb method
for i in range(0, iterations):
  max_ucb = -math.inf;
  ad = 0;
  for j in range(0, variables):
    if (num_of_selections[j] > 0):      
      r_avg = sum_of_rewards[j] / num_of_selections[j];
      delta = math.sqrt(1.5 * math.log(i+1) / num_of_selections[j]);
      ucb = r_avg + delta;
    else:
      ucb = math.inf;
    if ucb > max_ucb:
      max_ucb = ucb;
      ad = j;
  selected_ads.append(ad);
  num_of_selections[ad] += 1;
  sum_of_rewards[ad] += dataset.values[i,ad];
  total_rewards += dataset.values[i,ad];

plt.hist(selected_ads);
plt.xlabel("List of ads");
plt.ylabel("Number of times clicked");
plt.show();