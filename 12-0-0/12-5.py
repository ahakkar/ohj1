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

LOW_STOCK_LIMIT = 30
COMMANDS = {"help":     "- Without args, command prints list of all commands.\n"\
                        "- With arg <command> prints a description of the <command>",
            "print":    "- Without arguments, prints all known products in the\n"\
                        "  ascending order of the product codes.\n"\
                        "- With one argument consisting of a valid product key,\n"\
                        "  prints info about that product.",
            "change":   "- With one argument (amount of change, positive or negative)\n"\
                        "  modifies the amount of a product in stock.",
            "delete":   "explanation",
            "low":      "explanation",
            "combine":  "explanation",
            "sale":     "explanation"}

class Product:
    """
    This class represent a product i.e. an item available for sale.
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

    def __str__(self):
        """
        for automated tests
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
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
        for automated tests
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def modify_stock_size(self, amount):
        """
        modify stock size

        :param amount: int, amount, + or -
        """

        self.__stock += amount
        
    # TODO: Multiple methods need to be written here to allow
    #       all the required commands to be implemented.
    
    def print_commands(self) -> None:
        cmds:str = ""
        for val in COMMANDS:
            cmds.append(f"{val}, ")
        
        print(cmds[0:-2])


def _read_lines_until(fd, last_line):
    """
    read lines until

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    read a file

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None

class Warehouse:
    """
    This params list style was taught in ohj2 so I assume it is OK to do it.
    """
    def __init__(self):
        data:dict = {}
    
    def __str__(self):
        pass
    
    def add_data(self, data_to_add:dict):
        self.data = data_to_add
        
    def help(self, params:list) -> None:
        if (len(params) == 0):
            print("Type help <command> to get a description of "\
                  "a specific command.\nList of commands:")
            for val in sorted(COMMANDS):
                print(val)
            return
        elif (len(params) == 1): 
            if params[0] in COMMANDS:
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
            for key, val in sorted(self.data.items()):
                print(val)   
            return     
                
        # print one value        
        elif (len(params) == 1):       
            # does params contain a valid key?
            try:
                key = int(params[0])                      
                if key in self.data:
                    print(self.data[key])   
                    return                                
            except ValueError: 
                pass
                
        print(f"Error: product {' '.join(params)} can not be "
                +"printed as it does not exist.")     
    
    def change(self, params:list) -> None:
        pass      

    def delete(self, params:list) -> None:
        pass
    
    def low(self, params:list) -> None:
        pass
    
    def combine(self, params:list) -> None:
        pass
    
    def sale(self, params:list) -> None:
        pass
    
def menu(data:dict) -> None:
    """Handles menu and user cmds_

    :param  data: dict with product objects
    :return None
    """
    
    # custom class containing methods for each cmd
    wh = Warehouse()
    wh.add_data(data)
    
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
                getattr(wh, cmd)(params)
            except AttributeError: 
                continue
        # otherwise complain about bad cmd
        else:              
            print(f"Error: bad command line '{command_line}'.")        
    
    return None


def main():
    # filename = input("Enter database name: ")
    filename = "products.txt"

    warehouse = read_database(filename)
    if warehouse is None:
        return

    # main menu
    menu(warehouse)
    
    return 0

if __name__ == "__main__":
    main()