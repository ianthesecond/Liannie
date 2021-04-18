from oscar.apps.shipping.methods import FixedPrice as CoreFixedPrice

class StandardDelivery(CoreFixedPrice):
    code = 'standard'
    name = 'Standard delivery'
    charge_excl_tax = 15000

