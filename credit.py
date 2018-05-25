class Credit:
    
    def __init__(self):
        self.cards = {}

    def add_card(self, cc, limit):
        if len(str(cc))>16:
            return False
        if not self.cards.__contains__(cc):
            sumnum = 0 
            x = 0
            while x <= len(str(cc))-2:
                sumnum = sumnum + int(str(cc)[x])
                x = x+1

            print("%s\n%s" % (sumnum, cc))
            if int(sumnum)%10 == int(cc)%10:
                self.cards[cc] = {'limit':limit, 'amount':0, 'records':[]}
                return True

        return False

    def limit(self, cc):
        if not self.cards.__contains__(cc):
            return None 
        return self.cards[cc]['limit']

    def balance(self, cc):
        if not self.cards.__contains__(cc):
            return None
        return self.cards[cc]['amount']

    def charge(self, cc, amnt, desc):
        if not self.cards.__contains__(cc):
            return False
        if desc != 'Payment':
            if self.cards[cc]['amount'] + amnt < self.cards[cc]['limit']:
                self.cards[cc]['amount'] = self.cards[cc]['amount']
                self.cards[cc]['records'].insert(0, ('Charge', amnt, desc))
                return True
        return False

    def payment(self, cc, amnt):
        if not self.cards.__contains__(cc):
            return False
        self.cards[cc]['amount'] - amnt
        self.cards[cc]['records'].insert(0, ('Payment', amnt, 'payment'))
        return True

    def reissue(self,cc, new_cc):
        if not self.cards.__contains__(cc):
            return False
        self.add_card(new_cc, self.cards[cc].limit())
        self.cards[new_cc]['amount'] = self.cards[cc]['amount']
        self.cards[new_cc]['records'] = self.cards[cc]['records']
        del self.cards[cc]
        return True

    def transcations(self, cc):
        if not self.cards.__contains__(cc):
            return False
        return self.cards[cc][0:10]

    def __contains__(self, cc):
        return self.cards.__contains__()

    def __iter__(self):
        return self.cards.__iter__()

    def __len__(self):
        return self.cards.__len__()
    

def update_accounts(credit,  filename):
    fp = open(filename, 'r')
    lines = fp.readlines()
    for line in lines:
        info = line.split()
        if 'open'==info[0] : 
            if not credit.add_card(int(info[1]), int(info[2])):
                print("Bad Transaction: %s\n" % (line, ))
        elif 'charge' == info[0] :
            if not credit.charge(int(info[1]), int(info[2]), info[3]):
                print("Bad Transaction: %s\n" % (line ))
        elif 'payment' == info[0] :
            if not credit.payment(int(info[1]), int(info[2])):
                print("Bad Transaction: %s\n" % (line ))

