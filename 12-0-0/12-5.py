# -*- encoding: utf-8 -*-
'''
@File    :   12-5.py
@Time    :   26/11/2022, 11:34:16
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Varastokirjanpito
'''

COMMENT_CHAR = '#'
LOW_STOCK_LIMIT = 30
COMMANDS = {"help":     "- Without args, command prints list of all commands.\n"\
                        "- With arg <command> prints a description of the <command>",
                        
            "print":    "- Without arguments, prints all known products in the\n"\
                        "  ascending order of the product codes.\n"\
                        "- With one argument consisting of a valid product key,\n"\
                        "  prints info about that product.",
                        
            "change":   "- With one argument (amount of change, positive or negative)\n"\
                        "  modifies the amount of a product in stock.",
                        
            "delete":   "- With arg <key>, deletes a product from warehouse if it\n"\
                        "  exists and stock amount is <= 0.",
            
            "low":      "- Prints a list of items which are under LOW_STOCK_LIMIT,\n"\
                        "  ordered by item key, to ascending order.",
            
            "combine":  "- With args <category1> <category2>, combines two items with\n"\
                        "  differnt keys, same category and same price.",
            
            "sale":     "- With args <category> <sale_percentage>, changes the sale\n"\
                        "  percentage of items belonging to a category.",
            
            "list":     "- Lists all categories, if no params are provided.\n"\
                        "- Lists all products in a category, if a <category> is provided."}

