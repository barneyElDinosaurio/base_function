# -*-coding=utf-8-*-
import math

music = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1,
                                 "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4,
                                           "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5,
                                        "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5,
                                         "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar": 4, "backup vocals": 5,
                                     "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1,
                                 "rap": 1},
         "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2,
                                            "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2,
                                 "rap": 1}}

def manthatt(band1,band2):
    s=0
    for key in band1:
        s+=abs(band1[key]-band2[key])
    return s

def oula_distance(band1, band2):
    s = 0
    for key in band1:
        s += (band1[key] - band2[key]) ** 2
    return math.sqrt(s)


def computeNeighbor(username, user):
    recommands = []
    for k in user:
        distance = 0
        if k != username:
            # distance=MinkovskiDistance(user,username,k,2)
            distance = manthatt(user[k], user[username])
            recommands.append((k,distance))


    # print(recommands)
    return sorted(recommands, key=lambda x: x[1])


def normalize():
    pass
def main():
    # print(oula_distance(music['Glee Cast/Jessie\'s Girl'], music['Dr Dog/Fate']))
    print(computeNeighbor('The Black Keys/Magic Potion', music))


if __name__ == '__main__':
    main()
