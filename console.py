import pdb

from models.vet import Vet

import repositories.vet_repository as vet_repo

vet_1 = Vet("Sandra", "Jones")
vet_repo.save(vet_1)

vet = vet_repo.select(3)

pdb.set_trace()
