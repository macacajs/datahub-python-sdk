import json
import urllib
import urllib2

class DataHubSDK:
    def __init__(self, protocol = 'http', hostname = '127.0.0.1', port = '5678'):
        """Initialize the MemorizeFormatter."""
        self.rootUrl = '{0}://{1}:{2}'.format(protocol, hostname, port)

    def updateSceneByProjectIdAndDataId(self, projectId, dataId, data):
        print(projectId, dataId, data)
        res = self.getDataByProjectIdAndDataId(projectId, dataId)
        if not res['success']:
            return '123'

        url = '{0}/api/data/{1}/{2}'.format(self.rootUrl, projectId, dataId)
        print(url, data)
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        req = urllib2.Request(url, urllib.urlencode(data), headers)
        response = urllib2.urlopen(req)
        res = json.loads(response.read())
        print(res['success'])
        response.close()
        return res

    def getDataListByProjectId(self, projectId, data):
        """Initialize the MemorizeFormatter."""
        url = '{0}/api/data/{1}'.format(self.rootUrl, projectId)
        print(url, data)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        res = json.loads(response.read())
        return res

    def getDataByProjectIdAndDataId(self, projectId, dataId):
        url = '{0}/api/data/{1}/{2}'.format(self.rootUrl, projectId, dataId)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        res = json.loads(response.read())
        response.close()
        return res


