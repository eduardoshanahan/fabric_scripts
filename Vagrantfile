Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "ubuntu/trusty64"

    config.vm.define :"fabric_scripts"

    config.vm.synced_folder "../", "/home/vagrant/code"

    config.vm.provider :virtualbox do |vb|
        vb.name = "fabric_scripts"
        vb.customize ["modifyvm", :id, "--memory", "512"]
    end

    config.vm.provision :fabric do |fabric|
        fabric.fabfile_path = "fabfile.py"
        fabric.tasks = []
    end
end