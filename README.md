# SudReg

##### A light weight Python library for the SudReg Web API

## Documentation

SudReg Web API's full documentation is online at [Sudski registar api - javni korisnici](https://sudreg-podaci.pravosudje.hr/docs/services/5adda5d214bb2910b8322a96/operations/bris_pravni_oblik_Get).

## Installation

```bash
pip install sudreg
```

## Quick Start

```python
from sudreg import SudskiRegistarAPI

api = SudskiRegistarAPI("Subscription-Key")

print(api.get_subjekt_detalji(tip_identifikatora="oib", identifikator="53056966535", expand_relations=True))

```