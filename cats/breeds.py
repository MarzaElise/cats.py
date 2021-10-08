from utils import Breed

class BreedsMixin:

    def get_breeds(self):
        ses = self.session
        ses.headers["x-api-key"] = self.api_key
        s = ses.get(f"{self.BASE}/breeds")
        json = s.json()
        return [Breed(**data) for data in json]
