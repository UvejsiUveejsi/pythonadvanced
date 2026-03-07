class Vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone = backbone

    def vertebrate_info(self):
        print("Vertebrates have a backbone")



class Aquatic:
    def __init__(self, habitat = "water"):
        self.habitat = habitat

    def aquatic_info(self):
            print("Aquatic ani live in water")


class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat = "water"):
        super().__init__(backbone=backbone)
        self.habitat=habitat
        self.species = species

    def Fish_info(self):
        print(f"the {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print("fish is swimming")


goldfish = Fish("goldfish")
print(goldfish.has_backbone)
print(goldfish.habitat)
print(goldfish.Fish_info())
print(goldfish.swim())
print(goldfish.aquatic_info())
print(goldfish.vertebrate_info())