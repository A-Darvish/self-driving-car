from numpy import linspace


class FuzzyController:

    def fuzzification(self, left_dist, right_dist):
        close_L, moderate_L, far_L, close_R, moderate_R, far_R = 0,0,0,0,0,0

        if left_dist < 50 :
            close_L = -0.02*left_dist + 1
        
        if 35 < left_dist < 50 :
            moderate_L = (left_dist - 35)/15
        if 50 <= left_dist < 65 :
            moderate_L = (65 - left_dist)/15
        
        if 50 < left_dist <= 100 :
            far_L = 0.02*left_dist - 1
        


        if right_dist < 50 :
            close_R = -0.02*right_dist + 1
        
        if 35 < right_dist < 50 :
            moderate_R = (right_dist - 35)/15
        if 50 <= right_dist < 65 :
            moderate_R = (65 - right_dist)/15
        
        if 50 < right_dist <= 100 :
            far_R = 0.02*right_dist - 1

        return close_L, moderate_L, far_L, close_R, moderate_R, far_R
        

    def inference(self, left_dist, right_dist) :
        close_L, moderate_L, far_L, close_R, moderate_R, far_R = self.fuzzification(left_dist, right_dist)
        low_right = min(close_L, moderate_R)
        high_right = min(close_L, far_R)
        low_left = min(moderate_L, close_R)
        high_left = min(far_L, close_R)
        nothing = min(moderate_L, moderate_R)

        return high_right, low_right, nothing, low_left, high_left 


    def defuzzification(self, left_dist, right_dist) :

        def max_rotate(x):
            high_right_new, low_right_new, nothing_new, low_left_new, high_left_new = 0,0,0,0,0
            high_right, low_right, nothing, low_left, high_left = self.inference(left_dist, right_dist)
            
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
    

    def __init__(self):
        pass


    def decide(self, left_dist,right_dist):
        
        return self.defuzzification(left_dist, right_dist)
    