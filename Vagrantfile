Vagrant.configure("2") do |config|
    config.vm.define "centos7" do |centos7|
        centos7.vm.box = "boxen/centos-7"
        centos7.vm.hostname = "centos7"
        centos7.vm.network "private_network", ip: "192.168.14.12"
        centos7.vm.provision "shell" do |shell|
            shell.inline = <<-SHELL
                set -euxo pipefail

                yum install -y gcc rpm-build
            SHELL
        end
        centos7.vm.synced_folder ".", "/vagrant"
    end
end
