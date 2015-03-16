call gcloud compute instances delete -q core
call gcloud compute instances create core --image https://www.googleapis.com/compute/v1/projects/coreos-cloud/global/images/coreos-alpha-598-0-0-v20150219 --machine-type g1-small --metadata-from-file user-data=cloud-config.yaml --can-ip-forward
