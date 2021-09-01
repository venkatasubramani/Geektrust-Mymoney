import unittest


class Test_money(unittest.TestCase):

    def test_input1(self):
        '''
        ALLOCATE 6000 3000 1000
        SIP 2000 1000 500
        CHANGE 4.00% 10.00% 2.00% JANUARY
        CHANGE -10.00% 40.00% 0.00% FEBRUARY
        CHANGE 12.50% 12.50% 12.50% MARCH
        CHANGE 8.00% -3.00% 7.00% APRIL
        CHANGE 13.00% 21.00% 10.50% MAY
        CHANGE 10.00% 8.00% -5.00% JUNE
        BALANCE MARCH
        REBALANCE
        '''
        self.assertAlmostEqual('10593 7897 2272', '10593 7897 2272')
        self.assertAlmostEqual('23619 11809 3936', '23619 11809 3936')


    def test_input2(self):
        '''
        ALLOCATE 8000 6000 3500
        SIP 3000 2000 1000
        CHANGE 11.00% 9.00% 4.00% JANUARY
        CHANGE -6.00% 21.00% -3.00% FEBRUARY
        CHANGE 12.50% 18.00% 12.50% MARCH
        CHANGE 23.00% -3.00% 7.00% APRIL
        BALANCE MARCH
        BALANCE APRIL
        REBALANCE
        '''
        self.assertAlmostEqual('15937 14552 6187', '15937 14552 6187')
        self.assertAlmostEqual('23292 16055 7690', '23292 16055 7690')
        self.assertAlmostEqual('CANNOT_REBALANCE', 'CANNOT_REBALANCE')