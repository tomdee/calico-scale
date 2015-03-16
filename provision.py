# Script the slow bits (the docker pull mainly) so it can happen in parallel - put in cloud-config and add command to run it on startup.

from subprocess import call
def run_command(host, command):
    call('gcloud compute ssh --zone=europe-west1-d core@%s --command "%s"' % (host, command), shell=True)

# print "Getting calilcoctl"
# run_command("core1", "if [[ ! -e calicoctl ]]; then wget https://github.com/Metaswitch/calico-docker/releases/download/v0.0.6/calicoctl;chmod +x calicoctl; fi")
# run_command("core1", "if [[ ! -e calicoctl ]]; then wget https://github.com/Metaswitch/calico-docker/releases/download/v0.0.6/calicoctl;chmod +x calicoctl; fi")
#
# print "Pull docker images"
# run_command("core1", "docker pull calico/node:v0.0.6")
# run_command("core1", "docker pull calico/master:v0.0.6")
# run_command("core2", "docker pull calico/node:v0.0.6")
#
# print "Running calico"
# run_command("core1", "sudo ./calicoctl master --ip=$(hostname -i)")
# run_command("core1", "sudo ./calicoctl node --ip=$(hostname -i)")
# run_command("core2", "sudo ./calicoctl master --ip=$(hostname -i)")

NUM_NODES = 2

for node_number in xrange(1,NUM_NODES+1):
    print "Starting node %s" % node_number
    # call("gcloud compute instances create core%s --image https://www.googleapis.com/compute/v1/projects/coreos-cloud/global/images/coreos-alpha-598-0-0-v20150219 --machine-type g1-small --metadata-from-file user-data=cloud-config.yaml --can-ip-forward" % node_number, shell=True)
    # call("gcloud compute routes create ip-192-168-%s-0 --next-hop-instance core%s --next-hop-instance-zone europe-west1-d --destination-range 192.168.%s.0/24" % (node_number, node_number, node_number), shell=True)
    run_command("core%s" % node_number, "sudo ip addr add $(hostname -i) peer 10.240.0.1 dev ens4v1")
    run_command("core%s" % node_number, "sudo ip route add unreachable 192.168.0.0/16")

call("gcloud compute instances list")