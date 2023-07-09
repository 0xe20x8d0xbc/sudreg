import requests


class SudskiRegistarAPI:
    def __init__(self, subscription_key):
        self.base_url = "https://sudreg-api.pravosudje.hr/javni"
        self.headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    def get_bris_pravni_oblik(self, expand_relations=None, timestamp_id=None):
        endpoint = "/bris_pravni_oblik"
        params = {}
        if expand_relations is not None:
            params["expand_relations"] = expand_relations
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_bris_registar(self, expand_relations=None, timestamp_id=None):
        endpoint = "/bris_registar"
        params = {}
        if expand_relations is not None:
            params["expand_relations"] = expand_relations
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_djelatnost_podruznice(self, offset, limit=None, timestamp_id=None):
        endpoint = "/djelatnost_podruznice"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_drzava(self, timestamp_id=None):
        endpoint = "/drzava"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_email_adrese(self, offset, limit=None, timestamp_id=None):
        endpoint = "/email_adrese"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_evidencijske_djelatnosti(self, offset, limit=None, timestamp_id=None):
        endpoint = "/evidencijske_djelatnosti"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_gfi(self, offset, limit=None, timestamp_id=None):
        endpoint = "/gfi"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_ino_registar(self, offset, limit=None, timestamp_id=None):
        endpoint = "/ino_registar"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_jezik(self, timestamp_id=None):
        endpoint = "/jezik"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_nacionalna_klasa_djelatnosti(self, timestamp_id=None):
        endpoint = "/nacionalna_klasa_djelatnosti"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_naziv_podruznice(self, offset, limit=None, timestamp_id=None):
        endpoint = "/naziv_podruznice/get"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_objava_priopcenja(self, offset, limit=None, timestamp_id=None):
        endpoint = "/objava_priopcenja"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_postupak(self, offset, limit=None, timestamp_id=None):
        endpoint = "/postupak"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_pravni_oblik(self, offset, limit=None, timestamp_id=None):
        endpoint = "/pravni_oblik"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_predmet_poslovanja(self, offset, limit=None, timestamp_id=None):
        endpoint = "/predmet_poslovanja"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_pretezite_djelatnosti(self, offset, limit=None, timestamp_id=None):
        endpoint = "/pretezite_djelatnosti"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_prijevod_skracena_tvrtka(self, offset, limit=None, timestamp_id=None):
        endpoint = "/prijevod_skracena_tvrtka"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_prijevod_tvrtka(self, offset, limit=None, timestamp_id=None):
        endpoint = "/prijevod_tvrtka"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_sjediste(self, offset, limit=None, timestamp_id=None):
        endpoint = "/sjediste"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_sjediste_podruznice(self, offset, limit=None, timestamp_id=None):
        endpoint = "/sjediste_podruznice/get"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_skracena_tvrtka(self, offset, limit=None, timestamp_id=None):
        endpoint = "/skracena_tvrtka"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_skraceni_naziv_podruznice(self, offset, limit=None, timestamp_id=None):
        endpoint = "/skraceni_naziv_podruznice"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_status(self, timestamp_id=None):
        endpoint = "/status"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_subjekt_detalji(self, tip_identifikatora, identifikator, expand_relations=None, timestamp_id=None):
        endpoint = "/subjekt_detalji"
        params = {"tipIdentifikatora": tip_identifikatora, "identifikator": identifikator}
        if expand_relations is not None:
            params["expand_relations"] = expand_relations
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_subjekt(self, offset, limit=None, tvrtka_naziv=None, timestamp_id=None, only_active=None):
        endpoint = "/subjekt"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if tvrtka_naziv is not None:
            params["tvrtka_naziv"] = tvrtka_naziv
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        if only_active is not None:
            params["only_active"] = only_active
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_sud(self, timestamp_id=None):
        endpoint = "/sud"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_temeljni_kapital(self, offset, limit=None, timestamp_id=None):
        endpoint = "/temeljni_kapital"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_timestamp(self, timestamp_id=None):
        endpoint = "/timestamp"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_tvrtka(self, offset, limit=None, timestamp_id=None):
        endpoint = "/tvrtka"
        params = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_valuta(self, timestamp_id=None):
        endpoint = "/valuta"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_gfi_dokumenta(self, timestamp_id=None):
        endpoint = "/vrsta_gfi_dokumenta"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_postupka(self, timestamp_id=None):
        endpoint = "/vrsta_postupka"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_pravnog_oblika(self, timestamp_id=None):
        endpoint = "/vrsta_pravnog_oblika"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
