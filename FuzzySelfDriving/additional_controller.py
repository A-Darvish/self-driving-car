from numpy import linspace


class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """
    def fuzzification(self, center_dist):
        close, moderate, far = 0, 0, 0
        
        if 0 <= center_dist < 50:
            close = (50 - center_dist) / 50
        
        if 40 < center_dist <= 50:
            moderate = (center_dist - 40) / 10
        if 50 <= center_dist < 100:
            moderate = -(center_dist - 100) / 50
        
        if 90 < center_dist <= 200:
            far = (center_dist - 90) / 110
        if center_dist > 200:
            far = 1
        
        return close, moderate, far

    

    def inference(self, center_dist):
        close, moderate, far = self.fuzzification(center_dist)
        low = close
        medium = moderate
        high = far
        return low, medium, high
    

    def defuzzification(self, center_dist) :
        def max_speed(x) :
            low2, medium2, high2 = 0, 0, 0
            low, medium, high = self.inference(center_dist)
            if 0 < x <= 5:
                low2 = min(low, x / 5)
            if 5 <= x < 10:
                low2 = min(low, -(x - 10) / 5)
            
            if 0 < x <= 15:
                medium2 = min(medium, x / 15)
            if 15 <= x < 30:
                medium2 = min(medium, -(x - 30) / 15)
            
            if 25 < x <= 30:
                high2 = min(high, (x - 25) / 5)
            if 30 <= x < 90:
                high2 = min(high, -(x - 90) / 60)
            
            return max(low2, medium2, high2)

        soorat = 0.0
        makhraj = 0.0
        X = linspace(0, 90, 900)
        for i in X:
            U = max_speed(i)
            soorat += U * i
            makhraj += U
        center = 0.0
        if makhraj != 0:
            center = 1.0 * float(soorat)/float(makhraj)

        return center

        

    def __init__(self):
        pass
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        return self.defuzzification(center_dist)
        # return 30
    