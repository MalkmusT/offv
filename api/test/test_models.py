from api.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and name fields are defined correctly
    """
    user = User('patkennedy79@gmail.com', 'FlaskIsNotAwesome','Pat')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.password != 'FlaskIsAwesome'
    assert user.name == 'Pat'
