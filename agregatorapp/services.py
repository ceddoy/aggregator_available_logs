import datetime

import apache_log_parser

from aggregator_available_logs.settings import PATH_ACCESS_LOG, MASK_REQUEST_LOGS, FILENAME_LOGS
from agregatorapp.models import Log


# def get_date_for_retrieve_logs():
#     return (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%m-%Y")


def load_logs():
    data_in_bd = []
    with open(f'{PATH_ACCESS_LOG}{FILENAME_LOGS}', 'r') as f:
        line_parser = apache_log_parser.make_parser(MASK_REQUEST_LOGS)
        for line_log in f.read().splitlines():
            if not line_log:
                continue
            line_parser_log = line_parser(line_log)
            data_in_bd.append(Log(ip_address=line_parser_log.get('remote_host'),
                                  remote_logname=line_parser_log.get('remote_logname'),
                                  remote_user=line_parser_log.get('remote_user'),
                                  date_add=line_parser_log.get('time_received_datetimeobj'),
                                  request_line=line_parser_log.get('request_first_line'),
                                  status=line_parser_log.get('status'),
                                  response_bytes=line_parser_log.get('response_bytes_clf'),
                                  header_referer=line_parser_log.get('request_header_referer'),
                                  header_user_agent=line_parser_log.get('request_header_user_agent')))

    return data_in_bd


def get_date_end_day(date):
    return (datetime.datetime(year=date.year, month=date.month, day=date.day) +
            datetime.timedelta(days=1) -
            datetime.timedelta(seconds=1))
