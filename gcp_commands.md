## Most used GCP commands

```
# list all GCloud projects
gcloud projects list

# set GCloud project
gcloud config set project [PROJECT-ID]

# connect to VM
gcloud compute ssh --zone=[INSTANCE-ZONE] [INSTANCE-NAME]

# copy file to local machine (examples)
gcloud compute scp instance-1:/home/databases/complete_db.txt D:\data

# copy file from local machine
gcloud compute scp C:\Users\yabra\2015-02.txt instance-1:/home/yabran_muvdi/2015-02-txt

# copy files to BUCKET
gsutil cp C:\Users\yabra\2015-02.nml.gz gs://dow-jones-data/zipped_files/
```