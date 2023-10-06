from faker import Faker
import logging
from pathlib import Path

BAS_DIR=Path(__file__).resolve().parent

logging.basicConfig(filename=BAS_DIR/'user.log', 
                    filemode="a",
                    level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(message)s')


fake=Faker(locale="fr_FR")

"""Module To Generate a random User"""

def get_user():

    """Generate a single User

    Returns:
        str: user
    """
    logging.info("Generate User")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(num_users):
    """Generate a list of users

    Args:
        num_users (int): number of users

    Returns:
        List[str]: users
    """
    users=[]
    for _ in range(num_users):
        users.append(get_user())
    logging.info(f"Generate a list of {num_users} users.")
    return users

if __name__=="__main__":
    nom=get_users(num_users=5)
    print(nom)
