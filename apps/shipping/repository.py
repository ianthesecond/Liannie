from oscar.apps.shipping.repository import Repository as CoreRepository

from oscar.core.loading import get_class

StandardDelivery = get_class('shipping.methods', 'StandardDelivery')

class Repository(CoreRepository):
    methods = (StandardDelivery(),)



