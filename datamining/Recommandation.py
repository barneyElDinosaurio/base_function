# -*-coding=utf8-*-
import json
import math
import codecs

class recommander():
    def __init__(self, data, k=1, metric='pearson', n=5):
        self.data = data
        self.k = k
        self.metric = metric
        self.n=n
        if self.metric == 'pearson':
            self.fn = self.pearson
        self.username2id={}
        self.userid2name={}
        self.productid2name={}

    def convertProductID2name(self, id):
        """Given product id number return product name"""
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id


    def manhatt(self,rating1,rating2):
        s=0
        for key in rating1:
            if key in rating2:
                s+=abs(rating1-rating2)
        return s
    def computerManhatt(self,username):
        distance=[]
        for key in self.data:
            if username !=key:
                d=self.manhatt(self.data[username],self.data[key])
                distance.append((key,d))
        return sorted(distance,key=lambda x:x[1])

    def pearson(self, rating1, rating2):
        xy = 0
        sumX = 0
        sumY = 0
        sqr_X = 0
        sqr_Y = 0
        n = 0

        for key in rating1:
            if key in rating2:
                xy += rating1[key] * rating2[key]
                sumX += rating1[key]
                sumY += rating2[key]
                sqr_X += rating1[key] ** 2
                sqr_Y += rating2[key] ** 2
                n += 1
        if n==0:
            return 0
        denominator = math.sqrt(sqr_X - sumX ** 2 / float(n)) * math.sqrt(sqr_Y - sumY ** 2 / float(n))
        # not capture the denominator is zero !
        if denominator == 0:
            return 0
        else:
            return (xy - sumX * sumY / float(n)) / float(denominator)

    def computeNeighbour(self, username):
        distance = []
        for key in self.data:
            if key != username:
                d = self.fn(self.data[username], self.data[key])
                distance.append((key, d))

        return sorted(distance, key=lambda x: x[1], reverse=True)

    def recommand(self, user):
        recommand_list = {}
        distances = self.computeNeighbour(user)
        # 归一化person系数
        total=0
        for i in range(self.k):
            total+=float(distances[i][1])
        # distances_std=[]
        for i in range(self.k):
            pearson_std=float(distances[i][1])/total

            recommand_user=distances[i][0]

            for book in self.data[recommand_user]:
                if book not in self.data[user]:
                    if book not in recommand_list:
                        mark=float(self.data[recommand_user][book])*pearson_std
                        recommand_list[book]=mark
                    else:
                        mark=recommand_list[book]+float(self.data[recommand_user][book])*pearson_std
                        recommand_list[book]=mark
        # recommand_user = distances[0][0]
        # for item in self.data[recommand_user]:
        #     if item not in self.data[user]:
        #         recommand_list.append((item, self.data[recommand_user][item]))
        #
        recommand_list=list(recommand_list.items())
        # print recommand_list
        recommand_list=[(self.convertProductID2name(k),v) for (k,v) in recommand_list]
        recommand_list.sort(key=lambda x:x[1],reverse=True)

        return recommand_list[:self.n]
    def userRatings(self, id, n):
        """Return n top ratings for user with id"""
        print ("Ratings for " + self.userid2name[id])
        ratings = self.data[id]
        print(len(ratings))
        ratings = list(ratings.items())
        ratings = [(self.convertProductID2name(k), v)
                   for (k, v) in ratings]
        # finally sort and return
        ratings.sort(key=lambda artistTuple: artistTuple[1],
                     reverse = True)
        ratings = ratings[:n]
        for rating in ratings:
            print("%s\t%i" % (rating[0], rating[1]))
    def loadBookDB(self, path=''):
        """loads the BX book dataset. Path is where the BX files are
        located"""
        self.data = {}
        i = 0
        #
        # First load book ratings into self.data
        #
        f = codecs.open(path + "BX-Book-Ratings.csv", 'r', 'utf8')
        for line in f:
            i += 1
            # separate line into fields
            fields = line.split(';')
            user = fields[0].strip('"')
            book = fields[1].strip('"')
            rating = int(fields[2].strip().strip('"'))
            if user in self.data:
                currentRatings = self.data[user]
            else:
                currentRatings = {}
            currentRatings[book] = rating
            self.data[user] = currentRatings
        f.close()
        #
        # Now load books into self.productid2name
        # Books contains isbn, title, and author among other fields
        #
        f = codecs.open(path + "BX-Books.csv", 'r', 'utf8')
        for line in f:
            i += 1
            # separate line into fields
            fields = line.split(';')
            isbn = fields[0].strip('"')
            title = fields[1].strip('"')
            author = fields[2].strip().strip('"')
            title = title + ' by ' + author
            self.productid2name[isbn] = title
        f.close()
        #
        #  Now load user info into both self.userid2name and
        #  self.username2id
        #
        f = codecs.open(path + "BX-Users.csv", 'r', 'utf8')
        for line in f:
            i += 1
            # print(line)
            # separate line into fields
            fields = line.split(';')
            userid = fields[0].strip('"')
            location = fields[1].strip('"')
            if len(fields) > 3:
                age = fields[2].strip().strip('"')
            else:
                age = 'NULL'
            if age != 'NULL':
                value = location + '  (age: ' + age + ')'
            else:
                value = location
            self.userid2name[userid] = value
            self.username2id[location] = userid
        f.close()
        print(i)


def main():
    with open('user.json', 'r') as f:
        users = json.load(f)
    obj = recommander(data=users)
    obj.loadBookDB('')
    # print obj.recommand('171118')
    # print obj.recommand('Hailey')
    obj.userRatings('171118',5)

if __name__ == '__main__':
    main()
    print "Done"
