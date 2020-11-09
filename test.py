def add_to_dict(towhat, key, value):
    info = towhat.get(key, [])
    info.append(value)
    towhat[key] = info

alternate = {}

add_to_dict(alternate,"Andrew","Cambridge")
add_to_dict(alternate,"Barbara","Bloomsbury")
add_to_dict(alternate,"Andrew","Corsica")

print(alternate)