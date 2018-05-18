import logging.config

from flask import Flask, Blueprint
from da_rest_api import settings
from da_rest_api.api.risk_report.endpoints.risk_report import ns as risk_report_posts_namespace
from da_rest_api.api.restplus import api
import gc

application = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    #    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(risk_report_posts_namespace)
    flask_app.register_blueprint(blueprint)


@application.teardown_request
def teardown_request(exception):
    gc.collect()


def main():
    initialize_app(application)
    # log.info(
    #    '>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    application.run(host='0.0.0.0', port=8888, debug=settings.FLASK_DEBUG)
    # app.run()

if __name__ == "__main__":
    main()
