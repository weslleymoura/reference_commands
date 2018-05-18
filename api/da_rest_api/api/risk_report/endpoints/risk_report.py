import logging
import pandas as pd
import os
import time
from time import gmtime, strftime, time
import boto3
from flask import request
from flask_restplus import Resource, abort
from da_rest_api.api.risk_report.serializers import provider_risk_score, page_of_provider_risk_scores
from da_rest_api.api.risk_report.parsers import provider_arguments, pagination_arguments
from da_rest_api.api.restplus import api
from math import ceil
import inspect
import sys
import json
import warnings
warnings.filterwarnings('ignore')

# Set path
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# Get time
init_time = int(time())

# Logging
log = logging.getLogger(__name__)

# Data
d = {'id': [1, 2, 3], 'score': [0.1, 0.5, 0.8], 'paid': [100,200,300]}
df_provider = pd.DataFrame(data = d)

# Set name space
ns = api.namespace('risk-report', description='Operations related to the risk report')

# filtering
def filter_risk_report(df, filter_args):
    scoreGT = filter_args.get('scoreGT', None)
    scoreLT = filter_args.get('scoreLT', None)
    paidGT = filter_args.get('paidGT', None)
    paidLT = filter_args.get('paidLT', None)

    if scoreGT:
        df = df[df['score'] > scoreGT]

    if scoreLT:
        df = df[df['score'] < scoreLT]

    if paidGT:
        df = df[df['paid'] > paidGT]

    if paidLT:
        df = df[df['paid'] < paidLT]

    return df

@ns.route('/providers')
class ProviderCollection(Resource):

    @api.expect(provider_arguments)
    @api.marshal_with(page_of_provider_risk_scores)
    def get(self):
        """
        Returns ordered list (by risk score) of providers.
        """
        provider_args = provider_arguments.parse_args(request)
        page = provider_args.get('page', 1)

        risk_report_list = filter_risk_report(df_provider, provider_args)

        if len(risk_report_list) == 0:
            return('', 204)

        total = len(risk_report_list)

        perPage = provider_args.get('perPage', max(total, 1))

        if isinstance(perPage, type(None)):
            perPage = max(total, 1)

        start_i = (page - 1) * (perPage - 1)
        end_i = min((page - 1) * perPage + perPage, total)

        pages = ceil((len(risk_report_list) / perPage))

        risk_report_list = risk_report_list[['id', 'score', 'paid']].iloc[start_i: end_i]
        risk_report_list.columns = ['id', 'score', 'paid']

        risk_report_list = risk_report_list.to_dict(orient='records')

        return {'timeStamp': init_time,
                'page': page,
                'pages': pages,
                'perPage': perPage,
                'total': total,
                'scores': risk_report_list}


@ns.route('/providers/<int:id>')
class ProviderIDCollection(Resource):

    @api.marshal_with(provider_risk_score)
    def get(self, id):
        """
        Returns risk score for a single provider.
        """
        risk_report_list = df_provider[['id', 'score', 'paid']]
        risk_report_list.columns = ['id', 'score', 'paid']

        if id in risk_report_list['id'].tolist():
            risk_report = risk_report_list[risk_report_list[
                'id'] == id].to_dict(orient='records')
            risk_report[0]['timeStamp'] = init_time
        else:
            abort(404, 'Provider ID not found', id=id, timeStamp=int(init_time))

        return risk_report
