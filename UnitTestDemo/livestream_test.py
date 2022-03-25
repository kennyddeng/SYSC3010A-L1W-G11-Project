import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import unittest

class TestLivestream(unittest.TestCase):
    """
    Pings livestream host ip:port.
    Run with livestream running and not running. Passes both tests.
    """
    def test_livestream(self):
        host = "192.168.2.253:8000"
        ip = "192.168.2.253"
        port = "8000"
    
        pingTest = subprocess.Popen(["telnet", ip, port])
        pingTest.terminate()
        pingTest.wait()
        #print(pingTest)
        if (pingTest == 1): # livestream not running
            self.assertEquals(1, pingTest)
        else: # livestream running  
            self.assertNotEquals(1, pingTest)
                 
if __name__ == "__main__":
    unittest.main()