import sys

from paypalcheckoutsdk.core import SandboxEnvironment, PayPalHttpClient

class PayPalClient:
    def __init__(self):
        self.client_id = 'AVib1FxGF5SQO8QBTAmemo3pDOeQi6D6eymifwn_Ktqu9MOd35VBreZf5mhI0EKpBtieyYKJ_eyNrRKu'
        self.client_secret = 'EH85uEtaZpcZ5-JqORD2WnWdoGl4gT-R-LbWjNUq2Fz9amGMjftm5P4MeVVGZocx5M3_fnYTR7hid81C'
        self.enviroment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.enviroment)