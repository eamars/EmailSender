import sys
if sys.version_info < (3, 0):
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

def removeSpace(instring):
    outstring = ''
    for char in instring:
        if char == ' ':
            outstring += '%20'
        else:
            outstring += char
    return outstring

class BugReport(object):
    def __init__(self, appName, appVersion, OSVersion=str(sys.version_info)):
        self.BUG_REPORT_LINK = "http://bugtrackrsys.appspot.com/add/?application={}&ver={}&platform={}&level={}&description={}"
        self.OS_VERSION = removeSpace(OSVersion)
        self.applicationName = removeSpace(appName)
        self.applicationVersion = appVersion

    def submit(self, level, errorDescriptions):
        self.errorlevel = level
        self.errorLog = removeSpace(errorDescriptions)
        url = self.BUG_REPORT_LINK.format(self.applicationName, self.applicationVersion, self.OS_VERSION, self.errorlevel, self.errorLog)
        urlopen(url)

if __name__ == '__main__':
    a = BugReport('PythonTestProgram', '1.0')
    a.submit('Normal', 'None')