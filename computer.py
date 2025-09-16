"""
   Filename: computer.py
Description: It stores computer's attributes like description, processor  type, hard drive capacity, memory, operating system, year made and price.
     Author: Selina Fang
       Date: Sep 16 2025
"""
class Computer:
    """
    It represents a computer in the resale shop. It can store attributes like description, processor  type, hard drive capacity, memory, operating system, year made and price and also defines methods of updating the price and the OS of the computers.
    """
    # What attributes will it need?
    # The attributes it needs are description, processor type, hard drive capacity, memory, operating system, year made and price.

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        """
        The constructor here can is set up by creating the computer's information like OS, year made and  price.
        """
        self.description= description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory= memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price

    # What methods will you need?
    # The method we need is to update the price and the operating system of the computer and show the basic information of the computer.
    def update_price(self, new_price:int):
        """
        update the price of the computer.
        """
        self.price=new_price

    def update_os(self, new_os:str):
        """
        update the operating system of the computer.
        """
        self.operating_system=new_os

    def show(self):
        """
        return the basic information of the computer.
        """
        return (f'description: {self.description}, processor_type: {self.processor_type}, hard_drive_capacity: {self.hard_drive_capacity}, memory: {self.memory}, operating_system: {self.operating_system}, year_made: {self.year_made}, price: {self.price}')