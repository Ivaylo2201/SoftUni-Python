class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, value) -> None:
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value
        
    @property
    def password(self) -> str:
        return self.__password

    @staticmethod
    def is_valid(value: str) -> bool:
        letter_count, digit_count = 0, 0

        for i in value:
            if i.isdigit():
                digit_count += 1
            elif i.isalpha() and i.isupper():
                letter_count += 1

        if not (len(value) >= 8 and letter_count >= 1 and digit_count >= 1):
            return False

        return True

    @password.setter
    def password(self, value: str) -> None:
        if not self.is_valid(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
