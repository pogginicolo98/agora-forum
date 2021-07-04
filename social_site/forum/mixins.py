from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixin(UserPassesTestMixin):
    """ The objective of this mixin is permit only to staff users create new sections """

    def test_func(self):
        return self.request.user.is_staff
