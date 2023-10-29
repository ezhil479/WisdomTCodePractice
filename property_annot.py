class Phone:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.complete_spec = f"{self.name}"

        @property
        def complete_spec(self):
            return f"{self.name} and rate {self.price}"
        
p1 = Phone("Nokia", 3000)
print(p1.name)
print(p1.price)
print(p1.complete_spec)
p1.price = 5000
print(p1.price)
print(p1.complete_spec)


