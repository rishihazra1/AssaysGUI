from numpy import array, polyfit

x_terms = []
y_terms = []

def get_best_fit_line(x_terms, y_terms):
    x = array(x_terms)
    y = array(y_terms)
    a, b, c = polyfit(x, y, 2)
    return a, b, c

def get_r_squared(x_terms, y_terms, a, b, c):
    unexplained_variance = 0
    total_variance = 0
    sum = 0
    for element in range(0, len(y_terms)):
        sum += y_terms[element]
    average_actual = sum/len(y_terms)
    for index in range(0, len(x_terms)):
        actual = y_terms[index]
        predicted = a*(x_terms[index])**2 + b*(x_terms[index]) + c
        total_variance += (actual - average_actual)**2
        unexplained_variance += (predicted - actual)**2
    r_squared = 1 - (unexplained_variance/total_variance)
    print("r_squared: " + str(r_squared))
    return r_squared
