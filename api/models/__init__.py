# -*- coding: utf-8 -*-

from api import db
from sqlalchemy.dialects.postgresql import JSON

from api.models.user import User
from api.models.search import Result
from api.models.products import Incredient, Product
