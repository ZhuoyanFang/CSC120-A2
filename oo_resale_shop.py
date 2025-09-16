from typing import Dict, Optional
from computer import Computer

class ResaleShop:
    """
    It represents a resale shop, and it has an inventory that records that buying, selling and refurbishing of the computers.
    """
    # What attributes will it need?
    # The attributes it need is the shop itself.

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        """
        The constructor here is set up by creating an inventory with a list of computers.
        """
        self.inventory: list[Computer] = []

    # What methods will you need?
    # The methods we want are buying, selling, updating prices and os of computers, refurbishing a computer and print the inventory.
    def buy(self, computer:Computer):
        """
        Add a computer to the inventory.
        """
        self.inventory.append(computer)
        return self.inventory.index(computer)

    def update_price(self,computer:Computer,new_price:int):
        """
        Update the price of a certain computer in the inventory.
        """
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Computer", computer.description, "not found. Cannot update price.")

    def sell(self, computer:Computer,item_id: int):
        """
        Remove a computer from the inventory and print error if the computer is not found in the inventory.
        """
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Computer", computer.description, "sold!")
        else:
            print("Computer", computer.description, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Print all the data of the computers in the inventory.
        """
        if self.inventory:
            for computer in self.inventory:
                print(f'Item ID: {self.inventory.index(computer)} : ', computer.show())
        else:
            print("No inventory to display.")

    def refurbish(self,computer:Computer, new_os: Optional[str] = None):
        """
        Refurbish a certain computer's price based on the year is was made and update the OS of the computer.
        """
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0 
            elif computer.year_made < 2012:
                computer.price = 250 
            elif computer.year_made < 2018:
                computer.price = 550 
            else:
                computer.price = 1000 

            if new_os is not None:
                computer.update_os(new_os)
        else:
            print("Computer", computer.description, "not found. Please select another item to refurbish.")


def main():
    computer1 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    shop = ResaleShop()
    shop.buy(computer1)
    shop.print_inventory()

    # First, let's make a computer
    computer2=Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
        
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer2.description)
    print("Adding to inventory...")
    shop.buy(computer2)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing", computer2.description, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer2, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling", computer2.description)
    shop.sell(computer2, None)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Print two error messages
    shop.update_price(computer2,10000)
    shop.sell(computer2, None)

# Calls the main() function when this file is run
if __name__ == "__main__": main()