"""Create the authentication users table for local development.

Run from the alternate_credit_backend directory:
    python -m scripts.init_auth_db

The MySQL server and credit_auth_db database must already exist.
"""
from app.db import Base, engine
from app.models.user_models import User  # noqa: F401 - registers model metadata


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("Authentication table(s) created or already present.")


if __name__ == "__main__":
    main()
