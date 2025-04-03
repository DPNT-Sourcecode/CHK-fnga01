
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
        price = 0
        price += dict['C'] * 20 + dict['D'] * 15
        price += dict['B']//2 * 45 + dict['B'] % 2 * 30
        price += dict['A']//3 * 130 + dict['A'] % 3 * 50

        
        return price
