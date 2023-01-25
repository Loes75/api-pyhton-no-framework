from typing import List, Any, Dict, Union


class Commons:

    @staticmethod
    def serialize_generics_models(_list: List[Any]) -> List[Dict]:
        return [_mod.to_dict() for _mod in _list]
