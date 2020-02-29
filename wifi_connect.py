import zumidashboard.scripts as scripts
#add your info in here then run this program
network_name = ""
network_password = ""

scripts.get_ssid_list()
scripts.kill_supplicant()
scripts.add_wifi(network_name,network_password)
scripts.check_wifi()
