class DataRepository():
    configFile = 'config.txt'

    def addConnection(self, data):
        host = data['host']
        port = str(data['port'])
        pwd = data['pwd']
        login = data['login']
        name = data['name']

        stringToSave = '|'.join([login, host, port, pwd, name])

        with open(self.configFile, "a") as f:
            f.write(stringToSave + '|\n')

    def getConnectionsArray(self):
        with open(self.configFile) as file:
            lines = file.readlines()

        result = []
        for line in lines:
            lineArr = line.split('|')
            connectionRow = {}
            connectionRow['login'] = lineArr[0]
            connectionRow['host'] = lineArr[1]
            connectionRow['port'] = lineArr[2]
            connectionRow['pwd'] = lineArr[3]
            connectionRow['name'] = lineArr[4]
            result.append(connectionRow)
        return result