from db.database import db_session
from models.user import User

import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python register_user.py <email> <is_admin>')
        sys.exit(1)
    
    with db_session() as session:
        email = sys.argv[1]
        is_admin = int(sys.argv[2])
        if session.query(User).filter(User.email == email).count() > 0:
            print("User already exists")
            sys.exit(1)
        user = User("", "", email, is_admin)
        try:
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            sys.exit(1)
    
    print("User registered successfully")
