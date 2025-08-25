def parse(response: dict) -> list[str]:
    logins = []
    if "people" in response and "result" in response["people"]:
        for person in response["people"]["result"]:
            if "login" in person:
                logins.append(person["login"])
    return logins