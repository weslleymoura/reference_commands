import logging.config

from flask import Flask, Blueprint
from da_rest_api import settings
from da_rest_api.api.risk_report.endpoints.risk_report import ns as risk_report_posts_namespace
from da_rest_api.api.restplus import api

application = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(risk_report_posts_namespace)
application.register_blueprint(blueprint)

application.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
application.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
application.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


if __name__ == "__main__":
    application.run()
