# Yet-another-hentai-site
A hentai site started because of the (supposed) shutdown of HH.

## Using the API:
All the urls connected with the api start with:
> **_/api/_**...

Explination of all the possible urls:
* api/
    API returns all of the info in the database

* api/series/**name or id of the series here**:
    API returns all of the info about given series as well as info about videos connected with it

* api/series/**name or id of the series here**/**episode**:
    API returns all the info about a given episode of the given series

* api/video/**id of the video**:
    API returns all the info about the video with the given id

* api/tag/**tags** **_or_** api/tag/any/**tags**:
    Return all the videos that contain at least one of the tags given. **Tags must be provided by their ids and if there are many of them, they need to be separated with a period ( . ), for example: 3 _or_ 4.10.25**

* api/tag/all/**tags**:
    Return all the videos that contain all of the tags given. **Tags must be provided by their ids and if there are many of them, they need to be separated with a period ( . ), for example: 3 _or_ 4.10.25**