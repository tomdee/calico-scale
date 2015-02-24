call gcloud compute instances create core1 core2 core3 --image https://www.googleapis.com/compute/v1/projects/coreos-cloud/global/images/coreos-alpha-598-0-0-v20150219 --machine-type g1-small --metadata-from-file user-data=cloud-config.yaml --can-ip-forward
call gcloud compute firewall-rules create "any" --allow tcp:1-65535 --network "default" --source-ranges "192.168.0.0/16"
