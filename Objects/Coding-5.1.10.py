#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

#setter funcions
    def set_meat(self, value):
        if value in ["chicken", "steak", "pork", "tofu", False]:
            self.meat = value
        else:
            self.meat = False

    def set_to_go(self, value):
        if value in [True, False]:
            self.to_go = value
        else:
            self.to_go = False

    def set_rice(self, value):
        if value in ["white", "brown", False]:
            self.rice = value
        else:
            self.rice = False

    def set_beans(self, value):
        if value in ["black", "pinto", False]:
            self.beans = value
        else:
            self.beans = False

    def set_extra_meat(self, value):
        if value in [True, False]:
            self.extra_meat = value
        else:
            self.extra_meat = False

    def set_guacamole(self, value):
        if value in [True, False]:
            self.guacamole = value
        else:
            self.guacamole = False

    def set_cheese(self, value):
        if value in [True, False]:
            self.cheese = value
        else:
            self.cheese = False

    def set_pico(self, value):
        if value in [True, False]:
            self.pico = value
        else:
            self.pico = False

    def set_corn(self, value):
        if value in [True, False]:
            self.corn = value
        else:
            self.corn = False

    def get_cost(self):
        cost = 5
        if self.meat in ["chicken", "pork", "tofu"]:
            cost = cost + 1
        if self.meat == "steak":
            cost = cost + 1.5

        if self.extra_meat == True and self.meat != False:
            cost = cost + 1

        if self.guacamole == True:
            cost = cost + 0.75

        return round(cost, 2)



#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
