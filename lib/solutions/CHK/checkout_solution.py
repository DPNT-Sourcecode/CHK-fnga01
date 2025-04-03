
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        skus.sort()
        dict = {
            'A': 0,
            'B': 0,
            'C': 0,     
            'D': 0,
        }
        for a in skus:
            if a in dict:
                dict[a] += 1
        
        
        return 
