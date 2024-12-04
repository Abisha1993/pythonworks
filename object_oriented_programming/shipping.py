class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)
class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)
class StandardShipping(Shipping):
        def calculate_shipping_cost(self,weight):
             print(weight*10)
expe_instance=ExpressShipping()
expe_instance.calculate_shipping_cost(10)
std_instance=StandardShipping()
std_instance.calculate_shipping_cost(10)

    