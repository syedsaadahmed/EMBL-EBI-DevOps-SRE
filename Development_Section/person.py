from flask import make_response, abort

PERSON = {
    "john": {
        "first_name": "john",
        "last_name": "skeet",
        "age": "22",
        "favourite_color": "green",
    },
    "Adam": {
        "first_name": "Adam",
        "last_name": "Gilchrist",
        "age": "25",
        "favourite_color": "yellow",
    },
    "Donald": {
        "first_name": "Donald",
        "last_name": "Trump",
        "age": "30",
        "favourite_color": "red",
    },
}

def get_all():
    # get_all_values = [] 
    # for key in PERSON.keys():
    #     get_all_values.append(PERSON[key])
    # return get_all_values
    return [PERSON[key] for key in sorted(PERSON.keys())]

def get_one(first_name):
    if first_name in PERSON:
        person = PERSON.get(first_name)
    else:
        abort(
            404, "Person with first name {first_name}, not found".format(first_name=first_name)
        )
    return person

def delete(first_name):
    if first_name in PERSON:
        del PERSON[first_name]
        return make_response(
            "Person with first name {first_name} successfully deleted".format(first_name=first_name), 200
        )
    else:
        abort(
            404, "Person with first name {first_name} not found".format(first_name=first_name)
        )

def add(person):
    first_name = person.get("first_name", None)
    last_name = person.get("last_name", None)
    age = person.get("age", None)
    favourite_color = person.get("favourite_color", None)


    if first_name not in PERSON and first_name is not None:
        PERSON[first_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "favourite_color": favourite_color,
        }
        return make_response(
            "{first_name} record successfully created".format(first_name=first_name), 201
        )
    else:
        abort(
            406,
            "Person with first name {first_name} already exists".format(first_name=first_name),
        )

def update(first_name, person):
    if first_name in PERSON:
        PERSON[first_name]["last_name"] = person.get("last_name")
        PERSON[first_name]["age"] = person.get("age")
        PERSON[first_name]["favourite_color"] = person.get("favourite_color")

        return PERSON[first_name]
    else:
        abort(
            404, "Person with first name {first_name} not found in the list".format(first_name=first_name)
        )