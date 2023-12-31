from Wild_Cat_Zoo.project import User
from Wild_Cat_Zoo.project import Library


class Registration:
    @staticmethod
    def add_user(user: User, library: Library) -> str or None:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library) -> str or None:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        for u in library.user_records:
            if u.user_id == user_id and u.username != new_username:
                data = library.rented_books[u.username]
                u.username = new_username
                library.rented_books[u.username] = data

                return f"Username successfully changed to: {new_username} for user id: {user_id}"

            elif u.user_id == user_id and u.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
