import pdb

from models.vet import Vet
from models.owner import Owner
from models.animal import Animal

import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo
import repositories.animal_repository as animal_repo

animal_repo.delete_all()
vet_repo.delete_all()
owner_repo.delete_all()

vet_1 = Vet("Sandra", "Jones")
vet_repo.save(vet_1)

owner_1 = Owner("Jam", "Jimson", "07162626243", "jim@email.com")
owner_repo.save(owner_1)
owner_2 = Owner("Jim", "Jamson", "07162626243", "jim@email.com")
owner_repo.save(owner_2)

pet_1 = Animal("Floof", "01-02-1987", "cat", owner_1, vet_1, "05-08-2020")
pet_2 = Animal("Fluff", "03-04-1958", "dog", owner_2, vet_1, "05-08-2020")
animal_repo.save(pet_1)
animal_repo.save(pet_2)

pet_1.name = "Puffball"
pet_1.owner = owner_2
animal_repo.update(pet_1)

animal = animal_repo.select(pet_1.id)

print(animal.__dict__)

pdb.set_trace()
