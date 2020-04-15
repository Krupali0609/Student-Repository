""" Thisis unittest . py file which is testing the functions of the file which 
 have been declaredd"""
import os
import unittest
from typing import Iterator, Tuple, Dict, List
from HW09_Krupali_Italiya import University, Student, Instructor, file_reader

class TestRepository(unittest.TestCase):
    """Path setup"""
    def setUp(self):
            self.test_path = "C:/Users/0609k/OneDrive/Desktop/Python"
            self.repo = University(self.test_path,False)
        
    def test_Student(self):
        """Testcase for student"""
        result1 = {'10103': ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    '10175': ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183', 'Chapman, O', ['SSW 689']],
                    '11399': ['11399', 'Cordova, I', ['SSW 540']],
                    '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                    '11658': ['11658', 'Kelly, P', ['SSW 540']],
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    '11788': ['11788', 'Fuller, E', ['SSW 540']]}
        
        result2 = {cwid: students.ptable_row() for cwid, students in self.repo._students.items()}
        self.assertEqual.__self__.maxDiff = None #googled this:  was getting an error
        self.assertEqual(result1,result2)

    def test_Instructor(self):
        """Testcase for instructor"""
        result1 = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                    ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        result2 = {tuple(detail) for instructor in self.repo._instructors.values() for detail in instructor.ptable_row()}
        self.assertEqual(result1, result2)

#execution starts from here
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
