from Products.validation.interfaces.IValidator import IValidator
from DateTime import DateTime

from zope.interface import implements

class ValidateStartNEndDate(object):
    """ Validate start date and end date. """
    implements(IValidator)

    #Above line is important otherwise we will get an FalseValidatorError:
    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        """Validator code"""
        start_date =  kwargs['REQUEST'].get('start_date')
        end_date =  kwargs['REQUEST'].get('end_date')
        try:
            start_date = DateTime(start_date)
            end_date = DateTime(end_date)
        except:
            return """Please choose the valid start/end date."""
        
        if start_date > end_date:
            return """Start date should be lesser than End date."""
        return True
