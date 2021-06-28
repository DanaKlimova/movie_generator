from flask import (
    abort,
    make_response,
)


MOVIES = {
    "1": {
        "id": 1,
        "name": "movie 1",
        "year": "2001",
    },
    "2": {
        "id": 2,
        "name": "movie 2",
        "year": "2002",
    },
    "3": {
        "id": 3,
        "name": "movie 3",
        "year": "2003",
    },
}


def get_list():
    return list(MOVIES.values())


def get(id):
    return list(filter(
        lambda movie: movie["id"] == int(id),
        list(MOVIES.values())
    ))


def post(data):
    name = data.get("name", None)
    year = data.get("year", None)

    if not name or not year:
        abort(400, "Name and year are required.")
    else:
        id = int(sorted(MOVIES.keys())[-1]) + 1
        MOVIES[str(id)] = {
            "id": id,
            "name": name,
            "year": year,
        }
        return make_response(f"{name} successfully created", 201)


def update(id, data):
    name = data.get("name", None)
    year = data.get("year", None)

    if not name or not year:
        abort(400, "Name and year are required.")

    movies = list(filter(
        lambda movie: movie["id"] == int(id),
        list(MOVIES.values())
    ))
    if not movies:
        abort(404, f"Movie with {id} id not found")
    else:
        movies[0]["name"] = name
        movies[0]["year"] = year
    return movies[0]


def delete(id):
    if id in MOVIES:
        del MOVIES[id]
        return make_response(f"Movie with {id} id successfully deleted", 200)
    else:
        abort(404, f"Movie with {id} id not found")
