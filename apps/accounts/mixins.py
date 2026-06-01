from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Accès réservé au personnel connecté (groupe Staff ou supérieur)."""

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (
            user.is_superuser
            or user.groups.filter(
                name__in=["SuperAdmin", "Communicator", "ProgramManager", "Staff"]
            ).exists()
        )


class ProgramManagerRequiredMixin(StaffRequiredMixin):
    def test_func(self):
        if not super().test_func():
            return False
        user = self.request.user
        return user.is_superuser or user.groups.filter(
            name__in=["SuperAdmin", "ProgramManager"]
        ).exists()


class CommunicatorRequiredMixin(StaffRequiredMixin):
    def test_func(self):
        if not super().test_func():
            return False
        user = self.request.user
        return user.is_superuser or user.groups.filter(
            name__in=["SuperAdmin", "Communicator"]
        ).exists()
