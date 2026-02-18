class Father:
    def skill(self):
        return "Driving"


class Mother:
    def talent(self):
        return "Cooking"


class Child(Father, Mother):
    pass


child = Child()
print(child.skill())
print(child.talent())
