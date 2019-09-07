from sklearn.naive_bayes import MultinomialNB
from collections import Counter
import pandas as pd
import numpy as np
import pickle


class DataSetMaker:
    def __init__(self):
        self.readFile()

    def readFile(selfs):
        selfs.dataframe = pd.read_csv('spam.csv')

    def dictonary_maker(self):
        try:
            words = []
            data = []
            for i in range(len(self.dataframe)):
                words += self.dataframe.EmailText[i].split()
            for word in words:
                if word.isalpha():
                    data.append(word)
            self.dictonary = Counter(data)
            return self.dictonary
        except BaseException as e:
            print(e)
            return None

    def datasetMaker(self):
        labels = []
        data = []
        i = 0
        try:
            words = self.dataframe.EmailText[0].split()
            for entry in self.dictonary:
                data.append(words.count(entry))
            features = np.array([data])
            data = []

            for email in self.dataframe.EmailText[1:]:
                words = email.split()
                for entry in self.dictonary:
                    data.append(words.count(entry))
                features = np.concatenate((features, [data]), axis=0)
                data = []
                print(i)
                if self.dataframe.Label[i] == 'spam':
                    labels.append(1)
                if self.dataframe.Label[i] == 'ham':
                    labels.append(0)
                i += 1
            else:
                if self.dataframe.Label[i] == 'spam':
                    labels.append(1)
                if self.dataframe.Label[i] == 'ham':
                    labels.append(0)

            features = np.array(features)

            labels = np.array(labels)
            return features, labels
        except BaseException as e:
            print(e)
            return None


class TrainModel:
    def model(self, features, labels):
        self.features = features
        self.labels = labels
        self.model = MultinomialNB()
        self.model.fit(self.features, self.labels)
        return self.model

    def testModel(self, test_features, test_labels):
        self.test_features = test_features
        self.test_labels = test_labels
        score = 0
        self.test_prd_labels = self.model.predict(self.test_features)
        for i in range(len(self.test_prd_labels)):
            if self.test_prd_labels[i] == self.test_labels[i]:
                score += 1

        accuracy = score / len(self.test_labels)
        return accuracy


class QueryTransformation:
    def queryTrans(self, dictonary, query):
        self.dictonary = dictonary
        self.query = query
        t_query = []
        data = []
        words = self.query.split()
        for entry in self.dictonary:
            data.append(words.count(entry))
        t_query.append(data)
        return t_query


class Predict:
    def prdict(self, query, model):
        self.query = query
        self.model = model
        res = model.predict(self.query)
        return res


if __name__ == '__main__':

    d = DataSetMaker()
    dictonary = d.dictonary_maker()

    with open('dictonary.dat', 'wb') as f:
        pickle.dump(dictonary, f)  # dumping for future use

    print('dictonary completed.....')
    features, labels = d.datasetMaker()
    x_train, y_train = features[0:4800], labels[0:4800]
    x_test, y_test = features[4800:], labels[4800:]
    print('data set ready.....')
    print('training start.....')
    t = TrainModel()
    model = t.model(x_train, y_train)
    print('model ready.....')

    with open('MultinomialNB_model.dat', 'wb') as f:
        pickle.dump(model, f)

    accuracy = t.testModel(x_test, y_test)
    print('accuracy is', accuracy)

    while True:
        query = input('Entery query: ')
        t_q = QueryTransformation()
        t_query = t_q.queryTrans(dictonary, query)
        ped = Predict()
        res = ped.prdict(t_query, model)
        if str(res) == '[0]':
            print('ham')
        else:
            print('spam')