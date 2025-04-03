
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
            'G': 0,     
            'H': 0,
            'I': 0,
            'J': 0,
            'K': 0,
            'L': 0,
            'M': 0,
            'N': 0,
            'O': 0,
            'P': 0,
            'Q': 0,
            'R': 0,
            'S': 0,
            'T': 0,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0,
        }
        for a in skus:
            if a in dict:
                dict[a] += 1
            else:
                return -1
        # buy 2 E get a B for free            
        if dict['B'] > 0:
            dict['B'] = max(dict['B'] - dict['E']//2, 0)        
        #buy 2 F, get an F for free (need at least 3 in basket)
        if dict['F'] >= 3:
            dict['F'] -= dict['F']//3
        # 3N get one M for free
        if dict['M'] > 0:
            dict['M'] = max(dict['M'] - dict['N']//3, 0)
        # 3R get one Q for free
        if dict['Q'] > 0:
            dict['Q'] = max(dict['Q'] - dict['R']//3, 0)
        # 3U get one U for free
        if dict['U'] >= 4:
            dict['U'] -= dict['U']//4
        #any 3 items of [S,T,X,Y,Z] for 45
        #favour customer: remove most expensive item among these, and calculate the cheaper ones
        #most expensive: Z > S,T,Y > X
        groupoffer = dict['S'] + dict['T'] + dict['X'] + dict['Y'] + dict['Z']
        if groupoffer >= 3:
            price +=
    
        price = 0
        price += dict['C'] * 20 + dict['D'] * 15 + dict['E'] * 40 + dict['F'] * 10 + dict['G'] * 20 + dict['I'] * 35 + dict['J'] * 60 +  dict['L'] * 90 + dict['M'] * 15 + dict['N'] * 40 + dict['O'] * 10 + dict['R'] * 50 + dict['S'] * 20 + dict['T'] * 20 + dict['U'] * 40 + dict['W'] * 20 + dict['X'] * 17 + dict['Y'] * 20 + dict['Z'] * 21
        
        
        
        price += dict['A']//5 * 200 + dict['A'] % 5 //3 * 130 + (dict['A'] % 5) % 3 * 50        
        price += dict['B']//2 * 45 + dict['B'] % 2 * 30
        price += dict['H']//10 * 80 + dict['H'] % 10 //5 * 45 + (dict['H'] % 10) % 5 * 10
        price += dict['K']//2 * 150 + dict['K'] % 2 * 80
        price += dict['P']//5 * 200 + dict['P'] % 5 * 50
        price += dict['Q']//3 * 80 + dict['Q'] % 3 * 30
        price += dict['V']//3 * 130 + dict['V'] % 3 //2 * 90 + (dict['V'] % 3) % 2 * 50

        return price



