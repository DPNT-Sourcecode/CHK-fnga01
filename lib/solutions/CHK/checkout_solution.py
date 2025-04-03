
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        dict = {
            'A': 0,
            'B': 0,
            'C': 0,     
            'D': 0,
            'E': 0,
            'F': 0,
        }
        for a in skus:
            if a in dict:
                dict[a] += 1
            else:
                return -1
        # buy 2 E get a B for free            
        if dict['B'] > 0:
            dict['B'] -= dict['E']//2        
        #buy 2 F, get an F for free (need at least 3 in basket)
        if dict['F'] >= 3:
            dict['F'] -= dict['F']//3
        
    
        price = 0
        price += dict['C'] * 20 + dict['D'] * 15 + dict['E'] * 40 + dict['F'] * 10
        price += dict['B']//2 * 45 + dict['B'] % 2 * 30
        # A: offers for buying 5 and 3, 5 takes priority
        price += dict['A']//5 * 200 + dict['A'] % 5 //3 * 130 + (dict['A'] % 5) % 3 * 50

        return price


