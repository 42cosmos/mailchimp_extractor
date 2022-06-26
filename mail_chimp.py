import os
import pandas as pd

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


class MailChimp:
    def __init__(self):
        self.api_token = os.environ['API_KEY']
        self._client = MailchimpMarketing.Client()
        self._client.set_config(self._api_token)

    def find_campaign_id_by_folder_id(self, folder_id):
        try:
            result = self._client.campaigns.list(count=1000, status='sent', folder_id=folder_id)
            return result

        except ApiClientError as error:
            print("Error: {}".format(error.text))

    def _get_campaign_details(self, campaign_id):
        try:
            response = self._client.reports.get_campaign_report(campaign_id)
            return response

        except ApiClientError as error:
            print("Error: {}".format(error.text))

    def _get_campaign_click_details(self, campaign_id):
        """Return a list of dictionaries containing reports. """
        try:
            response = self._client.reports.get_campaign_click_details(campaign_id, count=1000)
            return response

        except ApiClientError as error:
            print("Error: {}".format(error.text))

    def click_details_to_pandas(self, campaign_id):
        """Convert a Mailchimp click detail reports dictionary to a Pandas dataframe."""
        reports = self._get_campaign_click_details(campaign_id)
        result_list = list()

        if reports:
            for report in reports['urls_clicked']:
                temp_df = pd.json_normalize(report)
                result_list.append(temp_df)

            all_df = pd.concat(result_list)

            if all_df.columns[-1] == '_links':
                result = all_df[all_df.columns[:-1]]

        return result

    def campaign_information_to_pandas(self, campaign_id):
        """Convert a Mailchimp reports dictionary to a Pandas dataframe."""
        report = self._get_campaign_details(campaign_id)

        df = pd.DataFrame(
            columns=['campaign_id',
                     'send_time',
                     'campaign_title',
                     'subject_line',
                     'preview_text',
                     'emails_sent',
                     'abuse_reports',
                     'unsubscribed',
                     'hard_bounces',
                     'soft_bounces',
                     'clicks_total',
                     'unique_clicks',
                     'unique_subscriber_clicks',
                     'click_rate',
                     'opens_total'
                     'unique_opens',
                     'open_rate',
                     'last_open'
                     ])

        if report:
            row = {
                'campaign_id': report.get('id'),
                'send_time': report.get('send_time'),
                'campaign_title': report.get('campaign_title'),
                'subject_line': report.get('subject_line'),
                'preview_text': report.get('preview_text'),
                'emails_sent': report.get('emails_sent'),
                'abuse_reports': report.get('abuse_reports'),
                'unsubscribed': report.get('unsubscribed'),
                'hard_bounces': report.get('bounces').get('hard_bounces'),
                'soft_bounces': report.get('bounces').get('soft_bounces'),
                'clicks_total': report.get('clicks').get('clicks_total'),
                'unique_clicks': report.get('clicks').get('unique_clicks'),
                'unique_subscriber_clicks': report.get('clicks').get('unique_subscriber_clicks'),
                'click_rate': report.get('clicks').get('click_rate'),
                'opens_total': report.get('opens').get('opens_total'),
                'unique_opens': report.get('opens').get('unique_opens'),
                'open_rate': report.get('opens').get('open_rate'),
                'last_open': report.get('opens').get('last_open')

            }

            df = df.append(row, ignore_index='True')

        df = df.fillna(0)

        return df
