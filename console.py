import pdb

from models.vet import Vet
from models.owner import Owner

import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo

vet_repo.delete_all()
owner_repo.delete_all()

vet_1 = Vet("Sandra", "Jones")
vet_repo.save(vet_1)

owner_1 = Owner("Jim", "Jimson", "07162626243", "jim@email.com")
owner_repo.save(owner_1)
owner_2 = Owner("Jim", "Jamson", "07162626243", "jim@email.com")
owner_repo.save(owner_2)

owners = owner_repo.select_all()
for owner in owners:
    print(owner.__dict__)

owner = owner_repo.select(owner_2.id)


vets = vet_repo.select_all()

for vet in vets:
    print(vet.__dict__)

vet_1.first_name = "Jeremy"
vet_1.last_name = "Bingham"
vet_1.id = 2
vet_repo.update(vet_1)

pdb.set_trace()
