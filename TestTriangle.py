# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3,5,4 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 10), 'NotATriangle', '1,2,10 is not a Triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10, 1, 2), 'NotATriangle', '10,1,2 is not a Triangle')
    def estNotATriangleB(self):
        self.assertEqual(classifyTriangle(2, 10, 1), 'NotATriangle', '2,10,1 is not a Triangle')

    def testInvalidIputA(self):
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput', '201,201,201 is invalid input')

    def testInvalidIputB(self):
        self.assertEqual(classifyTriangle(0, 1, 2), 'InvalidInput', '0,1,2 is invalid input')

    def testInvalidIputC(self):
        self.assertEqual(classifyTriangle(1, 5, 300), 'InvalidInput', '1,5,300 is invalid input')

    def testInvalidIputD(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is invalid input')

    def testInvalidIputE(self):
        self.assertEqual(classifyTriangle(0.1, 0.1, 0.1), 'InvalidInput', '0.1,0.1,0.1 is invalid input')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 is a Isoceles Triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5,6,7 is a Scalene Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
