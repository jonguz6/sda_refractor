from abc import ABCMeta, abstractmethod


class NoReportsException(Exception):
    pass


class AbstractReportSender(metaclass=ABCMeta):
    @abstractmethod
    def send(self, report):
        raise NotImplementedError


class EmailReportSender(AbstractReportSender):
    def send(self, report):
        pass


class SlackReportSender(AbstractReportSender):
    def send(self, report):
        pass


class AbstractReportBuilder(metaclass=ABCMeta):
    @abstractmethod
    def create_reports(self):
        pass


class MonthlyReportBuilder(AbstractReportBuilder):
    def create_reports(self):
        pass


class Reporter:
    def __init__(
        self,
        report_sender: AbstractReportSender,
        report_builder: AbstractReportBuilder
    ):
        self._report_sender = report_sender
        self._report_builder = report_builder

    def send_reports(self):
        reports = self._report_builder.create_reports()
        if not reports:
            raise NoReportsException
        for report in reports:
            self._report_sender.send(report)


def main():
    report_builder = MonthlyReportBuilder()
    email_sender = EmailReportSender()
    email_reporter = Reporter(email_sender, report_builder)
    email_reporter.send_reports()
    slack_sender = SlackReportSender()
    slack_reporter = Reporter(slack_sender, report_builder)
    slack_reporter.send_reports()

if __name__ == '__main__':
    main()