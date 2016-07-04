import unittest
import urllib2
import json

webserver = "http://127.0.0.1:5000/posts/"

class TestStringMethods(unittest.TestCase):
    def test_bringup(self):
        print "Bringing up the webserver"
        pass
    def test_ParameterSet(self):
	resp = json.loads(urllib2.urlopen(webserver).read())
        self.assertEqual(resp["error"], "Operation failed")
        pass
    def test_AllParameterSet(self):
        resp = json.loads(urllib2.urlopen(webserver + "?subreddit=img").read())
        self.assertEqual(resp["error"], "Operation failed")
        resp = json.loads(urllib2.urlopen(webserver + "?from=4&to=6").read())
        self.assertEqual(resp["error"], "Operation failed")
        resp = json.loads(urllib2.urlopen(webserver + "?keyword=help").read())
        self.assertEqual(resp["error"], "Operation failed")
        resp = json.loads(urllib2.urlopen(webserver + "?other=help").read())
	self.assertEqual(resp["error"], "Operation failed")
        pass
    def test_timeIsAnInteger(self):
        resp = json.loads(urllib2.urlopen(webserver +
                                          "?subreddit=f&from=2&to=a").read())
        self.assertEqual(resp["error"], "Operation failed");
        pass

if __name__ == '__main__':
    unittest.main()
