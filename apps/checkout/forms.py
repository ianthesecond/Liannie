from oscar.apps.checkout.forms import ShippingAddressForm as CoreShippingAddressForm

class ShippingAddressForm(CoreShippingAddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.line4 = "Jakarta"
    
    class Meta(CoreShippingAddressForm.Meta):
        fields = [
            'title', 'first_name', 'last_name', 'line1', 'country', 'phone_number', 'notes',
        ]