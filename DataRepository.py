class DataRepository():
    configFile = 'config.txt'

    def addConnection(self, data):
        host = data['host']
        port = str(data['port'])
        pwd = data['pwd']
        login = data['login']
        name = data['name']

        stringToSave = '|'.join([login,host,port,pwd,name])

        with open(self.configFile, "a") as f:
            f.writelines([stringToSave])
