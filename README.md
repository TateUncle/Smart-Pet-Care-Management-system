🐾 Pet Care Management System

Inheritance: Dog and Cat inherit from Pet.
Composition: Owner owns Pet.
Aggregation: PetCareCompany manages Service.

Polymorphism:
pet_type() overridden in subclasses.
add_service() behaves differently with/without cost.
__str__() prints customized messages.

Exception Handling
Type checks for adding pets, owners, services.
Handling missing services when assigning to pets.

File I/O exceptions handled.
File I/O
Save to pet_data.json.
Load from pet_data.json.

Abstract Data Type
Used List for owners, pets, and services.

Main Executable
Demonstrates adding owners, pets, services, assigning services, calculating fees, and saving/loading data.

