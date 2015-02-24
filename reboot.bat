call gcloud compute instances add-metadata core1 --zone europe-west1-d --metadata-from-file=user-data=cloud-config.yaml
call gcloud compute instances add-metadata core2 --zone europe-west1-d --metadata-from-file=user-data=cloud-config.yaml
call gcloud compute instances add-metadata core3 --zone europe-west1-d --metadata-from-file=user-data=cloud-config.yaml