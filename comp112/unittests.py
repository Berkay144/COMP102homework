'''
Created on 11 Nis 2024

@author: berkay
'''
import unittest 

from AgeCheck import agecheck #Main code call

class TestAgeCheck(unittest.TestCase): #Called from other file
    
    
    # Test 1 Age <= 25 and Experience <= 2
    def test1(self):
        #young driver with less experience
        self.assertEqual(agecheck(25, 2), 4)
        
    # Test 2: Age <= 25 and Experience > 2
    def test2(self):
        #young driver with more experience
        self.assertEqual(agecheck(25, 3), 2)
        
    # Test 3: 25 < Age <= 70 and Experience <= 5
    def test3(self):
        #older driver with less experience
        self.assertEqual(agecheck(30, 5), 3)
        
    # Test 4: 25 < Age <= 70 and Experience > 5
    def test4(self):
        # older driver with more experience
        self.assertEqual(agecheck(30, 6), 1.5)
        
    # Test 5: Age > 70 and Age <= 80
    def test5(self):
        # elderly driver
        self.assertEqual(agecheck(75, 0), 1.5)
        
    # Test 6: Age > 80
    def test6(self):
        # driver over 80 years old
        self.assertEqual(agecheck(85, 0), 2)
        
    # Test 7 these are equalities and edges (ara)
    def test_edges(self):
        # Testing the boundary age and experience values
        self.assertEqual(agecheck(25, 0), 4)
        self.assertEqual(agecheck(70, 5), 3)
        self.assertEqual(agecheck(80, 0), 1.5)
        
if __name__ == '__main__':
    unittest.main()
    
    #There are failed tests (3 to be exact)
