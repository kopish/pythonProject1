# example_4.py

class BasePhone:
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def call_to(self, contact_name):
        pass

    def set_alarm_for(self, time):
        pass

    def open_sms_from(self, contact_name):
        pass

    def lock_screen(self):
        pass


class Nokia(BasePhone):
    DATA = {
        "contacts": {
            "David": {
                "phone": "+380991231231",
                "SMS": [
                    "Hello, guy!"
                ]
            },
            "Kate": {
                "phone": "+380991765231",
                "SMS": [
                    "Can we meet next morning?"
                ]
            }
        },
        "alarms": [],
        "status": "unlocked",
    }

    def call_to(self, contact_name):
        if not self.DATA['status'] == "lock":
            contact_phone = self.DATA["contacts"][contact_name]["phone"]
            print(f"Calling to {contact_name} with phone number {contact_phone}")

    def set_alarm_for(self, time):
        if not self.DATA['status'] == "lock":
            self.DATA["alarms"].append(time)
            print(f"Alarms was set for {time}. All alarms: {self.DATA['alarms']}")

    def open_sms_from(self, contact_name):
        if not self.DATA['status'] == "lock":
            SMS = self.DATA['contacts'][contact_name]["SMS"]
            print(f"All SMS from {contact_name}: {SMS}")

    def lock_screen(self):
        self.DATA["status"] = "lock"


class Samsung(BasePhone):
    DATA = {
        "contacts": {
            "David": {
                "phone": "+380991231231",
                "SMS": [
                    "Hello, guy!"
                ]
            },
            "Kate": {
                "phone": "+380991765231",
                "SMS": [
                    "Can we meet next morning?"
                ]
            }
        },
        "alarms": [],
        "status": "unlocked",
    }

    def _get_contact(self, contact_name):
        return self.DATA["contacts"][contact_name]

    def _get_contact_sms(self, contact_name):
        contact = self._get_contact(contact_name)
        return contact["SMS"]

    def _get_contact_phone(self, contact_name):
        contact = self._get_contact(contact_name)
        return contact["phone"]

    def _get_alarms(self):
        return self.DATA["alarms"]

    def _set_status(self, lock):
        self.DATA["status"] = "lock"

    def _set_alarm_for(self, time):
        self.DATA["alarms"].append(time)

    def _is_phone_unlock(self):
        phone_status = self.DATA["status"]

        if phone_status == "unlocked":
            return True
        else:
            print("WARNING: You can't get access to locked phone!")
            return False

    def lock_screen(self):
        self._set_status("lock")

    def call_to(self, contact_name):
        if self._is_phone_unlock():
            phone_number = self._get_contact_phone(contact_name)
            print(f"Calling to {contact_name} with phone number {phone_number}")

    def set_alarm_for(self, time):
        if self._is_phone_unlock():
            self._set_alarm_for(time)
            all_alarms = self._get_alarms()
            print(f"Alarms was set for {time}. All alarms: {all_alarms}")

    def open_sms_from(self, contact_name):
        if self._is_phone_unlock():
            contact_sms = self._get_contact_sms(contact_name)
            print(f"All SMS from {contact_name}: {contact_sms}")


def test_my_phone(phone):
    phone.call_to("David")
    phone.set_alarm_for("6:00")
    phone.open_sms_from("Kate")
    phone.lock_screen()
    phone.open_sms_from("Kate")


nokia_phone = Nokia(owner_name="Oleg")     # same to Nokia("Oleg")
samsung_phone = Samsung(owner_name="Oleg") # same to Samsung("Oleg")

print(" Test Nokia phone ".center(50, "="))
test_my_phone(nokia_phone)

print()

print(" Test Samsung phone ".center(50, "="))
test_my_phone(samsung_phone)

