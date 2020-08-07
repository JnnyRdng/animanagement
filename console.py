import pdb

from models.vet import Vet
from models.owner import Owner
from models.animal import Animal
from models.record import Record

import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo
import repositories.animal_repository as animal_repo
import repositories.record_repository as record_repo

record_repo.delete_all()
animal_repo.delete_all()
vet_repo.delete_all()
owner_repo.delete_all()

vet_1 = Vet("Sandra", "Jones")
vet_repo.save(vet_1)

owner_1 = Owner("Jam", "Jimson", "07162626243", "jim@email.com")
owner_2 = Owner("Jim", "Jamson", "07162626243", "jim@email.com")
owner_repo.save(owner_1)
owner_repo.save(owner_2)

pet_1 = Animal("Floof", "01-02-1987", "cat", owner_1, vet_1, "05-08-2020")
pet_2 = Animal("Fluff", "03-04-1958", "dog", owner_2, vet_1, "05-08-2020")
animal_repo.save(pet_1)
animal_repo.save(pet_2)

record_1 = Record("06-08-2020", "Cat is ill", pet_1)
record_2 = Record("07-08-2020", "Cat is still ill", pet_1)
record_3 = Record("06-08-2020", "Now dog is sick", pet_2)
record_repo.save(record_1)
record_repo.save(record_2)
record_repo.save(record_3)


pdb.set_trace()
