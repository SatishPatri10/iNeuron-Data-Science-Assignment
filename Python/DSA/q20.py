# pip install scipy

from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value
    
sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]

p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)