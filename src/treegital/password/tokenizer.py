# -*- coding: utf-8 -*-

import hashlib
import hmac

from datetime import date, timedelta
from zope.interface import Interface, implementer


class ITokenFactory(Interface):
    """A unique token factory
    """

    def create(word):
        """returns a hex representation of a tokenized word.
        """

    def verify(word, challenger):
        """returns a bool. True is tokenized word == challenged.
        False otherwise.
        """


@implementer(ITokenFactory)
class ShaTokenFactory(object):
    """A sha based token factory

    An alternative would be a token factory storing random token.
    The advantage of this solution is that we don't need to manage sweeping
    of old entry.

    The token is valid for a few days
    """

    def __init__(self, secret, validity=3):
        self.secret = secret
        self.validity = validity

    @property
    def today(self):
        """isolated for testing purpose"""
        return date.today()

    def create(self, word):
        token = hmac.new(key=self.secret, digestmod=hashlib.sha256)
        token.update(word)
        token.update(str(self.today))
        return token.hexdigest()

    def verify(self, word, challenger):
        today = self.today
        basetoken = hmac.new(key=self.secret, digestmod=hashlib.sha256)
        basetoken.update(word)
        for n in range(self.validity):
            token = basetoken.copy()
            token.update(str(today - timedelta(n)))
            if token.hexdigest() == challenger:
                return True
        return False
