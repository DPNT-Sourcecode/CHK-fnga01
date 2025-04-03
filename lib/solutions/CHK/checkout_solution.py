
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        dict = {
            'A': 0,
            'B': 0,
            'C': 0,     
            'D': 0,
            'E': 0,
        }
        for a in skus:
            if a in dict:
                dict[a] += 1
            else:
                return -1
        # buy 2 E get a B for free            
        dict['B'] -= dict['E']//2        
    
        price = 0
        price += dict['C'] * 20 + dict['D'] * 15 + dict['E'] * 40
        price += dict['B']//2 * 45 + dict['B'] % 2 * 30
        # A: offers for buying 5 and 3, 5 takes priority
        price += dict['A']//5 * 200 + dict['A'] % 5 //3 * 130 + (dict['A'] % 5) % 3 * 50

        
        return price

