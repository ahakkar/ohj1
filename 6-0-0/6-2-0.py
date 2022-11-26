# -*- encoding: utf-8 -*-
'''
@File    :   6-2-0.py
@Time    :   15/10/2022, 11:38:12
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Asks sea level measurements from user. Prints values based on measurements.

11.38-> 12:35
'''

DECIMAL_PRECISION = 2

def get_min_value(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, min value in list
    """
    minimum: float
    minimum = min(measurements)
    
    return minimum

def get_max_value(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, max value in list
    """
    maximum: float
    maximum = max(measurements)
    
    return maximum

def get_median(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, median value of list
    """
    
    median: float
    measurements = sorted(measurements)
    
    # even
    if len(measurements) % 2 == 0:
        middle1 = measurements[int(len(measurements)/2-1)]
        middle2 = measurements[int(len(measurements)/2)]
        median = (middle1+middle2)/2
    # odd
    else:        
        middle = int(len(measurements)/2)        
        median = measurements[middle]
        
    return median

def get_mean(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, mean value of list
    """
    mean: float
    mean = sum(measurements)/len(measurements)
    
    return mean

def get_std_dev(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, stddev of list values
    """
    from math import sqrt
    
    stddev: float
    stddev = sqrt(get_variance(measurements))
    
    return stddev

def get_variance(measurements:list) -> float:
    """
    param : List, measurements
    return: Float, variance calcualted from measurements
    """
    values: list = []
    mean: float
    variance: float
    
    mean = get_mean(measurements)
    
    for val in measurements:
        values.append(pow((val-mean), 2))
    
    variance = 1/(len(measurements)-1)*sum(values)
    
    return variance

def read_measurements() -> tuple:
    """
    param : none
    return: tuple(list of measurements, bool over 1 measurement in list?)
    
    Collects a list of measurements from user. Min 2 measurements.
    """
    is_good: bool
    
    measurements: list = []
    is_good = False
    
    print("Enter seawater levels in centimeters one per line.\n" +
          "End by entering an empty line.")
    
    while(True):
        user_input = input()
        if len(user_input) > 0:
            measurements.append(float(user_input))
        elif len(measurements) < 2:
            print("Error: At least two measurements must be entered!")
            break
        else:
            is_good = True
            break
                
    return (measurements, is_good)

def print_measurements(measurements:list) -> None:
    """
    param : List, measurements
    return: none
    
    Print data based on measurements
    """
    
    print(f"Minimum: {get_min_value(measurements):.{DECIMAL_PRECISION}f} cm")
    print(f"Maximum: {get_max_value(measurements):.{DECIMAL_PRECISION}f} cm")
    print(f"Median: {get_median(measurements):.{DECIMAL_PRECISION}f} cm")
    print(f"Mean: {get_mean(measurements):.{DECIMAL_PRECISION}f} cm")
    print(f"Deviation: {get_std_dev(measurements):.{DECIMAL_PRECISION}f} cm")    
    

def main() -> None:
    measurements: list = []
    
    # 2 item tuple with: list, bool
    results = read_measurements()
    measurements = results[0]
    
    # analyze data only when more than 1 measurement given by user
    if results[1]:     
        print_measurements(measurements)
    
    # August 2022, Pohnpei, Federal States of Micronesia
    measurements1 = [        
        877, 893, 899, 906, 908, 896, 884, 874,
        867, 882, 892, 888, 889, 886, 895, 902,
        892, 887, 876, 860, 865, 877, 867, 865,
        892, 901, 916, 922, 925, 947, 962
    ]
    
    measurements2 = [234.5, 678.9, 789, 345.6, 456.7, 567.8, 123.4]
    
    measurements3 = [123, 456, 789, 123]    

if __name__ == "__main__":
    main()
