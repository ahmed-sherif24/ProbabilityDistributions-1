import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import binom
def print_pause(message):

    print(message)

    time.sleep(2)
def binomial_drv ():
# Set the parameters
    n_binomial = 10    # Number of trials
    p_binomial = 0.25     # Probability of success
    print("A multple choice exam consist of 10 questions each with 4 choice ")
    print_pause(" what is the probabilty that you correctly answered at most 7 questions ?")
    print_pause("So we can considered that the best random variable to solve it is the Bibnomial random variable")
    print_pause("Because in this case we have only two conditions correct answer or not ")
    print_pause("The probabilty of success is 0.25 ")
    print_pause("The number of trials is 10 ")
     # Calculate mean and variance
    mean_binomial = binom.mean(n=n_binomial, p=p_binomial)
    variance_binomial = binom.var(n=n_binomial, p=p_binomial)
    

    # Generate binomial random variable
    binomial_rvs = binom.rvs(n=n_binomial, p=p_binomial, size=1000)

    # Calculate PMF and CDF
    k_values = np.arange(0, n_binomial + 1)
    pmf_values = binom.pmf(k_values, n=n_binomial, p=p_binomial)
    cdf_values = binom.cdf(k_values, n=n_binomial, p=p_binomial)

    # Calculate mean and variance
    mean_binomial = binom.mean(n=n_binomial, p=p_binomial)
    variance_binomial = binom.var(n=n_binomial, p=p_binomial)

    
    # Display mean and variance
    print_pause(f"The MEAN value   {mean_binomial}")
    print_pause(f"The VARIANCE value =  {variance_binomial}")
    cdf = binom.cdf(7, n=n_binomial, p=p_binomial)
    print_pause("To calculate the probabilty that you correctly answered at most 7 questions")
    print_pause("We must calculate the CDF of 7 ")
    print_pause(f"the CDF OF = {cdf}")
    
    time.sleep(4)
    
    print_pause("Now lets get this value from the CDf diagram : ")
    

    
    # Plot PMF and CDF
    
    time.sleep(3)
    
    
    showx =int(input("show ?"))
    if showx ==1:
       
        plt.figure(figsize=(12, 6))

        plt.subplot(121)
        plt.bar(k_values, pmf_values, align='center', alpha=0.75, color = 'red')
        plt.title('Binomial Distribution PMF')
        plt.xlabel('k')
        plt.ylabel('Probability')

        plt.subplot(122)
        plt.step(k_values, cdf_values, where='post')
        plt.title('Binomial Distribution CDF')
        plt.xlabel('k')
        plt.ylabel('Probability')
        plt.tight_layout()
        plt.show()
   

    
    
    
print (" choose the number of Example that you want : ")
print("1- Binomial rabdom variable ")
print("2- Geomitric random variable ")

choose = int(input("?"))
if choose == 1 :
    binomial_drv()
