import os, sys

# Custom exception class designed to capture error message and details under logs directory
class CustomException(Exception):
    ## Constructor method to initialize the exception with an error message and its details as 
    # we have to capture both error message and error details under our logs directory
    def __init__(self, error_message:Exception, error_details: sys):
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,

                                                                 error_details=error_details)
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details: sys)->str:
        #_ placeholder for the parts of the exception information that are not needed here and exce_tb then stores the traceback object
        #exce_tb variable is used to retrieve information about the current exception being handled through the sys.exc_info() function.
        _, _, exce_tb = error_details.exc_info()

        #It extracts contextual details such as:Line numbers (try_block_line_number and exception_block_line_number) where the error/exception occurred.
        #File name (file_name) where the error was raised.
        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in execution of :
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        """
        return error_message
    
    #The __str__ method returns the error_message attribute of the CustomException class 
    def __str__(self):
        return self.error_message
    #
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.error_message}')"
