
class CreditCardPurchase:
    POSSIBLE_CATEGORIES = ['בילויים', 'סופרמרקט', 'ביגוד', 'אלקטרוניקה', 'חיות מחמד', 'בריאות', 'רכב', 'בנק', None]
    NONE_CATEGORY = 'אחר'

    def __init__(self, purchase_text):
        self._purchase_text = purchase_text
        self.price = None
        self.time = None
        self.location = None
        self.category = None

    def to_dict(self):
        return {'price': self.price, 'time': self.time, 'location': self.location, 'category': self.category}

    def _extract_text_information(self):
        pass

    def _extract_category(self):
        pass

    def _query_location_at_google(self):
        pass


class Word2Vec:
    pass
