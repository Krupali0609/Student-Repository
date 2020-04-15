""" Thisis unittest . py file which is testing the functions of the file which 
 have been declaredd"""
import os
import unittest
from typing import Iterator, Tuple, Dict, List
from HW10_Krupali_Italiya import University, Student, Instructor, file_reader,Major

class TestRepository(unittest.TestCase):
    """Path setup"""
    def setUp(self):
            self.test_path = "C:/Users/0609k/OneDrive/Desktop/Python/Txt_file10"
            self.repo = University(self.test_path,False)
        
    def test_majors(self):
        """ Testing majors table"""
        result1 = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                    ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        result2 = [majors.ptable_row() for majors in self.repo._majors.values()]
        self.assertEqual(result1,result2)

    def test_Student_attributes(self):
        """ Testing student table """
        result1 = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                  ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
                  ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88], 
                  ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58], 
                  ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
                  ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0], 
                  ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                  ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0], 
                  ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
                  ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]
       
        result2 = [student.ptable_row() for cwid, student in self.repo._students.items()]
    
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
