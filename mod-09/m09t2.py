from classes.auto import Auto

auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(auto1.nopeus)
auto1.kiihdyta(-200)
print(auto1.nopeus)