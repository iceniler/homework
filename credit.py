class Credit:
    
    def __init__(self):
        self.cards = {}

    def add_card(self, cc, limit):
        if(len(str(cc))>16):
            return False
        if(not self.cards[cc]):
            sum = 0 
            for x in range(0, len(str(cc)-2):
                sum = sum + int(str(cc).index(x))

            if(sum%10 == cc%10):
                self.cards[cc] = {'limit':limit, 'amount':0, 'records':[]}
                return True

        return False

    def limit(self, cc):
        return self.cards[cc]['limit']

    def balance(self, cc):
        return self.cards[cc]['amount']

    def charge(self, cc, amnt, desc):
        if(desc != 'Payment'):
            if(self.cards[cc]['amount'] + amnt < self.cards[cc]['limit']):
                self.cards[cc]['amount'] + amnt
                self.cards[cc]['records'].list(0, ('Charge', amnt, desc))
                return True
        return False

    def payment(self, cc, amnt):
        self.cards[cc]['amount'] - amnt
        self.cards[cc]['records'].list(0, ('Payment', amnt, desc))

    def reissue(self,cc, new_cc):
        self.add_card(new_cc, self.cards[cc].limit())
        self.cards[new_cc]['amount'] = self.cards[cc]['amount']
        self.cards[new_cc]['records'] = self.cards[cc]['records']
        del self.cards[cc]

    def transcations(self, cc):
        return self.cards[cc][0:10]

    def __contains__(self, cc):
        return self.cards.__contains__()

    def __iter__(self):
        return self.cards.__iter__()

    def __len__(self):
        return self.cards.__len__()
