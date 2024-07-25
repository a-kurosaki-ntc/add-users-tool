from db.database import db_session
from models.user import User
from models.usecase import Usecase
from models.user_usecase import UserUsecase
from models.configuration import Configuration

import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python register_user.py <email> <is_admin>')
        sys.exit(1)
    
    with db_session() as session:
        email = sys.argv[1]
        is_admin = int(sys.argv[2])
        configurations = session.query(Configuration)
        configurations_dict = {c.key: c.value for c in configurations}
        user_limit = int(configurations_dict["user_limit"])
        if session.query(User).count() >= user_limit:
            print("User limit exceeded")
            sys.exit(1)
        if session.query(User).filter(User.email == email).count() > 0:
            print("User already exists")
            sys.exit(1)
        user = User("", "", email, is_admin)
        try:
            session.add(user)
            for usecase in session.query(Usecase).all():
                if not usecase.is_public and not user.is_admin:
                    continue
                user_usecase = UserUsecase(user.id, usecase.id)
                session.add(user_usecase)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            sys.exit(1)
    
    print("User registered successfully")
