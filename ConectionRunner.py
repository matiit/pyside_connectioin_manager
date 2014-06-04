import os

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

class ConnectionRunner:
    credentials = {}

    def __init__(self, credentials):
        self.checkDependencies()
        self.credentials = credentials

    def checkDependencies(self):
        if (which('sshpasss') is None):
            raise Exception("You need to install sshpass! [ sudo apt-get install sshpass ] if you "
                            "use Debian like OS")

    def run(self):
        #  dataRep = DataRepository()
        # host = self.hostnameInput.text()
        # port = self.portSpinBox.value()
        # pwd = self.passwordInput.text()
        # login = self.userNameInput.text()
        # name = self.connectionNameInput.text()

        executableConnectionString = self.buildExecutableConnectionString()

        os.systen('terminator -e \'' + executableConnectionString + '\'')

    def buildExecutableConnectionString(self):
        login = self.credentials['login']
        pwd = self.credentials['pwd']
        port = self.credentials['port']
        host = self.credentials['host']

        return 'sshpass -p ' + pwd +' ssh '+ login +'@' + host + ' -p ' + port

