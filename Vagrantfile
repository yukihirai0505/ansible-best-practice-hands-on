Vagrant.configure("2") do |config|

  config.vm.box = "bento/centos-6.7"
  config.ssh.insert_key = false

  config.vm.define "host" do |node|
    node.vm.box = "bento/centos-6.7"
    node.vm.hostname = "host"
    node.vm.network :private_network, ip: "192.168.43.51"
    node.vm.synced_folder "./httpdStore", "/var/www/html/"
  end

  config.vm.define "stage" do |node|
    node.vm.box = "bento/centos-6.7"
    node.vm.hostname = "stage"
    node.vm.network :private_network, ip: "192.168.43.52"
  end

  config.vm.define "production" do |node|
    node.vm.box = "bento/centos-6.7"
    node.vm.hostname = "production"
    node.vm.network :private_network, ip: "192.168.43.53"
  end
end
