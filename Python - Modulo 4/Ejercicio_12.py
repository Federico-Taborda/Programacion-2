def conjunto(conjunto1:set, conjunto2:set) -> set:
    return conjunto1 - conjunto2 | conjunto2 - conjunto1