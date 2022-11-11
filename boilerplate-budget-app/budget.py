class Category:
    def __init__(self, category: str, ledger=None):
        if ledger is None:
            ledger = []
        self.ledger = ledger
        self.category = category

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        s = 0
        for dict1 in self.ledger:
            s += dict1["amount"]
        return s

    def transfer(self, amount2, another_category):
        if isinstance(another_category, Category):
            if self.check_funds(amount2):
                self.withdraw(amount2, f"Transfer to {another_category.category}")
                another_category.deposit(amount2, f"Transfer from {self.category}")
                return True
            else:
                return False

    def check_funds(self, amount):
        s = 0.0
        for dict1 in self.ledger:
            s += dict1["amount"]

        if s >= amount:
            return True
        else:
            return False

    def __str__(self):
        st = self.category.center(30, "*")
        for dict1 in self.ledger:
            st += '\n{:<23}{:>7.2f}'.format(dict1['description'][:23], dict1["amount"])
        st += f"\nTotal: {self.get_balance()}"
        return st


def create_spend_chart(categories):
    # gia kathe katigoria px food ,clothing etc
    categories_list = []
    withdraw_sum = 0
    for category in categories:
        for i in range(len(category.ledger)):
            if category.ledger[i]["amount"] < 0:
                withdraw_sum += category.ledger[i]["amount"]

    for category in categories:
        withdraw_sum_per_category = 0
        for i in range(len(category.ledger)):
            if category.ledger[i]["amount"] < 0:
                withdraw_sum_per_category += category.ledger[i]["amount"]
        dict_to_add_to_list = {"Category name": category.category, "Percentage":
            round(100 * withdraw_sum_per_category / withdraw_sum)}

        categories_list.append(dict_to_add_to_list)
    # AssertionError: 'Perc[25 chars]n100|\n 90|\n 80|\n 70|\n 60| o \n 50| o \n 40[290 chars]  \n' !=
    # 'Perc[25 chars]n100|          \n 90|          \n 80|         [349 chars] t  '
    st = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        st += '{:>4}'.format(str(i) + "|")
        for category in categories_list:
            if category['Percentage'] >= i:
                st += ' o '
            else:
                st += '   '
        st += ' \n'

    categories_list = []
    max_length = 0
    for i in range(len(categories)):
        categories_list.append(list(categories[i].category))
        if len(categories[i].category) > max_length:
            max_length = len(categories[i].category)
    st += '    ' + '---' * len(categories_list) + '-'
    for i in range(max_length):
        st += '\n     '
        for name in categories_list:
            try:
                st += name[i] + '  '
            except:
                st += "   "
    #st += '\n'

    return st
