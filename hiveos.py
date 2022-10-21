from requests import get

#File with sensitive information needed for the script
import credentials


def hiveos_requests():

    #"Logging in" to the API so to say, with personal API key
    headers = { 
        "Content-Type": "application/json",
        "Authorization": "Bearer " + credentials.hiveos_key }

    #The base URL for the API, which we use as a base to navigate to different endpoints
    base_url = "https://api2.hiveos.farm/api/v2"

    #The endpoint for worker related data
    endpoint_workers = base_url + "/farms/{0}/workers/{1}".format(credentials.farm_id, credentials.worker_1_id)

    #Request for the said endpoint
    hiveos_api = get(endpoint_workers, headers=headers)

    #Extracting keys from the API
    hiveos_api_keys = hiveos_api.json()
    hiveos_api_keys.keys()

    #Worker 1 GPU 1 data
    worker_1_gpu_1_name = "Radeon RX 5700 MSI Mech: "
    worker_1_gpu_1_hashrate = hiveos_api_keys["gpu_stats"][0]["hash"]
    worker_1_gpu_1_power = hiveos_api_keys["gpu_stats"][0]["power"]
    worker_1_gpu_1_fan = hiveos_api_keys["gpu_stats"][0]["power"]
    worker_1_gpu_1_coretemp = hiveos_api_keys["gpu_stats"][0]["temp"]
    worker_1_gpu_1_memtemp = hiveos_api_keys["gpu_stats"][0]["memtemp"]

    worker_1_gpu_1_stats = [worker_1_gpu_1_name, worker_1_gpu_1_hashrate, worker_1_gpu_1_coretemp, worker_1_gpu_1_memtemp, worker_1_gpu_1_fan, worker_1_gpu_1_power] 

    #Worker 1 GPU 2 data
    worker_1_gpu_2_name = "Radeon RX 5700 Gigabyte OC: "
    worker_1_gpu_2_hashrate = hiveos_api_keys["gpu_stats"][1]["hash"]
    worker_1_gpu_2_power = hiveos_api_keys["gpu_stats"][1]["power"]
    worker_1_gpu_2_fan = hiveos_api_keys["gpu_stats"][1]["power"]
    worker_1_gpu_2_coretemp = hiveos_api_keys["gpu_stats"][1]["temp"]
    worker_1_gpu_2_memtemp = hiveos_api_keys["gpu_stats"][1]["memtemp"]

    worker_1_gpu_2_stats = [worker_1_gpu_2_name, worker_1_gpu_2_hashrate, worker_1_gpu_2_coretemp, worker_1_gpu_2_memtemp, worker_1_gpu_2_fan, worker_1_gpu_2_power]


    print(worker_1_gpu_1_stats, worker_1_gpu_2_stats)


if __name__ == '__main__':
    hiveos_requests()