

class Service:
    def __init__(self, service_id, service_name, price):
        self.service_id = service_id
        self.service_name = service_name
        self.price = price

    def get_service_details(self):
        return f"{self.service_name} - N${self.price}"


class Pet:
    def __init__(self, pet_id, name, age):
        self.pet_id = pet_id
        self.name = name
        self.age = age
        self.services = []

    def assign_service(self, service):
        self.services.append(service)

    def display_services(self):
        if not self.services:
            print(f"{self.name} has no services assigned.")
        else:
            print(f"Services for {self.name}:")
            for s in self.services:
                print(f"- {s.get_service_details()}")

    def pet_type(self):
        return "Normal pet"


class Dog(Pet):
    def __init__(self, pet_id, name, age, breed, requires_special_grooming):
        super().__init__(pet_id, name, age)
        self.breed = breed
        self.requires_special_grooming = requires_special_grooming

    def pet_type(self):
        return "Dog"


class Cat(Pet):
    def __init__(self, pet_id, name, age, breed, is_indoor):
        super().__init__(pet_id, name, age)
        self.breed = breed
        self.is_indoor = is_indoor

    def pet_type(self):
        return "Cat"


class Owner:
    def __init__(self, owner_id, name, contact):
        self.owner_id = owner_id
        self.name = name
        self.contact = contact
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"{pet.name} added to {self.name}'s pets.")

    def remove_pet(self, pet_id):
        for pet in self.pets:
            if pet.pet_id == pet_id:
                self.pets.remove(pet)
                print(f"{pet.name} removed from {self.name}'s pets.")
                return
        print("Pet not found.")

    def get_pets(self):
        return self.pets


class Company:
    def __init__(self, name, address):
        self.company_name = name
        self.address = address
        self.owners = []
        self.services = []

    def add_owner(self, owner):
        self.owners.append(owner)

    def add_service(self, service):
        self.services.append(service)

    def calculate_total_service_fees(self):
        total = 0
        for owner in self.owners:
            for pet in owner.get_pets():
                for service in pet.services:
                    total += service.price
        return total



if __name__ == "__main__":
    
    my_company = Company("LadyHouse Care", "134 K Street")

    
    grooming = Service("1R01", "Grooming", 45.0)
    boarding = Service("1R02", "Boarding", 

    my_company.add_service(grooming)
    my_company.add_service(boarding)

    
    own1 = Owner("888T", "Erik", "erikkishatona@email.com")
    dog1 = Dog("W01", "Spotty", 5, "Golden Retriever", True)
    cat1 = Cat("W02", "Kitty", 4, "Siamese", True)

    
    own1.add_pet(dog1)
    own1.add_pet(cat1)

    
    my_company.add_owner(own1)

    
    dog1.assign_service(grooming)
    cat1.assign_service(boarding)

    
    dog1.display_services()
    cat1.display_services()

    # Polymorphism demonstration
    pets = [dog1, cat1]
    for pet in pets:
        print(f"{pet.name} is a {pet.pet_type()}")

    # Calculate total service fees
    print(f"Total service fees: N${my_company.calculate_total_service_fees()}")


