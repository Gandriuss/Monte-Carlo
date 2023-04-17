import random
import time

def monte_carlo(num_trials, prob_of_getting_number):

    list_of_trial_numbers = []      # holds each one of the experiments 

    for i in range(num_trials):
        total_tosses = 0
        heads = 0
        while heads < 2:                                
            total_tosses += 1
            toss = random.random()                      # generate a toss [0,1]
            if toss <= prob_of_getting_number:         # get a number
                heads = 0
            elif toss > prob_of_getting_number:        # get a head
                heads += 1

        list_of_trial_numbers.append(total_tosses)
                
    return sum(list_of_trial_numbers) / num_trials     # Take the average

num_trials = 1000000
prob_of_getting_number = 0.9
start_time = time.time()

expected_tosses = monte_carlo(num_trials, prob_of_getting_number)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"-----------------------------------------------------------------------------------------")
print(f" \n Expected number of tosses until two successive heads: {expected_tosses} \n time of cumputation: {elapsed_time} seconds")
