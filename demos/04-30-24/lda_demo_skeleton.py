import numpy
import scipy.stats
import pandas as pd

df_vowel = pd.read_csv(r"lda_sample_data.csv",encoding='utf-8')

vowel_all = df_vowel['F1']
ground_truth = df_vowel['vowel']

vowel_i = df_vowel['F1'].head(32)
vowel_a = df_vowel['F1'].iloc[32:]
print(vowel_i)
print(vowel_a)

# TODO_1
vowel_i_mu = numpy.mean(vowel_i)

vowel_i_sigma = numpy.std(vowel_i, ddof=1)

# TODO: calculate the mean of vowel a
vowel_a_mu = None
# TODO: calculate the standard deviation of vowel a
vowel_a_sigma = None

# Mean standard deviation
# Note: This formula only works because we have an equal number of vowels
# LDA assumes the two categories have the same standard deviation
mn_sigma = numpy.mean([vowel_i_sigma, vowel_a_sigma])

def numerator(x, category):

    #P(Y=k) = 1/2, because there are only two vowel categories
    py_given_k = 1/2

    # Calculate P(x | Y = K) K is the vowel i
    if category == 'i':
        i_dens = scipy.stats.norm.pdf(x, vowel_i_mu, mn_sigma)
        return i_dens * py_given_k
    # Calculate P(x | Y = K) K is the vowel a
    else:
        # TODO: Calculate the pdf of the normal distribution of [a]
        a_dens = None
        return a_dens * py_given_k
        
def denominator(x):
    # the return values in the numerator() function is the denominator.
    # assign values iy and ih to category in the numerator function
    # TODO: return the deminator, which is the p(y|i) + the p(y|a)
    return denominator

def custom_lda(x):

    # assign the denominator value to d
    d = denominator(x)

    #p_i is P(Y=i|x)
    p_i = numerator(x, 'i') / d

    #p_a is P(Y=a|x)
    # TODO: calculate p_a
    p_a = None
    
    return [p_i, p_a]
    
def classify(x):

    p = custom_lda(x)

    # TODO: write a if condition. If the first probability returned from custom_lda is larger, the vowel is i;
    #  if the second probability is larger, the vowel is a.

    #if given the F1 value, the probability of being in i category is higher, classify this datapoint as i
    #if given the F1 value, the probability of being in a category is higher, classify this datapoint as a
    if p[0] > p[1]:
        pass
        
def test_numerator():
    #The ground truth was calculated manually, to make sure our numerator is working ok.
    ground = [0.0006368694390322965, 0.0006686691014698572, 0.0007516888194454205, 0.0007391989596789381]
    test_vals = [numerator(x, 'i') for x in vowel_i[:2]] + [numerator(x, 'a') for x in vowel_a[:2]]
    #numpy.allclose() function is used to find if two arrays are element-wise equal within a tolerance
    print(test_vals)
    print('Numerator probably okay?', numpy.allclose(ground, test_vals))
    
def test_denom():
    #The ground true was calculated manually, to make sure our denominator is working ok.
    ground = [0.0010318799965939836, 0.0010233825507172441, 0.0009480104596025087, 0.0009769790094216653]
    test_vals = [denominator(x) for x in vowel_i[:2]] + [denominator(x) for x in vowel_a[:2]]
    #numpy.allclose() function is used to find if two arrays are element-wise equal within a tolerance
    print('Denominator probably okay?', numpy.allclose(ground, test_vals))

def test_lda():
    ground = [[0.617193318151788, 0.3828066818482119], [0.6533911497721123, 0.3466088502278875],
     [0.20708805284638301, 0.7929119471536169], [0.24338296672666898, 0.7566170332733311]]

    #shorthand for: for x in ground: for y in x
    #because the ground list has nested list
    #read from the left most for to the right
    ground = [y for x in ground for y in x]
    test_vals = [custom_lda(x) for x in vowel_i[:2]] + [custom_lda(x) for x in vowel_a[:2]]
    print(test_vals)
    test_vals = [y for x in test_vals for y in x]
    print('LDA probably okay?', numpy.allclose(ground, test_vals))

def accuracy():
    #compare the classification result with the ground truth
    preds = [classify(x) for x in numpy.hstack((vowel_i, vowel_a))]
    print('Accuracy:', sum(yhat == y for yhat, y in zip(preds, ground_truth)) / 64)
        
        
# Comment/uncomment these as needed
test_numerator()
test_denom()
#test_lda()
#accuracy()

# empirically determine decision boundary
#numPy.linspace() returns an array of evenly spaced values within the specified interval [start, stop].
test_values = numpy.linspace(min(vowel_all), max(vowel_all), num=1000)
diffs = []
for x in test_values:
    p1, p2 = custom_lda(x)
    diffs.append(abs(p1 - p2))
#The numpy.argmin() method returns indices of the min element of the array.
#Essentially, it returns the indice in test_value where the probability between two categories is the smallest.
#Empirically, it is finding the most ambiguous token on a continuum between the min F1 and max F1
print('Decision boundary at approximately', test_values[numpy.argmin(diffs)])