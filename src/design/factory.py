class User1:
    def do_work(self):
        print('one')


class User2:
    def do_work(self):
        print('two')


class UserFactory:
    user_types = {
        'user1': User1,
        'user2': User2,
    }

    @classmethod
    def create_user(cls, user_type):
        return cls.user_types.get(user_type.lower())


if __name__ == '__main__':
    User = UserFactory().create_user('user1')
    User().do_work()

    User = UserFactory().create_user('user2')
    User().do_work()