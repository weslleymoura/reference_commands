from flask_restplus import reqparse

provider_arguments = reqparse.RequestParser()
provider_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
provider_arguments.add_argument('perPage', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                help='Results per page {error_msg}')

provider_arguments.add_argument('scoreGT', type=int, required=False, default=0,
                                help='Filter by minimum score')
provider_arguments.add_argument('scoreLT', type=int, required=False, default=0,
                                help='Filter by maximum score')

provider_arguments.add_argument('paidGT', type=int, required=False, default=0,
                                help='Filter by minimum paid')
provider_arguments.add_argument('paidLT', type=int, required=False, default=0,
                                help='Filter by maximum paid')

provider_arguments.add_argument('sortBy', type=str, required=False,
                                default='score', choices=['score', 'paid'], help='Sort list by column')

provider_arguments.add_argument('sortDirection', type=str, required=False,
                                default='descending', choices=['descending', 'ascending'], help='Control if the list should be sorted in ascending order')

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('perPage', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                  help='Results per page {error_msg}')
