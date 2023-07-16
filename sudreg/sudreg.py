import requests


class SudskiRegistarAPI:
    """
       A Python client for the Sudski Registar API.

       This client provides an interface to interact with the Sudski Registar API, which provides access to various
       legal and business-related data.

       Attributes:
           base_url (str): The base URL for the Sudski Registar API.
           headers (dict): The headers to be used in API requests. It includes the subscription key.
       """

    def __init__(self, subscription_key):
        """
                Initializes the SudskiRegistarAPI with a subscription key.

                Args:
                    subscription_key (str): The subscription key for the Sudski Registar API.
                """
        self.base_url = "https://sudreg-api.pravosudje.hr/javni"
        self.headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    def get_bris_pravni_oblik(self, expand_relations=None, timestamp_id=None):
        """
                Retrieves the BRIS registrar.

                Args:
                    expand_relations (bool, optional): If set to True, expands the relations in the response.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """

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
        """
               Retrieves the activities of a branch.

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
                Retrieves the activities of a branch.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """

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
        """
               Retrieves the country information.

               Args:
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
        endpoint = "/drzava"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_email_adrese(self, offset, limit=None, timestamp_id=None):
        """
                Retrieves email addresses.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the recorded activities.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """

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
        """
               Retrieves the GFI (General Financial Information).

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
                Retrieves the foreign register.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
               Retrieves the language information.

               Args:
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
        endpoint = "/jezik"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_nacionalna_klasa_djelatnosti(self, timestamp_id=None):
        """
               Retrieves the national classification of activities.

               Args:
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
        endpoint = "/nacionalna_klasa_djelatnosti"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was unsuccessful
        return response.json()

    def get_naziv_podruznice(self, offset, limit=None, timestamp_id=None):
        """
                Retrieves the name of the branch.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
               Retrieves the publication of announcements.

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
               Retrieves the procedure information.

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
                Retrieves the legal form information.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

                Raises:
                    requests.HTTPError: If the API response was unsuccessful.
                """

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
        """
                Retrieves the subject matter of business.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
               Retrieves the predominant activities.

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
                Retrieves the translation of the abbreviated company name.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

                Raises:
                    requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the translation of the company name.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

                Raises:
                    requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the seat information.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the seat of a subsidiary.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the abbreviated company name.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the abbreviated name of a subsidiary.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves the status information.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
        endpoint = "/status"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_subjekt_detalji(self, tip_identifikatora, identifikator, expand_relations=None, timestamp_id=None):
        """
                Retrieves detailed information about a subject.

                Args:
                    tip_identifikatora (str): The type of identifier (mbs or oib).
                    identifikator (str): The identifier value.
                    expand_relations (bool, optional): If set to True, expands the relations in the response.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
               Retrieves information about subjects.

               Args:
                   offset (int): The offset for pagination.
                   limit (int, optional): The maximum number of items to retrieve.
                   tvrtka_naziv (str, optional): The company name to filter the results.
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.
                   only_active (bool, optional): If set to True, only active subjects will be returned.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
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
        """
                Retrieves information about courts.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
        endpoint = "/sud"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_temeljni_kapital(self, offset, limit=None, timestamp_id=None):
        """
                Retrieves information about basic capital.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

                Raises:
                    requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves timestamp information.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
        endpoint = "/timestamp"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_tvrtka(self, offset, limit=None, timestamp_id=None):
        """
                Retrieves information about companies.

                Args:
                    offset (int): The offset for pagination.
                    limit (int, optional): The maximum number of items to retrieve.
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
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
        """
                Retrieves currency information.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """

        endpoint = "/valuta"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_gfi_dokumenta(self, timestamp_id=None):
        """
                Retrieves information about types of GFI documents.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
        endpoint = "/vrsta_gfi_dokumenta"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_postupka(self, timestamp_id=None):
        """
                Retrieves information about types of procedures.

                Args:
                    timestamp_id (int, optional): The timestamp ID to retrieve data for.

                Returns:
                    dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
                """
        endpoint = "/vrsta_postupka"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_vrsta_pravnog_oblika(self, timestamp_id=None):
        """
               Retrieves information about types of legal forms.

               Args:
                   timestamp_id (int, optional): The timestamp ID to retrieve data for.

               Returns:
                   dict: The response from the API as a dictionary.

               Raises:
                   requests.HTTPError: If the API response was unsuccessful.
               """
        endpoint = "/vrsta_pravnog_oblika"
        params = {}
        if timestamp_id is not None:
            params["timestamp_id"] = timestamp_id
        response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
