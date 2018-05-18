from flask_restplus import fields
from da_rest_api.api.restplus import api
import numpy as np


class FormattedFloat(fields.Float):

    def format(self, value):
        if value != value:
            return None
        if type(value).__module__ == np.__name__:
            return round(float(value.item()), 2)
        return round(float(value), 2)


class FormattedInteger(fields.Integer):

    def format(self, value):
        if type(value).__module__ == np.__name__:
            return int(value.item())
        return int(value)

base_provider_risk_score = provider_risk_score = api.model('Risk Score', {
    'id': fields.Integer(readOnly=True, description='The unique identifier for a provider'),
    'paid': FormattedFloat(readOnly=True, description='Paid amound associated with the risk score'),
    'score': fields.Integer(readOnly=True, description='Aggregate risk score based on predictive analytics')
})

provider_risk_score = api.model('Risk Score', {
    'id': fields.Integer(readOnly=True, description='The unique identifier for a provider'),
    'timeStamp': fields.Integer(readOnly=True, description='Timestamp of when risk score was generated'),
    'paid': FormattedFloat(readOnly=True, description='Paid amound associated with the risk score'),
    'score': fields.Integer(readOnly=True, description='Aggregate risk score based on predictive analytics')
})

pagination = api.model('A page of results', {
    'timeStamp': fields.Integer(readOnly=True, description='Timestamp of when risk score was generated'),
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'perPage': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_provider_risk_scores = api.inherit('Page of provider risk scores', pagination, {
    'scores': fields.List(fields.Nested(base_provider_risk_score))
})
