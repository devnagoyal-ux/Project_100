class Atm(object):

    def __init__(self,atm_card_num,pin_num):

        self.atm_card_num = atm_card_num
        self.pin_num = pin_num

    def cash_with_drawl(self):
        print("Cash Withdrawned")

    def balance_enquiry(self):
        print("Balance Enquired")

user_atm_card_num = input("Enter your atm card number : - ")
user_pin_num = input("Enter your atm pin number : - ")

user = Atm(user_atm_card_num,user_pin_num)
print(user.cash_with_drawl())
print(user.balance_enquiry())



    