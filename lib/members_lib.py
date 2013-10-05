class Person(object):
    def __init__(self, name='NoName', email='sample@uclive.ac.nz', phone='000'):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return 'Name: {}\nEmail: {}\nPhone: {}\n'.format(self.name, self.email, self.phone)