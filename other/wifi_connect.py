import zumidashboard.scripts as scripts
#add your info in here then run this program
network_name = ""
network_password = ""
# network_name = "my_network"
# network_password = "my_password"

scripts.get_ssid_list()
scripts.kill_supplicant()
scripts.add_wifi(network_name,network_password,isHiddenNetwork=False)
scripts.check_wifi()