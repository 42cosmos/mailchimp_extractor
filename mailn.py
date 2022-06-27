from extract_mailchimp import MailChimp


def return_campaign_information_dataframe(campaign_id):
    click_details_df = mc.click_details_to_pandas(campaign_id)
    camp_info_df = mc.campaign_information_to_pandas(campaign_id)

    return camp_info_df, click_details_df


if __name__ == "__main__":
    campaign_folder_id = "49808e33ee"
    mc = MailChimp()
    print(mc.get_campaign_id_by_folder_id(campaign_folder_id))
    #
    # campaign_id_list = list()
    # for campaign_raw in mc.find_campaign_id_by_folder_id(campaign_folder_id)['campaigns']:
    #     campaign_id = campaign_raw.get('id')
    #     campaign_title = campaign_raw.get('settings').get('title')
    #     print([campaign_id, campaign_title])
    #     break
        # information, click_details = return_campaign_information_dataframe(campaign_id)
        # print(information.shape, click_details.shape)
