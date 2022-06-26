from mail_chimp import MailChimp
from google_sheet_2 import SpreadSheetsUploader


def return_campaign_information_dataframe(campaign_id):
    click_details_df = mc.click_details_to_pandas(campaign_id)
    camp_info_df = mc.campaign_information_to_pandas(campaign_id)

    return camp_info_df, click_details_df


def upload_spreadsheet(sheet_name, metric_length, dimension_length, df):
    gs_uploader.set_cell_index(sheet_name=sheet_name,
                               metric_length=metric_length,
                               dimension_length=dimension_length)

    gs_uploader.update_sheet(df.values.tolist())


if __name__ == "__main__":
    campaign_folder_id = "49808e33ee"
    SPREADSHEET_ID = "1AQO9OVE6IQFB3MZx2n6vt2nRoBJ-GuYN0Fi0FH-TioA"

    mc = MailChimp()
    gs_uploader = SpreadSheetsUploader(SPREADSHEET_ID)

    campaign_id_list = list()
    for campaign_raw in mc.find_campaign_id_by_folder_id(campaign_folder_id)['campaigns'][:2]:
        campaign_id = campaign_raw.get('id')
        information, click_details = return_campaign_information_dataframe(campaign_id)

        upload_spreadsheet("C-information", 5, 10, information)
        # upload_spreadsheet("C-click_detail", 4, 5, click_details)
