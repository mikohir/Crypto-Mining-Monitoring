from requests import get
from math import log, floor

#File with sensitive information needed for the script
import credentials

#Function for making pretty tables
from tabulate import tabulate

def hiveos_requests():

    #"Logging in" to the API so to say, with personal API key
    headers = { 
        "Content-Type": "application/json",
        "Authorization": "Bearer " + credentials.hiveos_key }

    #The base URL for the API, which we use as a base to navigate to different endpoints
    base_url = "https://api2.hiveos.farm/api/v2"

    #The endpoints for farm and worker(s) related data 
    endpoint_worker_1 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_1_id)
    endpoint_worker_2 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_2_id)
    endpoint_farm = base_url + "/farms/{0}".format(credentials.farm_id)

    #Request for the said endpoints
    hiveos_api_worker_1 = get(endpoint_worker_1, headers=headers)
    hiveos_api_worker_2 = get(endpoint_worker_2, headers=headers)
    hiveos_api_farm = get(endpoint_farm, headers=headers)

    #Extracting keys from the API
    hiveos_api_keys_worker_1 = hiveos_api_worker_1.json()
    hiveos_api_keys_worker_2 = hiveos_api_worker_2.json()
    hiveos_api_keys_farm = hiveos_api_farm.json()
   

    #Function for changing large numbers to Kilos, Megas etc.
    def hashrate_format(number):
        units = ['', ' MH', ' GH', ' TH', ' PH']
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k**magnitude, units[magnitude])



    #---------- WORKER 1 ----------#

    try:
        #Worker 1 GPU 0 data
        worker_1_gpu_0_name = "GPU 0: RX 5700 XT MSI Mech: "
        worker_1_gpu_0_hashrate = hiveos_api_keys_worker_1["gpu_stats"][0]["hash"]
        worker_1_gpu_0_power = str(hiveos_api_keys_worker_1["gpu_stats"][0]["power"]) + " W"
        worker_1_gpu_0_fan = str(hiveos_api_keys_worker_1["gpu_stats"][0]["fan"]) + " %"
        worker_1_gpu_0_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["temp"]) + " °C"
        worker_1_gpu_0_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"]) + " °C"

        worker_1_gpu_0_stats = [worker_1_gpu_0_name, hashrate_format(worker_1_gpu_0_hashrate), worker_1_gpu_0_coretemp, worker_1_gpu_0_memtemp, worker_1_gpu_0_fan, worker_1_gpu_0_power] 

        #Worker 1 GPU 1 data
        worker_1_gpu_1_name = "GPU 1: RX 5700 XT Gigabyte OC: "
        worker_1_gpu_1_hashrate = hiveos_api_keys_worker_1["gpu_stats"][1]["hash"]
        worker_1_gpu_1_power = str(hiveos_api_keys_worker_1["gpu_stats"][1]["power"]) + " W"
        worker_1_gpu_1_fan = str(hiveos_api_keys_worker_1["gpu_stats"][1]["fan"]) + " %"
        worker_1_gpu_1_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["temp"]) + " °C"
        worker_1_gpu_1_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"]) + " °C"

        worker_1_gpu_1_stats = [worker_1_gpu_1_name, hashrate_format(worker_1_gpu_1_hashrate), worker_1_gpu_1_coretemp, worker_1_gpu_1_memtemp, worker_1_gpu_1_fan, worker_1_gpu_1_power]

        #Worker 1 GPU 2 data
        worker_1_gpu_2_name = "GPU 2: RX 5700 XT Powercolor Red Dragon: "
        worker_1_gpu_2_hashrate = hiveos_api_keys_worker_1["gpu_stats"][2]["hash"]
        worker_1_gpu_2_power = str(hiveos_api_keys_worker_1["gpu_stats"][2]["power"]) + " W"
        worker_1_gpu_2_fan = str(hiveos_api_keys_worker_1["gpu_stats"][2]["fan"]) + " %"
        worker_1_gpu_2_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["temp"]) + " °C"
        worker_1_gpu_2_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"]) + " °C"

        worker_1_gpu_2_stats = [worker_1_gpu_2_name, hashrate_format(worker_1_gpu_2_hashrate), worker_1_gpu_2_coretemp, worker_1_gpu_2_memtemp, worker_1_gpu_2_fan, worker_1_gpu_2_power]

        #Worker 1 GPU 3 data
        worker_1_gpu_3_name = "GPU 3: RX 5700 XT ASUS Strix: "
        worker_1_gpu_3_hashrate = hiveos_api_keys_worker_1["gpu_stats"][3]["hash"]
        worker_1_gpu_3_power = str(hiveos_api_keys_worker_1["gpu_stats"][3]["power"]) + " W"
        worker_1_gpu_3_fan = str(hiveos_api_keys_worker_1["gpu_stats"][3]["fan"]) + " %"
        worker_1_gpu_3_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["temp"]) + " °C"
        worker_1_gpu_3_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"]) + " °C"

        worker_1_gpu_3_stats = [worker_1_gpu_3_name, hashrate_format(worker_1_gpu_3_hashrate), worker_1_gpu_3_coretemp, worker_1_gpu_3_memtemp, worker_1_gpu_3_fan, worker_1_gpu_3_power]

        #Create a list of all the different GPUs
        gpu_list = [worker_1_gpu_0_stats, worker_1_gpu_1_stats, worker_1_gpu_2_stats, worker_1_gpu_3_stats]

        #Worker 1
        with open("/var/www/html/hiveos_output_worker_1.txt", "w", encoding="utf-8") as hiveos_output_file_worker_1:
            hiveos_output_file_worker_1.write(tabulate(gpu_list, headers=["Model", "Hashrate", "Core Temp", "Mem Temp", "Fan", "Power"], tablefmt="fancy_grid"))
    
    #In case of an error
    except:
        with open("/var/www/html/hiveos_output_worker_1.txt", "w", encoding="utf-8") as hiveos_output_file_worker_1:
            hiveos_output_file_worker_1.write("+---------------+\n")
            hiveos_output_file_worker_1.write("| !!!OFFLINE!!! |\n")
            hiveos_output_file_worker_1.write("+---------------+")
       
       



    #---------- WORKER 2 ----------#
    
    try:    
        #Worker 2 GPU 0 data
        worker_2_gpu_0_name = "GPU 0: RTX 3070 Ti ASUS TUF: "
        worker_2_gpu_0_hashrate = hiveos_api_keys_worker_2["gpu_stats"][0]["hash"]
        worker_2_gpu_0_power = str(hiveos_api_keys_worker_2["gpu_stats"][0]["power"]) + " W"
        worker_2_gpu_0_fan = str(hiveos_api_keys_worker_2["gpu_stats"][0]["fan"]) + " %"
        worker_2_gpu_0_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["temp"]) + " °C"
        worker_2_gpu_0_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"]) + " °C"

        worker_2_gpu_0_stats = [worker_2_gpu_0_name, hashrate_format(worker_2_gpu_0_hashrate), worker_2_gpu_0_coretemp, worker_2_gpu_0_memtemp, worker_2_gpu_0_fan, worker_2_gpu_0_power]
            
        #Worker 2 GPU 1 data
        worker_2_gpu_1_name = "GPU 1: GTX 1660 Super MSI Ventus: "
        worker_2_gpu_1_hashrate = hiveos_api_keys_worker_2["gpu_stats"][1]["hash"]
        worker_2_gpu_1_power = str(hiveos_api_keys_worker_2["gpu_stats"][1]["power"]) + " W"
        worker_2_gpu_1_fan = str(hiveos_api_keys_worker_2["gpu_stats"][1]["fan"]) + " %"
        worker_2_gpu_1_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][1]["temp"]) + " °C"
        worker_2_gpu_1_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"]) + " °C"

            
        worker_2_gpu_1_stats = [worker_2_gpu_1_name, hashrate_format(worker_2_gpu_1_hashrate), worker_2_gpu_1_coretemp, worker_2_gpu_1_memtemp, worker_2_gpu_1_fan, worker_2_gpu_1_power] 

        #Worker 2 GPU 2 data
        worker_2_gpu_2_name = "GPU 2: RTX 3070 Ti ASUS TUF: "
        worker_2_gpu_2_hashrate = hiveos_api_keys_worker_2["gpu_stats"][2]["hash"]
        worker_2_gpu_2_power = str(hiveos_api_keys_worker_2["gpu_stats"][2]["power"]) + " W"
        worker_2_gpu_2_fan = str(hiveos_api_keys_worker_2["gpu_stats"][2]["fan"]) + " %"
        worker_2_gpu_2_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][2]["temp"]) + " °C"
        worker_2_gpu_2_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"]) + " °C"

        worker_2_gpu_2_stats = [worker_2_gpu_2_name, hashrate_format(worker_2_gpu_2_hashrate), worker_2_gpu_2_coretemp, worker_2_gpu_2_memtemp, worker_2_gpu_2_fan, worker_2_gpu_2_power]

        #Worker 2 GPU 3 data
        worker_2_gpu_3_name = "GPU 3: GTX 1660 Super MSI Gaming X: "
        worker_2_gpu_3_hashrate = hiveos_api_keys_worker_2["gpu_stats"][3]["hash"]
        worker_2_gpu_3_power = str(hiveos_api_keys_worker_2["gpu_stats"][3]["power"]) + " W"
        worker_2_gpu_3_fan = str(hiveos_api_keys_worker_2["gpu_stats"][3]["fan"]) + " %"
        worker_2_gpu_3_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][3]["temp"]) + " °C"
        worker_2_gpu_3_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"]) + " °C"

        worker_2_gpu_3_stats = [worker_2_gpu_3_name, hashrate_format(worker_2_gpu_3_hashrate), worker_2_gpu_3_coretemp, worker_2_gpu_3_memtemp, worker_2_gpu_3_fan, worker_2_gpu_3_power]

        #Worker 2 GPU 4 data
        worker_2_gpu_4_name = "GPU 4: GTX 1660 Super HP OEM: "
        worker_2_gpu_4_hashrate = hiveos_api_keys_worker_2["gpu_stats"][4]["hash"]
        worker_2_gpu_4_power = str(hiveos_api_keys_worker_2["gpu_stats"][4]["power"]) + " W"
        worker_2_gpu_4_fan = str(hiveos_api_keys_worker_2["gpu_stats"][4]["fan"]) + " %"
        worker_2_gpu_4_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][4]["temp"]) + " °C"
        worker_2_gpu_4_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"]) + " °C"

        worker_2_gpu_4_stats = [worker_2_gpu_4_name, hashrate_format(worker_2_gpu_4_hashrate), worker_2_gpu_4_coretemp, worker_2_gpu_4_memtemp, worker_2_gpu_4_fan, worker_2_gpu_4_power]

        #Worker 2 GPU 5 data
        worker_2_gpu_5_name = "GPU 5: GTX 1660 Super ASUS TUF: "
        worker_2_gpu_5_hashrate = hiveos_api_keys_worker_2["gpu_stats"][5]["hash"]
        worker_2_gpu_5_power = str(hiveos_api_keys_worker_2["gpu_stats"][5]["power"]) + " W"
        worker_2_gpu_5_fan = str(hiveos_api_keys_worker_2["gpu_stats"][5]["fan"]) + " %"
        worker_2_gpu_5_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][5]["temp"]) + " °C"
        worker_2_gpu_5_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"]) + " °C"

        worker_2_gpu_5_stats = [worker_2_gpu_5_name, hashrate_format(worker_2_gpu_5_hashrate), worker_2_gpu_5_coretemp, worker_2_gpu_5_memtemp, worker_2_gpu_5_fan, worker_2_gpu_5_power]

        #Worker 2 GPU 6 data
        worker_2_gpu_6_name = "GPU 6: GTX 1660 Super ASUS Phoenix: "
        worker_2_gpu_6_hashrate = hiveos_api_keys_worker_2["gpu_stats"][6]["hash"]
        worker_2_gpu_6_power = str(hiveos_api_keys_worker_2["gpu_stats"][6]["power"]) + " W"
        worker_2_gpu_6_fan = str(hiveos_api_keys_worker_2["gpu_stats"][6]["fan"]) + " %"
        worker_2_gpu_6_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][6]["temp"]) + " °C"
        worker_2_gpu_6_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"]) + " °C"

        worker_2_gpu_6_stats = [worker_2_gpu_6_name, hashrate_format(worker_2_gpu_6_hashrate), worker_2_gpu_6_coretemp, worker_2_gpu_6_memtemp, worker_2_gpu_6_fan, worker_2_gpu_6_power]
            
        #Worker 2 GPU 7 data
        worker_2_gpu_7_name = "GPU 7: GTX 1660 Super ASUS TUF: "
        worker_2_gpu_7_hashrate = hiveos_api_keys_worker_2["gpu_stats"][7]["hash"]
        worker_2_gpu_7_power = str(hiveos_api_keys_worker_2["gpu_stats"][7]["power"]) + " W"
        worker_2_gpu_7_fan = str(hiveos_api_keys_worker_2["gpu_stats"][7]["fan"]) + " %"
        worker_2_gpu_7_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][7]["temp"]) + " °C"
        worker_2_gpu_7_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"]) + " °C"

        worker_2_gpu_7_stats = [worker_2_gpu_7_name, hashrate_format(worker_2_gpu_7_hashrate), worker_2_gpu_7_coretemp, worker_2_gpu_7_memtemp, worker_2_gpu_7_fan, worker_2_gpu_7_power]
    
        #Create a list of all the different GPUs
        gpu_list_2 = [worker_2_gpu_0_stats, worker_2_gpu_1_stats, worker_2_gpu_2_stats, worker_2_gpu_3_stats, worker_2_gpu_4_stats, worker_2_gpu_5_stats, worker_2_gpu_6_stats, worker_2_gpu_7_stats]

        #Worker 2
        with open("/var/www/html/hiveos_output_worker_2.txt", "w", encoding="utf-8") as hiveos_output_file_worker_2:
            hiveos_output_file_worker_2.write(tabulate(gpu_list_2, headers=["Model", "Hashrate", "Core Temp", "Mem Temp", "Fan", "Power"], tablefmt="fancy_grid"))
    
    #In case of an error
    except:
        with open("/var/www/html/hiveos_output_worker_2.txt", "w", encoding="utf-8") as hiveos_output_file_worker_2:
            hiveos_output_file_worker_2.write("+---------------+\n")
            hiveos_output_file_worker_2.write("| !!!OFFLINE!!! |\n")
            hiveos_output_file_worker_2.write("+---------------+")
        
        


    #---------- Farm Total Stats ----------#
    
    total_gpus = str(hiveos_api_keys_farm["stats"]["gpus_online"])
    total_gpus_offline = str(hiveos_api_keys_farm["stats"]["gpus_offline"])
    total_hash = str(hashrate_format(hiveos_api_keys_farm["hashrates"][0]["hashrate"]))
    total_power = str(hiveos_api_keys_farm["stats"]["power_draw"]) + " W"
    
    with open("/var/www/html/hiveos_output_total.txt", "w", encoding="utf-8") as hiveos_output_file_total:
        
        if total_gpus_offline == str(0):
            hiveos_output_file_total.write(f"GPUs online: {total_gpus}\n")
            hiveos_output_file_total.write(f"GPUs offline: {total_gpus_offline}\n")
            hiveos_output_file_total.write(f"Hashrate: {total_hash}\n")
            hiveos_output_file_total.write(f"Power: {total_power}")
            
        elif total_gpus_offline >= str(0):
            hiveos_output_file_total.write(f"GPUs online: {total_gpus}\n")
            hiveos_output_file_total.write(f"GPUs offline: {total_gpus_offline}  <-- Something is Wrong!!!\n")
            hiveos_output_file_total.write(f"Hashrate: {total_hash}\n")
            hiveos_output_file_total.write(f"Power: {total_power}")
        
        
        
if __name__ == '__main__':
    hiveos_requests()
