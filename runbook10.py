from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netmiko_config(task):
    task.run(task=netmiko_send_config, config_file="./netmikoconfig.txt")

results = nr.run(task=netmiko_config)
print_result(results)