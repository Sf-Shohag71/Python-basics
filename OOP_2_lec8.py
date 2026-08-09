class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private attribute

acc1 = Account(12345, 'mypassword')

print(acc1.acc_no)
print(acc1.__acc_pass)