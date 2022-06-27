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
|`get_campaign_raw_data_by_folder_id`| {campaign_folder_id} | JSON         |
|`get_campaign_id_by_folder_id`| {campaign_folder_id} | [id, titile] |
|`campaign_information_to_pandas`| {campaign_id}        | DataFrame    |
|`click_details_to_pandas`|{campaign_id}| DataFrame    |

### Usage
you must make `.env` file with your mailchimp api key and server

```python
from extract_mailchimp import MailChimp

if __name__ == "__main__":
    campaign_folder_id = {campaign_folder_id}
    mc = MailChimp()
    print(mc.get_campaign_id_by_folder_id(campaign_folder_id))
    # [['{campaign_id}', '{campaign_title}']]
```