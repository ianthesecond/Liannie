from oscar.core.loading import get_class

CoreUserAddressForm = get_class('address.forms', 'UserAddressForm')

class UserAddressForm(CoreUserAddressForm):
    class Meta(CoreUserAddressForm.Meta):
        fields = [
            'title', 'first_name', 'last_name', 'line1', 'country', 'phone_number', 'notes',
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.line4 = "Jakarta"