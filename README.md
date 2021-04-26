# Keap Get Campaign XML
This is a Keap internal tool for Data Services to get the xml of a Keap Campaign.

#### Download the xml from the FileBox.
```sql
# To Get FileBoxId
SELECT FileBoxId FROM Funnel WHERE Id=213;

# Update FileBox so we can get the xml file via API
Update FileBox SET CanDownload=1, FileBoxType=1 Where Id =1234;
```
#### Get the App XMLRPC Key for Python.
Update the appname, api_key, and filebox_id (int)

#### --NOTE BEFORE RUNNING--
Make sure at the bottom get_file() is uncommented and push_file() is commented out. You will first get_file() and after making changes to xml you will comment out get_file() and uncomment push_file().
