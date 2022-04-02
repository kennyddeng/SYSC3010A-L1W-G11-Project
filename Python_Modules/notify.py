from twilio.rest import Client ## pip install twilio

class Notify:
    """
    Notify class that uses twilio API to connect to twilio account and send SMS messages.
    The notify_users method can be used to send the notifications.
    """
    def __init__(self):
        account_sid = 'ACd18afd79f85de08f908fa9223c1dc5b7'
        auth_token = '545bdf8fe73b432baf53086af5197898'
        self._config = {"account_sid": account_sid, "auth_token": auth_token}

        # List of numbers to message for notifications
        # 1: Kenny, 2: Cristian, 3: Chris
        self._message_list = {1: '+13432041697', 2: '+16134087355', 3: '+16472619243'}

    def notify_users(self, msg, users="All"):
        """
        Notfies the specified users with the message

        :type msg: Str
        :param msg: The message to be sent to users
        :type users: Str
        :param users: The users to send the message to. Defaults to "All" otherwise specify the key
        for the user to send the message to. Options are 1, 2, and 3. 
        """
        if users == "All":
            numbers = self._message_list.values()
        else:
            if users not in (1, 2, 3):
                print("User must be either 1, 2, or 3")
                return
            numbers = [self._message_list[users]]

        client = Client(self._config['account_sid'], self._config['auth_token'])

        messages = []

        for number in numbers:
            message = client.messages \
                .create(
                    body=msg,
                    from_='+17578013197',
                    to=number
                )
            if (message.status == 'queued'):
                messages.append(message.status)
                print("Message Sent")

        return messages


if __name__ == "__main__":
    # Instantiate Class
    notify = Notify()

    # Create message and users
    msg = "Hello world"
    user = 2 # Cristian's number

    # Send to specified user
    status = notify.notify_users(msg=msg, users=user)

    # Get status
    if status[0] == "queued":
        print("Message Sent")

    # Send to all users
    #notify.notify_users(msg=msg)