class Product:
    """
    This class represents a product, meaning an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        """Constructor

        :param _type_ code: _description_
        :param _type_ name: _description_
        :param _type_ category: _description_
        :param _type_ price: _description_
        :param _type_ stock: _description_
        """
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock 
        self.__sale_per = 0.0 # no sale % by default          

    def __str__(self):
        """
        For automated tests.
        """
        # the actual price of the item with sale percentage
        # for some reason this functionality was originally missing?     
        price_with_sale_per = (100.0 - self.__sale_per)/100.0 * self.__price

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {price_with_sale_per:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        For automated tests.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price
               
    def category(self) -> str:
        """
        Gets the item's category.

        :return: item's category
        """
        return self.__category

    def modify_stock_size(self, amount) -> None:
        """
        Modifies stock size.

        :param amount: int, amount, + or -
        """

        self.__stock += amount
    
    def name(self) -> str:
        """
        Gets the name of the item.

        :return: returns the name of the item.
        """
        return self.__name
    
    def price(self) -> float:
        """
        Gets the item's price.

        :return: Item's price.
        """
        return self.__price
        
    def set_sale_per(self, per:float) -> None:
        """
        Sets the item's sale percentage.

        :param float per: Sale percentage. Hopefully between 0.0-100.0.
        """
        self.__sale_per = per        
        
    def stock_size(self) -> int:
        """
        Gets the amount of item in stock.

        :return: amount of stock
        """
        return self.__stock
    
    def stock_value(self) -> float:
        """
        Gets the value of items in stock.

        :return: value of stock in €
        """
        
        # stock has value if it exists
        if self.__stock > 0:            
            return self.__stock * self.__price
        
        # if no stock, stock doesn't have any value
        return 0.0

class Warehouse:
    """
    This params list style was taught in ohj2 so I assume it is OK to do it.
    """
    def __init__(self, data):
        self.__data:dict = data
                
    def help(self, params:list) -> None:
        """
        Prints list of all commands, or if specific command is give in params,
        prints info about the cmd.
        
        Complains to user about non-existing commands or bad input.

        :param params: which command to get more info about
        """
        if (len(params) == 0):
            print("Type help <command> to get a description of "\
                  "a specific command.\nList of commands:")
            for val in sorted(COMMANDS):
                print(val)
            return
        elif (len(params) == 1): 
            if (params[0] in COMMANDS):
                print(COMMANDS[params[0]])            
            
            return
        
        print(f"Error: bad command: {' '.join(params)}.")                
            
    def print(self, params:list) -> None:
        """
        Prints all items if no params are provided.
        If one valid param is provided, prints one item.
        Otherwise complains to user about bad input.

        :params list params: list of user input
        :return None
        """
                                 
        # print all dict values sorted by key
        if (len(params) == 0):
            for key, val in sorted(self.__data.items()):
                print(val)   
            return     
                
        # print one value        
        elif (len(params) == 1):       
            # does params contain a valid key?
            try:
                key = int(params[0])                      
                if (key in self.__data):
                    print(self.__data[key])   
                    return 
            # according to spec program does not complain specifically about bad number format                               
            except ValueError: 
                pass
                
        print(f"Error: product '{' '.join(params)}' can not be "
                +"printed as it does not exist.")     
    
    def change(self, params:list) -> None:
        """
        Changes amount of product in stock.
        Complains to user about product not existing, or about
        bad command.

        :param params: <key> <change>
        """
        if(len(params) == 2):
            try:
                key:int = int(params[0])
                change:int = int(params[1])
                
                # change amount if key exists and change is a valid int
                if (key in self.__data):
                    self.__data[key].modify_stock_size(change) 
                else:
                    print(f"Error: stock for '{key}' can not be changed as it does not exist.")
                return
            # according to spec program does not complain specifically about bad number format
            except ValueError:
                pass 
        
        print(f"Error: bad parameters '{' '.join(params)}' for change command.")     

    def delete(self, params:list) -> None:
        """
        Deletes <key> product from warehouse if it exists and 
        stock amount is <= 0.
        
        Otherwise complains to user about existing stock or bad command.

        :param params: <key>
        """
        if(len(params) == 1):
            try:
                key = int(params[0])                      
                if (key in self.__data):
                    if (self.__data[key].stock_size() <= 0):
                        self.__data.pop(key) 
                    else:
                        print(f"Error: product '{key}' can not be deleted as stock remains.")
                    return
            # according to spec program does not complain specifically about bad number format
            except ValueError:
                pass
            
        print(f"Error: product '{' '.join(params)}' can not be deleted as it does not exist.")     
    
    def low(self, params:list) -> None:
        """
        Prints a list of items which are under LOW_STOCK_LIMIT,
        ordered by key ASC
        
        If user gave params, complains about a bad command.

        :param params: hopefully none!
        """
        if (len(params) == 0):
            for key, val in sorted(self.__data.items()):
                if (self.__data[key].stock_size() < LOW_STOCK_LIMIT):
                    print(self.__data[key])     
            return 
        
        print(f"Error: bad command line 'low {' '.join(params)}'.") 
    
    def combine(self, params:list) -> None:
        """
        Combines two items, if the items exist, have a different key,
        belong to a same category and have the same price.
        
        Otherwise complains about bad params in diffent ways.

        :param params: <category 1> <category 2>
        """
        if(len(params) == 2):            
            try:      
                can_combine = True          
                key1 = int(params[0])
                key2 = int(params[1])
                
                # are the keys same?
                if (key1 == key2):
                    can_combine = False
                    
                # are both keys in the data?
                elif not ((key1 in self.__data) and (key2 in self.__data)):
                    can_combine = False
                    
                # do both items belong to same category?
                elif (self.__data[key1].category() != self.__data[key2].category()):
                    print("Error: combining items of different categories "\
                         f"'{self.__data[key1].category()}' and '{self.__data[key2].category()}'.")
                    return  
                
                # do both items have the same price?
                elif (self.__data[key1].price() != self.__data[key2].price()): 
                    print("Error: combining items with different prices "\
                         f"'{self.__data[key1].price()}' and '{self.__data[key2].price()}'.")
                    return           
                
                # if nothing went wrong, we can combine the items    
                if can_combine:
                    self.__data[key1].modify_stock_size(self.data[key2].stock_size())   
                    self.__data.pop(key2) 
                    return 
                                  
            # according to spec program does not complain specifically about bad number format
            except ValueError:
                pass
        
        print(f"Error: bad parameters '{' '.join(params)}' for combine command.")   
    
    def sale(self, params:list) -> None:
        """
        Changes the sale percentage of items belonging to a <category>.

        :param params: <category: str> <sale_percentage: float>
        """
        if(len(params) == 2):            
            try:
                count:int = 0
                cat = params[0]
                sale_per = float(params[1])                 
                
                # change sale percentage for items with <cat> category                     
                for key, val in self.__data.items():
                    if self.__data[key].category() == cat:
                        self.__data[key].set_sale_per(sale_per)
                        count += 1
                        
                print(f"Sale price set for {count} items.")
                return                  
            # according to spec program does not complain specifically about bad number format
            except ValueError:
                pass
            except OverflowError:
                print(f"Error: overflow error with '{sale_per}'.")                
            
                
        print(f"Error: bad parameters '{' '.join(params)}' for sale command.")
        
    def list(self, params: list) -> None:
        """
        Lists all categories, if no params are provided.
        Lists all products in a category, if a <category> is provided.

        :param list params: no params, or a <category>
        """
        
        # prints a list of item categories.   
        if (len(params) == 0):
            cats:set = set()
            for key, val in self.__data.items():
                cats.add(val.category())
            
            print("List of current product categories:")
            print(', '.join(sorted(cats)))
            return
        
        # prints items in a category
        elif (len(params) == 1):
            cat:str = params[0]
            products:set = set()
            for key, val in self.__data.items():
                if (cat == val.category()):
                    products.add(val.name())
            
            # nothing in the category?
            if (len(products) == 0):
                print(f"No products in category '{cat}'.")
                return
            
            # list the products found
            print(f"List of products in category '{cat}':")
            print(', '.join(sorted(products)))
            return            
            
        print(f"Error: bad parameters '{' '.join(params)}' for list command.")     
class Data_parser:
    """
    Parses automatically data to key <product_id>, value <Product object> format
    from provided file
    """
    def __init__(self, filename):
        self.__data:dict = {}
        self.__row_nr: int = 1
        self.__filename: str = filename
        
        # get data
        self.__read_data_from_file()
        
    def __add_product_to_data(self, product:list):
        """
        Go through given product items and check they have a proper key and value.
        If they are good, create a Product object and add it to product database.
        
        param : list of product values.
        return: none
        """
        product_info:dict = {}
        
        for item in product:
            try:
                key, val = item.split(maxsplit=1) 
                if key in ("CODE", "STOCK"):
                    val = int(val)
                elif key == "PRICE":
                    val = float(val)
                elif key in ("NAME", "CATEGORY"):
                    pass
                else:
                    print(f"Error: an unknown data identifier '{key}'.")
                    return None  
            
                product_info[key] = val
            except ValueError:
                print(f"Error: bad data in row {self.__row_nr}: {item}")
                return None
            except OverflowError:
                print(f"Error: bad data in row {self.__row_nr}: {item}")     
        
        # product must have 5 properties
        if len(product_info) != 5:
            print(f"Error: a product block has invalid data lines above row {self.__row_nr}.")        
        
        # create a Product object from the properties and values
        product_object = Product(product_info["CODE"],
                                 product_info["NAME"],                                 
                                 product_info["CATEGORY"],
                                 product_info["PRICE"],
                                 product_info["STOCK"])
        
        # try to add the product object to data
        if product_info["CODE"] in self.__data:
            # if two product objects are the same, combine the stock
            if product_object == self.__data[product_info["CODE"]]:
                self.__data[product_info["CODE"]].modify_stock_size(product_info["STOCK"])
            # otherwise complain about bad data
            else:
                print(f"Error: product code '{product_info['CODE']}' conflicting data.")
                return None
            
        # finally add the object to data
        else:
            self.__data[product_info["CODE"]] = product_object   
    
    def data(self) -> dict:
        """
        Returns the automatically created and collected dict.
        Data was read from provided filename and parsed.

        :return: dict, data
        """
        return self.__data   

    def __parse_data(self, rows:list) -> None:
        """
        Goes through all the read rows.
        Checks for empty rows, commented rows, comments after product info.
        
        param : TODO        
        """
        data:dict = {}
        product: list = []
        product_found:bool = False
        
        for row in rows:
            # skip empty rows
            if (len(row) == 0):
                continue
            # skip commented rows
            elif row[0].strip() == COMMENT_CHAR:
                continue        
            # if we find a product, remember it and continue
            elif row == "BEGIN PRODUCT":
                product_found = True
                continue        

            # after product info ends, check if we found enough product rows
            if row == "END PRODUCT":
                if product_found == True:
                    # if product doesn't have required amount of rows, abort
                    if (len(product) != 5):                    
                        print(f"Error: invalid product info before row {self.__row_nr}") 
                        return None
                    # otherwise check and then add product data
                    self.__add_product_to_data(product)
                    product_found = False
                    product = []
                    
            # In rows which probably contain product info, collect it.
            elif product_found:
                # check if the line has a comment after product data
                comment_start: int = row.find(COMMENT_CHAR)
                if comment_start != -1:
                    row = row[:comment_start].strip()
                
                # finally add a row to product info
                product.append(row)
                    
            # increment current row number
            self.__row_nr +=1
            
    def __read_data_from_file(self) -> list:
        """
        param : str, filename to read
        return: dict with data parsed by parse_data()
        """
        data:dict = {}
        
        try:
            with open (self.__filename, "r") as read_file:
                rows:list = read_file.read().splitlines()
            read_file.close()
            data:dict = self.__parse_data(rows)
            return data
        
        except OSError:
            print("Bad file name!")
        
        return data          
        
def menu(warehouse:object) -> None:
    """
    Displays menu and executes user cmds.

    :param  warehouse: Warehouse object populated with Products
    :return None
    """
    
    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return None
        
        params = command_line.split(' ')      
        cmd = params[0].lower()
        params.pop(0)
        
        # try to run user cmd
        # this style was taught in ohj2 couse project 3: book
        if cmd in COMMANDS:        
            try:
                getattr(warehouse, cmd)(params)
            except AttributeError: 
                print(f"Error: command '{cmd}' does not exist.")
        # otherwise complain about bad cmd
        else:              
            print(f"Error: bad command line '{command_line}'.")      

def main():
    filename = input("Enter database name: ")
    # filename = "tiny_products.txt"

    # read data from file
    parser = Data_parser(filename)  
    # nothing read?
    if parser.data() is None:
        return
    
    warehouse = Warehouse(parser.data())

    # main menu
    menu(warehouse)
    
    return 0

if __name__ == "__main__":
    main()