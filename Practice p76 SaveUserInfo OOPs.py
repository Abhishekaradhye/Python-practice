"""Create a class SaveUserInfo to store user details: name, email, phone number, and optional address.
Implement input validation to ensure name has no digits, email contains '@', and phone number is numeric.
Raise exceptions for any invalid or missing mandatory fields.
Store each valid user object in a class-level list user_info.
Provide a method save_info to perform validation and save the user."""

class SaveUserInfo:
    user_info = []

    def __init__(self, name, email, phone_number, address='NA'):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def save_info(self):
        if not self.name or not self.email or not self.phone_number:
            raise Exception("Mandatory information not entered!")

        for char in self.name.split():
            if char.isdigit():
                raise Exception("Please enter valid name")

        if "@" not in self.email:
            raise Exception("Please enter valid email.")

        if not self.phone_number.isdigit():
            raise Exception("Please enter valid phone number.")

        SaveUserInfo.user_info.append(self)
