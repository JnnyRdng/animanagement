import pdb

from models.vet import Vet

import repositories.vet_repository as vet_repo

vet_1 = Vet("Sandra", "Jones")
vet_repo.save(vet_1)

vet = vet_repo.select(3)

vets = vet_repo.select_all()

for vet in vets:
    print(vet.__dict__)

vet_1.first_name = "Jeremy"
vet_1.last_name = "Bingham"
vet_1.id = 2
vet_repo.update(vet_1)

pdb.set_trace()
