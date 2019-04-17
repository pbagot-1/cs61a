This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

    
    

    Case Example
        >>> import hw06
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
