from typing import Callable

def session_decorator(session):
    def decorator(callback: Callable):
        def wrapper(*args, **kwargs):
            try:
                result = callback(*args, **kwargs)
                session.commit()

                return result

            except Exception as e:
                session.rollback()
                raise e

            finally:
                session.close()

        return wrapper
    return decorator
