import numpy
import scipy.stats

vowels = numpy.loadtxt('h95_ih_iy_adult_male.txt')
vowel_iy = vowels[:,0] # vowel in "heed"
vowel_ih = vowels[:,1] # vowel in "hid"
vowel_all = numpy.hstack((vowel_iy, vowel_ih))

ground_truth = (['iy'] * 45) + (['ih'] * 45)

# TODO_1
vowel_iy_mu = 1
# TODO_1
vowel_iy_sigma = 1

# TODO_1
vowel_ih_mu = 1
# TODO_1
vowel_ih_sigma = 1

# Mean standard deviation
# Note: This formula only works because we have an equal number of vowels
mn_sigma = numpy.mean([vowel_iy_sigma, vowel_ih_sigma])

def numerator(x, category):
    
    py_given_k = 1/2
    
    if category == 'iy':
        # TODO_1
        iy_dens = 1
        return iy_dens * py_given_k
    else:
        # TODO_1
        ih_dens = 1
        return ih_dens * py_given_k
        
def denominator(x):
    # TODO_2
    return 1

def custom_lda(x):
    # TODO_3
    d = 1

    p_iy = 1
    p_ih = 1
    
    return [p_iy, p_ih]
    
def classify(x):
    p = custom_lda(x)
    if p[0] > p[1]:
        return 'iy'
    else:
        return 'ih'
        
def test_numerator():
    ground = [0.0059365432895529605, 0.0030048840252944256, 0.0009156110562090575, 0.0020967570731761542]
    test_vals = [numerator(x, 'iy') for x in vowel_iy[:2]] + [numerator(x, 'ih') for x in vowel_ih[:2]]
    print('Numerator probably okay?', numpy.allclose(ground, test_vals))
    
def test_denom():
    ground = [0.005956721005603021, 0.003005956998776884, 0.005315136112995771, 0.004652912527005321]
    test_vals = [denominator(x) for x in vowel_iy[:2]] + [denominator(x) for x in vowel_ih[:2]]
    print('Denominator probably okay?', numpy.allclose(ground, test_vals))
    
def test_lda():
    ground = [[0.9966126135450895, 0.0033873864549105854], [0.9996430509541904, 0.00035694904580959674], [0.8277351629866367, 0.17226483701336323], [0.5493667544776183, 0.4506332455223817]]
    ground = [y for x in ground for y in x]
    test_vals = [custom_lda(x) for x in vowel_iy[:2]] + [custom_lda(x) for x in vowel_ih[:2]]
    test_vals = [y for x in test_vals for y in x]
    print('LDA probably okay?', numpy.allclose(ground, test_vals))
    
def accuracy():
    preds = [classify(x) for x in numpy.hstack((vowel_iy, vowel_ih))]
    print('Accuracy:', sum(yhat == y for yhat, y in zip(preds, ground_truth)) / 90)

# TODO_any:
# Comment/uncomment these as needed
test_numerator()
# test_denom()
# test_lda()
# accuracy() # should be 0.9

# # Uncomment when classification and LDA are working correctly
# # empirically determine decision boundary
# test_values = numpy.linspace(min(vowel_all), max(vowel_all), num=1000)
# diffs = []
# for x in test_values:
    # p1, p2 = custom_lda(x)
    # diffs.append(abs(p1 - p2))
# print('Decision boundary at approximately', test_values[numpy.argmin(diffs)])