import requests


def upcoming_launches(count):
    """

    :param count: count of launches
    :return:
    """
    result = []
    response = requests.get("https://launchlibrary.net/1.3/launch?next={}&mode=verbose".format(count)).json()
    for launch in response["launches"]:
        name = launch["name"]
        net = launch["net"]
        location = launch["location"]["pads"][0]["name"]
        tbdtime = launch["tbdtime"]
        tbddate = launch["tbddate"]
        if int(tbddate) == 0 and int(tbdtime) == 0:
            tbd = False
        else:
            tbd = True
        result.append({"name": name, "net": net, "location": location, "tbd": tbd})
    return result


def weather():
    pass


def money():
    pass


def hello():
    pass
