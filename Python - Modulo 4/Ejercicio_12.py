def conjunto(conjunto1:set, conjunto2:set) -> set:
    return conjunto1 - conjunto2 | conjunto2 - conjunto1

print(conjunto({1,2,3,4}, {3,4,5,6}))