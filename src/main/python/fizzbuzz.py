class fizzBuzz:
    def __init__(self):
        self.num_list = []
        self.start = None
        self.end = None
        self.int_count = 0
        self.lucky_count = 0
        self.fizz_count = 0
        self.buzz_count = 0
        self.fizzbuzz_count = 0

    def getFizzBuzz(self, val):
        if '3' in str(val):
            self.lucky_count += 1
            return 'lucky'
        elif val == 0:
            return '0'
        elif val%3 == 0 and val%5 == 0:
            self.fizzbuzz_count += 1
            return 'fizzbuzz'
        elif val%3 == 0:
            self.fizz_count += 1
            return 'fizz'
        elif val%5 == 0:
            self.buzz_count += 1
            return 'buzz'
        else:
            self.int_count += 1
            return str(val)

    def setFizzBuzzStart(self, val):
        self.start = val

    def setFizzBuzzEnd(self, val):
        self.end = val

    def setList(self):
        if self.start == None:
            raise ValueError("no start value set")
        elif self.end == None:
            raise ValueError("no end value set")
        else:
            if self.start <= self.end:
                self.num_list = [i for i in range(self.start, self.end+1)]
            else:
                self.num_list = [i for i in range(self.start, self.end-1, -1)]

    def makeFizzBuzz(self):
        if self.num_list == []:
            return
        for i in range(len(self.num_list)):
            self.num_list[i] = self.getFizzBuzz(self.num_list[i])

    def makeOutputString(self):
        ret_string = ' '.join(self.num_list)+' fizz: {} buzz: {} fizzbuzz: {} lucky: {} integer: {}'.format(
                self.fizz_count,
                self.buzz_count,
                self.fizzbuzz_count,
                self.lucky_count,
                self.int_count,
            )

        return ret_string

    def fizzMyBuzz(self, start=None, end=None):
        if start == None:
            raise ValueError("no start value given")
        elif end == None:
            raise ValueError("no end value given")
        self.setFizzBuzzStart(start)
        self.setFizzBuzzEnd(end)
        self.setList()
        self.makeFizzBuzz()
        return self.makeOutputString()
