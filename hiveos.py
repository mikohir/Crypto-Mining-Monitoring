from requests import get
from math import log, floor

#File with sensitive information needed for the script
import credentials


def hiveos_requests():

    #"Logging in" to the API so to say, with personal API key
    headers = { 
        "Content-Type": "application/json",
        "Authorization": "Bearer " + credentials.hiveos_key }

    #The base URL for the API, which we use as a base to navigate to different endpoints
    base_url = "https://api2.hiveos.farm/api/v2"

    #The endpoints for worker related data
    endpoint_worker_1 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_1_id)
    endpoint_worker_2 = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_2_id)

    #Request for the said endpoints
    hiveos_api_worker_1 = get(endpoint_worker_1, headers=headers)
    hiveos_api_worker_2 = get(endpoint_worker_2, headers=headers)

    #Extracting keys from the API
    hiveos_api_keys_worker_1 = hiveos_api_worker_1.json()
    hiveos_api_keys_worker_1.keys()

    hiveos_api_keys_worker_2 = hiveos_api_worker_2.json()
    hiveos_api_keys_worker_2.keys()

    #Function for changing large numbers to Kilos, Megas etc.
    def hashrate_format(number):
        units = ['', ' MH', ' GH', ' TH', ' PH']
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k**magnitude, units[magnitude])

    def worker_1():

        #Worker 1 GPU 0 data
        worker_1_gpu_0_name = "GPU 0: Radeon RX 5700 MSI Mech: "
        worker_1_gpu_0_hashrate = hiveos_api_keys_worker_1["gpu_stats"][0]["hash"]
        worker_1_gpu_0_power = str(hiveos_api_keys_worker_1["gpu_stats"][0]["power"]) + " W"
        worker_1_gpu_0_fan = str(hiveos_api_keys_worker_1["gpu_stats"][0]["fan"]) + " %"
        worker_1_gpu_0_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["temp"]) + " °C"
        worker_1_gpu_0_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"]) + " °C"

        worker_1_gpu_0_stats = [worker_1_gpu_0_name, hashrate_format(worker_1_gpu_0_hashrate), worker_1_gpu_0_coretemp, worker_1_gpu_0_memtemp, worker_1_gpu_0_fan, worker_1_gpu_0_power] 

        #Worker 1 GPU 1 data
        worker_1_gpu_1_name = "GPU 1: Radeon RX 5700 Gigabyte OC: "
        worker_1_gpu_1_hashrate = hiveos_api_keys_worker_1["gpu_stats"][1]["hash"]
        worker_1_gpu_1_power = str(hiveos_api_keys_worker_1["gpu_stats"][1]["power"]) + " W"
        worker_1_gpu_1_fan = str(hiveos_api_keys_worker_1["gpu_stats"][1]["fan"]) + " %"
        worker_1_gpu_1_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["temp"]) + " °C"
        worker_1_gpu_1_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"]) + " °C"

        worker_1_gpu_1_stats = [worker_1_gpu_1_name, hashrate_format(worker_1_gpu_1_hashrate), worker_1_gpu_1_coretemp, worker_1_gpu_1_memtemp, worker_1_gpu_1_fan, worker_1_gpu_1_power]

        #Worker 1 GPU 2 data
        worker_1_gpu_2_name = "GPU 2: Radeon RX 5700 Powercolor Red Dragon: "
        worker_1_gpu_2_hashrate = hiveos_api_keys_worker_1["gpu_stats"][2]["hash"]
        worker_1_gpu_2_power = str(hiveos_api_keys_worker_1["gpu_stats"][2]["power"]) + " W"
        worker_1_gpu_2_fan = str(hiveos_api_keys_worker_1["gpu_stats"][2]["fan"]) + " %"
        worker_1_gpu_2_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["temp"]) + " °C"
        worker_1_gpu_2_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"]) + " °C"

        worker_1_gpu_2_stats = [worker_1_gpu_2_name, hashrate_format(worker_1_gpu_2_hashrate), worker_1_gpu_2_coretemp, worker_1_gpu_2_memtemp, worker_1_gpu_2_fan, worker_1_gpu_2_power]

        #Worker 1 GPU 3 data
        worker_1_gpu_3_name = "GPU 3: Radeon RX 5700 ASUS Strix: "
        worker_1_gpu_3_hashrate = hiveos_api_keys_worker_1["gpu_stats"][3]["hash"]
        worker_1_gpu_3_power = str(hiveos_api_keys_worker_1["gpu_stats"][3]["power"]) + " W"
        worker_1_gpu_3_fan = str(hiveos_api_keys_worker_1["gpu_stats"][3]["fan"]) + " %"
        worker_1_gpu_3_coretemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["temp"]) + " °C"
        worker_1_gpu_3_memtemp = str(hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"]) + " °C"

        worker_1_gpu_3_stats = [worker_1_gpu_3_name, hashrate_format(worker_1_gpu_3_hashrate), worker_1_gpu_3_coretemp, worker_1_gpu_3_memtemp, worker_1_gpu_3_fan, worker_1_gpu_3_power]

        #Create a list of all the different GPUs
        gpu_list = [worker_1_gpu_0_stats, worker_1_gpu_1_stats, worker_1_gpu_2_stats, worker_1_gpu_3_stats]

        #Print out the GPU list in seperate lines
        print("Worker 1:")
        print(*gpu_list, sep="\n")

    worker_1()

    def worker_2():
        
        #Worker 2 GPU 0 data
        worker_2_gpu_0_name = "GPU 0: RTX 3070 Ti ASUS TUF: "
        worker_2_gpu_0_hashrate = hiveos_api_keys_worker_2["gpu_stats"][0]["hash"]
        worker_2_gpu_0_power = str(hiveos_api_keys_worker_2["gpu_stats"][0]["power"]) + " W"
        worker_2_gpu_0_fan = str(hiveos_api_keys_worker_2["gpu_stats"][0]["fan"]) + " %"
        worker_2_gpu_0_coretemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["temp"]) + " °C"
        worker_2_gpu_0_memtemp = str(hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"]) + " °C"

        worker_2_gpu_0_stats = [worker_2_gpu_0_name, hashrate_format(worker_2_gpu_0_hashrate), worker_2_gpu_0_coretemp, worker_2_gpu_0_memtemp, worker_2_gpu_0_fan, worker_2_gpu_0_power] 

        gpu_list_2 = [worker_2_gpu_0_stats]

        #Print out the GPU list in seperate lines
        print("Worker 2:")
        print(*gpu_list_2, sep="\n")

    worker_2()

if __name__ == '__main__':
    hiveos_requests()