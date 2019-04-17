# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        
        myFib = Fib()
        myFib.previous = self.value
        if (self.value == 0):
            myFib.value, myFib.previous = 1,0
        else:
            myFib.value, myFib.previous = self.value+self.previous, self.value
        return myFib

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    stock = 0
    deposited = 0
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def vend(self):

        if (self.stock == 0 and self.deposited > 0):
            print('Machine is out of stock. Here is your ${0}.'.format(self.deposited))
            self.deposited = 0
        elif (self.stock == 0):
            print('Machine is out of stock.')
        elif (self.price == self.deposited):
            print('Here is your {0}.'.format(self.name))
            self.deposited = 0
            self.stock -= 1
        elif (self.deposited > self.price):
            print('Here is your {0} and ${1} change.'.format(self.name, self.deposited - self.price))
            self.deposited = 0
            self.stock -= 1
        else:
            print('You must deposit ${0} more.'.format(self.price - self.deposited))
            
    def deposit(self,increase):
        self.deposited += increase
        if (self.stock == 0):
            print('Machine is out of stock. Here is your ${0}.'.format(self.deposited))
            self.deposited = 0
        else:
            print('Current balance: ${0}.'.format(self.deposited))

    def restock(self,increase):
        self.stock += increase
        print('Current soda stock: {0}'.format(self.stock))
