from numpy import linspace


def defuzzification() :
 
    def max_rotate(x):
        high_right_new, low_right_new, nothing_new, low_left_new, high_left_new = 0,0,0,0,0
        high_right, low_right, nothing, low_left, high_left = (0, 1, 0, 0, 0)
        
        if x <= -20:
            high_right_new = min(high_right, (x + 50)/30)
        if -20 < x < -5 :
            high_right_new = min(high_right, (-5 -x)/15)
            
            
        if -20 < x <= -10:
            low_right_new = min(low_right, (x + 20)/10)
        if -10 < x < 0 :
            low_right_new = min(low_right, (-x)/10)
            
            
            
        if -10 < x <= 0 :
            nothing_new = min(nothing, (x + 10)/ 10)
        if 0 < x < 10:
            nothing_new = min(nothing, (-x + 10)/10)
                
                
        if 0 < x <= 10:
            low_left_new = min(low_left, x/10)
        if 10 < x < 20:
            low_left_new = min(low_left, (-x + 20)/10)
            
                
        if 5 < x <= 20 :
            high_left_new = min(high_left, (x - 5)/15)
        if 20 < x < 50:
            high_left_new = min(high_left, (-x + 50)/30)

        return max(high_right_new, low_right_new, nothing_new, low_left_new, high_left_new)
    

    soorat = 0.0
    makhraj = 0.0
    X = linspace(-50, 50, 1000)
    for i in X:
        U = max_rotate(i)
        soorat += U * i 
        makhraj += U 
    center = 0.0
    if makhraj != 0:
        center = 1.0 * float(soorat)/float(makhraj)
    return center        


print(defuzzification())