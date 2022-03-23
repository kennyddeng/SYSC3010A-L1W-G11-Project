import unittest
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class SenseHatTest(unittest.TestCase):
    """
    Sense Hat unit tests
    """
    def test_temp_change(self):
        """
        This test takes the current temperature, waits 30 seconds, and then takes the temperature again.
        Assuming a fan is on, the test passes if the difference between temperatures is >= 1.

        Command line run: python3 sense_hat_test.py SenseHatTest.test_temp_change
        """
        temp1 = round(sense.get_temperature(), 1)
        sleep(30)
        temp2 = round(sense.get_temperature(), 2)
        difference = abs(temp2-temp1)
        print(difference)
        self.assertTrue(difference >= 1)

    def test_button(self):
        """
        This test waits for a stick event on the Sense Hat. 
        Once an event occurs, the test passes if the stick event is a "press".

        Command line run: python3 sense_hat_test.py SenseHatTest.test_button
        """
        event = sense.stick.wait_for_event()
        if event.action:
            self.assertTrue(event.action == "pressed")   

if __name__ == '__main__':
    unittest.main()