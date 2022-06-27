MailChimp Extractor by Directory ID
---

Download mailchimp campaign data by campaign directory (folder) id

Requirements
---
Python 3.6+

### Installation 
#### pip install
```python
pip install ~~
```

### Endpoints
|Method| requirement        | return       |
|:---|:-------------------|:-------------|
|`find_campaign_id_by_folder_id`| campaign_folder_id | [id, titile] |
|`campaign_information_to_pandas`| campaign_id        | DataFrame    |
|`click_details_to_pandas`|campaign_id| DataFrame    |

### Usage
you must make `.env` file with your mailchimp api key and server

```python
from extract_mailchimp import MailChimp


def return_campaign_information_dataframe(campaign_id):
    click_details_df = mc.click_details_to_pandas(campaign_id)
    camp_info_df = mc.campaign_information_to_pandas(campaign_id)

    return camp_info_df, click_details_df


if __name__ == "__main__":
    campaign_folder_id = {campaign_folder_id}
    mc = MailChimp()

    campaign_id_list = list()
    for campaign_raw in mc.find_campaign_id_by_folder_id(campaign_folder_id)['campaigns'][:2]:
        campaign_id = campaign_raw.get('id')
        information, click_details = return_campaign_information_dataframe(campaign_id)
        print(information.shape, click_details.shape)

```