class Person(object):
    group = []
    def __init__(self, name, money_spent):
        self.name = name
        self.money_spent = money_spent
        self.money_received = 0
        self.__class__.group.append(self)

    def gives_gift_to(self, *friends):
        gift_amount = self.money_spent/len(friends)
        for friend in friends:
            friend.money_received += gift_amount

    def networth(self):
        return int(self.money_received - self.money_spent)


dave = Person('dave', 200)
laura = Person('laura', 0)
owen = Person('owen', 500)
vick = Person('vick', 0)
amr = Person('amr', 150)

dave.gives_gift_to(laura, owen, vick)
owen.gives_gift_to(dave)
amr.gives_gift_to(vick, owen)


for friend in Person.group:
    print(friend.name, friend.networth())