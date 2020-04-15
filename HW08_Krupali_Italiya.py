"""This .py file is all about implementing the Date arithmetic, file reader and file analyzer. """

"""This is importing some of the in-built functions"""
from datetime import datetime, timedelta
from typing import Iterator, Tuple, Dict, List
import os
from prettytable import PrettyTable


def date_arithmetic()-> Tuple[datetime, datetime, int]:
    """ Code segment demonstrating expected return values. """
    date1:str = "Feb 27 2020"
    date2:str = "Feb 27 2019"
    date3:str = "Feb 1 2019"
    date4:str = "Sep 30 2019"
    dt1:datetime = datetime.strptime(date1, "%b %d %Y")
    dt2:datetime = datetime.strptime(date2, "%b %d %Y")
    dt3:datetime = datetime.strptime(date3, "%b %d %Y")
    dt4:datetime = datetime.strptime(date4, "%b %d %Y")


    num_days:int = 3
    three_days_after_02272000: datetime = dt1 +timedelta(days=num_days)
    three_days_after_02272017: datetime = dt2 + timedelta(days=num_days)
    days_passed_01012017_10312017: int = (dt4 - dt3).days


    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017

def file_reader(path: str, fields: int, sep: str = ",", header: bool = False) -> Iterator[Tuple[str]]:
    """ The function is about separating all the items about the file """
    try:
        fopen= open(path, "r")
        if not (file := fopen):
            raise FileNotFoundError
        with file:  
            for l_num, line in enumerate(file, 1):
                row_line: List[str] = line.rstrip("\n").split(sep)
                row_line_count: int = len(row_line)
                if row_line_count != fields:
                   raise ValueError(f"{path} has {row_line_count} fields on line {l_num} but expected {fields}")

                if not header or l_num != 1:
                    yield tuple(row_line)
    except FileNotFoundError  as e:
        print(e)


class FileAnalyzer:
    """Function for counting various attributes in file  """
    def __init__(self, directory: str):
        """Constructor is about directory found or not and intializing directory, file summary and analyzing files """
        try:
            if not os.path.exists(directory):
                raise FileNotFoundError(f"The directory:{directory} not found")
        except FileNotFoundError:
            print(f"The directory:{directory} not found")

        self.directory: str = directory 
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files() 
        self.pretty_print()

    def analyze_files(self):
        """  if files not found in directory and counting the classes, functions and lines and char in the .py files"""
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                try:
                    if not (fp := open(os.path.join(self.directory, file), "r")):
                        raise FileNotFoundError(f"File {fp} is not found or can not be opened")
                except FileNotFoundError:
                        print(f"File {fp} not found")
                with fp:  
                    class_cnt: int = 0
                    function_cnt: int = 0
                    line_cnt: int = 0
                    char_cnt: int = 0

                    for line in fp:
                        if line.strip().startswith("class "):
                            class_cnt += 1
                        elif line.strip().startswith("def "):
                            function_cnt += 1

                        line_cnt += 1
                        char_cnt += len(line)

                    self.files_summary[str(os.path.join(self.directory, file))] = {
                        "class": class_cnt,
                        "function": function_cnt,
                        "line": line_cnt,
                        "char": char_cnt
                    }


    def pretty_print(self):
        """ This function is about pretty table printing file name, class, function, lines and characters """
        table: PrettyTable = PrettyTable()
        table.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]
        for key, value in self.files_summary.items():  
            table.add_row([key] + list(value.values()))  

        return table

def main()-> None:
    string:str = "DATE ARITHMETIC"
    """the below print is to skip a line foR better presentation"""
    print("\n")
    """"Just to repesent centered the string in output"""
    centered_string =string.center(100,'-') 
    print(centered_string )
    print(date_arithmetic())

    
    string:str = "FILE READER"
    """the below print is to skip a line foR better presentation"""
    print("\n")
    """"Just to repesent centered the string in output"""
    centered_string =string.center(100,'-') 
    print(centered_string )
    p1="C:/Users/0609k/OneDrive/Desktop/Python/student_majors.txt"
    for lines in file_reader(p1,1,",",True):
        print(lines)

    
    string:str = "FILE ANALYZER"
    """the below print is to skip a line foR better presentation"""
    print("\n")
    """"Just to repesent centered the string in output"""
    centered_string =string.center(100,'-') 
    print(centered_string )
    p2="C:/Users/0609k/OneDrive/Desktop/Python"
    obj=FileAnalyzer(p2)
    print(obj.pretty_print())
    

#excution starts from here
if __name__ == '__main__':        
    main()

    
