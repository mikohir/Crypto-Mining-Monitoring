from requests import get
from math import log, floor

#File with sensitive information needed for the script
import credentials

#Function for making pretty tables
from tabulate import tabulate



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

#Functions to change HTML content color based on given values

def core_color(x):
    red = f"""
    "<span style="color: red"{x}</span>
    """
    orange = f"""
    <span style="color: rgba(255, 145, 1);">{x}</span>
    """
    green = f"""
    <span style="color: green;">{x}</span>
    """
    
    if x >= 60:
        output = red
    elif x < 58:
        output = green
    else:
        output = orange

    return output

def mem_color(x):
    red = f"""
    "<span style="color: red"{x}</span>
    """
    orange = f"""
    <span style="color: rgba(255, 145, 1);">{x}</span>
    """
    green = f"""
    <span style="color: green;">{x}</span>
    """
    
    if x >= 86:
        output = red
    elif x < 80:
        output = green
    else:
        output = orange

    return output



#---------- WORKER 1 ----------#

try:
    #Worker 1 GPU 0 data"
    worker_1_gpu_0_name = "RX 5700 XT MSI"
    worker_1_gpu_0_index = "0:"
    worker_1_gpu_0_hashrate = hiveos_api_keys_worker_1["gpu_stats"][0]["hash"]
    worker_1_gpu_0_power = hiveos_api_keys_worker_1["gpu_stats"][0]["power"]
    worker_1_gpu_0_fan = hiveos_api_keys_worker_1["gpu_stats"][0]["fan"]
    worker_1_gpu_0_coretemp = hiveos_api_keys_worker_1["gpu_stats"][0]["temp"]
    worker_1_gpu_0_memtemp = hiveos_api_keys_worker_1["gpu_stats"][0]["memtemp"]
    

    #Worker 1 GPU 1 data
    worker_1_gpu_1_name = "RX 5700 XT Gigabyte"
    worker_1_gpu_1_index = "1:"
    worker_1_gpu_1_hashrate = hiveos_api_keys_worker_1["gpu_stats"][1]["hash"]
    worker_1_gpu_1_power = hiveos_api_keys_worker_1["gpu_stats"][1]["power"]
    worker_1_gpu_1_fan = hiveos_api_keys_worker_1["gpu_stats"][1]["fan"]
    worker_1_gpu_1_coretemp = hiveos_api_keys_worker_1["gpu_stats"][1]["temp"]   
    worker_1_gpu_1_memtemp = hiveos_api_keys_worker_1["gpu_stats"][1]["memtemp"]


    #Worker 1 GPU 2 data
    worker_1_gpu_2_name = "RX 5700 XT PowerColor"
    worker_1_gpu_2_index = "2:"
    worker_1_gpu_2_hashrate = hiveos_api_keys_worker_1["gpu_stats"][2]["hash"]
    worker_1_gpu_2_power = hiveos_api_keys_worker_1["gpu_stats"][2]["power"]
    worker_1_gpu_2_fan = hiveos_api_keys_worker_1["gpu_stats"][2]["fan"]
    worker_1_gpu_2_coretemp = hiveos_api_keys_worker_1["gpu_stats"][2]["temp"]
    worker_1_gpu_2_memtemp = hiveos_api_keys_worker_1["gpu_stats"][2]["memtemp"]


    #Worker 1 GPU 3 data
    worker_1_gpu_3_name = "RX 5700 XT ASUS"
    worker_1_gpu_3_index = "3:"
    worker_1_gpu_3_hashrate = hiveos_api_keys_worker_1["gpu_stats"][3]["hash"]
    worker_1_gpu_3_power = hiveos_api_keys_worker_1["gpu_stats"][3]["power"]
    worker_1_gpu_3_fan = hiveos_api_keys_worker_1["gpu_stats"][3]["fan"]
    worker_1_gpu_3_coretemp = hiveos_api_keys_worker_1["gpu_stats"][3]["temp"]
    worker_1_gpu_3_memtemp = hiveos_api_keys_worker_1["gpu_stats"][3]["memtemp"]
    

    #Create a HTML table from all worker GPUs
    worker_1_table = f"""
        <table class="demTable">
            <thead>
                <tr>
                    <th><img src="./Icons/graphics-card.png"/></th>
				    <th>Hashrate</th>
				    <th>Core Temp (°C)</th>
				    <th>Mem Temp (°C)</th>
				    <th>Fan (%)</th>
				    <th>Power (W)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align: left;">{worker_1_gpu_0_name}</td>
                    <td>{hashrate_format(worker_1_gpu_0_hashrate)}</td>
                    <td>{core_color(worker_1_gpu_0_coretemp)}</td>
                    <td>{mem_color(worker_1_gpu_0_memtemp)}</td>
                    <td>{worker_1_gpu_0_fan}</td>
                    <td>{worker_1_gpu_0_power}</td>
                </tr>
                <tr>
                    <td style="text-align: left;">{worker_1_gpu_1_name}</td>
                    <td>{hashrate_format(worker_1_gpu_1_hashrate)}</td>
                    <td>{core_color(worker_1_gpu_1_coretemp)}</td>
                    <td>{mem_color(worker_1_gpu_1_memtemp)}</td>
                    <td>{worker_1_gpu_1_fan}</td>
                    <td>{worker_1_gpu_1_power}</td>
                </tr>
                <tr>
                    <td style="text-align: left;">{worker_1_gpu_2_name}</td>
                    <td>{hashrate_format(worker_1_gpu_2_hashrate)}</td>
                    <td>{core_color(worker_1_gpu_2_coretemp)}</td>
                    <td>{mem_color(worker_1_gpu_2_memtemp)}</td>
                    <td>{worker_1_gpu_2_fan}</td>
                    <td>{worker_1_gpu_2_power}</td>
                </tr>
                <tr>
                    <td style="text-align: left;">{worker_1_gpu_3_name}</td>
                    <td>{hashrate_format(worker_1_gpu_3_hashrate)}</td>
                    <td>{core_color(worker_1_gpu_3_coretemp)}</td>
                    <td>{mem_color(worker_1_gpu_3_memtemp)}</td>
                    <td>{worker_1_gpu_3_fan}</td>
                    <td>{worker_1_gpu_3_power}</td>
                </tr>
            </tbody>
        </table>
        """ 

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(f"{worker_1_table}")
    
#In case of an error
    
except IndexError:
    worker_1_table = f"""
    <div>
        <a style="color: red;">Index error. Please Check script.<br><br></a>
    <div>
    """
        
except KeyError or Exception:
    worker_1_table = f"""
    <div>
        <h1 style="color: red;">OFFLINE!<br><br></h1>
    <div>
    """
    
    
#---------- WORKER 2 ----------#

try:    
    #Worker 2 GPU 0 data
    worker_2_gpu_0_name = "RTX 3070 Ti ASUS"
    worker_2_gpu_0_index = "0:"
    worker_2_gpu_0_hashrate = hiveos_api_keys_worker_2["gpu_stats"][0]["hash"]
    worker_2_gpu_0_power = hiveos_api_keys_worker_2["gpu_stats"][0]["power"]
    worker_2_gpu_0_fan = hiveos_api_keys_worker_2["gpu_stats"][0]["fan"]
    worker_2_gpu_0_coretemp = hiveos_api_keys_worker_2["gpu_stats"][0]["temp"]       
    worker_2_gpu_0_memtemp = hiveos_api_keys_worker_2["gpu_stats"][0]["memtemp"]
     

    #Worker 2 GPU 1 data
    worker_2_gpu_1_name = "GTX 1660 Super MSI"
    worker_2_gpu_1_index = "1:"
    worker_2_gpu_1_hashrate = hiveos_api_keys_worker_2["gpu_stats"][1]["hash"]
    worker_2_gpu_1_power = hiveos_api_keys_worker_2["gpu_stats"][1]["power"]
    worker_2_gpu_1_fan = hiveos_api_keys_worker_2["gpu_stats"][1]["fan"]
    worker_2_gpu_1_coretemp = hiveos_api_keys_worker_2["gpu_stats"][1]["temp"]                
    worker_2_gpu_1_memtemp = hiveos_api_keys_worker_2["gpu_stats"][1]["memtemp"]
        

    #Worker 2 GPU 2 data    
    worker_2_gpu_2_name = "RTX 3070 Ti ASUS"
    worker_2_gpu_2_index = "2:"
    worker_2_gpu_2_hashrate = hiveos_api_keys_worker_2["gpu_stats"][2]["hash"]
    worker_2_gpu_2_power = hiveos_api_keys_worker_2["gpu_stats"][2]["power"]
    worker_2_gpu_2_fan = hiveos_api_keys_worker_2["gpu_stats"][2]["fan"]
    worker_2_gpu_2_coretemp = hiveos_api_keys_worker_2["gpu_stats"][2]["temp"]  
    worker_2_gpu_2_memtemp = hiveos_api_keys_worker_2["gpu_stats"][2]["memtemp"]
            

    #Worker 2 GPU 3 data
    worker_2_gpu_3_name = "GTX 1660 Super MSI"
    worker_2_gpu_3_index = "3:"
    worker_2_gpu_3_hashrate = hiveos_api_keys_worker_2["gpu_stats"][3]["hash"]
    worker_2_gpu_3_power = hiveos_api_keys_worker_2["gpu_stats"][3]["power"]
    worker_2_gpu_3_fan = hiveos_api_keys_worker_2["gpu_stats"][3]["fan"]
    worker_2_gpu_3_coretemp = hiveos_api_keys_worker_2["gpu_stats"][3]["temp"]           
    worker_2_gpu_3_memtemp = hiveos_api_keys_worker_2["gpu_stats"][3]["memtemp"]
         

    #Worker 2 GPU 4 data
    worker_2_gpu_4_name = "GTX 1660 Super HP"
    worker_2_gpu_4_index = "4:"
    worker_2_gpu_4_hashrate = hiveos_api_keys_worker_2["gpu_stats"][4]["hash"]
    worker_2_gpu_4_power = hiveos_api_keys_worker_2["gpu_stats"][4]["power"]
    worker_2_gpu_4_fan = hiveos_api_keys_worker_2["gpu_stats"][4]["fan"]
    worker_2_gpu_4_coretemp = hiveos_api_keys_worker_2["gpu_stats"][4]["temp"]           
    worker_2_gpu_4_memtemp = hiveos_api_keys_worker_2["gpu_stats"][4]["memtemp"]
          

    #Worker 2 GPU 5 data
    worker_2_gpu_5_name = "GTX 1660 Super ASUS"
    worker_2_gpu_5_index = "5:"
    worker_2_gpu_5_hashrate = hiveos_api_keys_worker_2["gpu_stats"][5]["hash"]
    worker_2_gpu_5_power = hiveos_api_keys_worker_2["gpu_stats"][5]["power"]
    worker_2_gpu_5_fan = hiveos_api_keys_worker_2["gpu_stats"][5]["fan"]
    worker_2_gpu_5_coretemp = hiveos_api_keys_worker_2["gpu_stats"][5]["temp"]                   
    worker_2_gpu_5_memtemp = hiveos_api_keys_worker_2["gpu_stats"][5]["memtemp"]
          

    #Worker 2 GPU 6 data
    worker_2_gpu_6_name = "GTX 1660 Super ASUS"
    worker_2_gpu_6_index = "6:"
    worker_2_gpu_6_hashrate = hiveos_api_keys_worker_2["gpu_stats"][6]["hash"]
    worker_2_gpu_6_power = hiveos_api_keys_worker_2["gpu_stats"][6]["power"]
    worker_2_gpu_6_fan = hiveos_api_keys_worker_2["gpu_stats"][6]["fan"]
    worker_2_gpu_6_coretemp = hiveos_api_keys_worker_2["gpu_stats"][6]["temp"]        
    worker_2_gpu_6_memtemp = hiveos_api_keys_worker_2["gpu_stats"][6]["memtemp"]
         

    #Worker 2 GPU 7 data
    worker_2_gpu_7_name = "GTX 1660 Super ASUS"
    worker_2_gpu_7_index = "7:"
    worker_2_gpu_7_hashrate = hiveos_api_keys_worker_2["gpu_stats"][7]["hash"]
    worker_2_gpu_7_power = hiveos_api_keys_worker_2["gpu_stats"][7]["power"]
    worker_2_gpu_7_fan = hiveos_api_keys_worker_2["gpu_stats"][7]["fan"]
    worker_2_gpu_7_coretemp = hiveos_api_keys_worker_2["gpu_stats"][7]["temp"]          
    worker_2_gpu_7_memtemp = hiveos_api_keys_worker_2["gpu_stats"][7]["memtemp"]
        

    #Create a HTML table from all worker GPUs
    worker_2_table = f"""
	<table class="demTable">
		<thead>
			<tr>
				<th><img src="./Icons/graphics-card.png"/></th>
				<th>Hashrate</th>
				<th>Core Temp (°C)</th>
				<th>Mem Temp (°C)</th>
				<th>Fan (%)</th>
				<th>Power (W)</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_0_name}</td>
				<td>{hashrate_format(worker_2_gpu_0_hashrate)}</td>
				<td>{core_color(worker_2_gpu_0_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_0_memtemp)}</td>
				<td>{worker_2_gpu_0_fan}</td>
				<td>{worker_2_gpu_0_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_1_name}</td>
				<td>{hashrate_format(worker_2_gpu_1_hashrate)}</td>
				<td>{core_color(worker_2_gpu_1_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_1_memtemp)}</td>
				<td>{worker_2_gpu_1_fan}</td>
				<td>{worker_2_gpu_1_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_2_name}</td>
				<td>{hashrate_format(worker_2_gpu_2_hashrate)}</td>
				<td>{core_color(worker_2_gpu_2_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_2_memtemp)}</td>
				<td>{worker_2_gpu_2_fan}</td>
				<td>{worker_2_gpu_2_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_3_name}</td>
				<td>{hashrate_format(worker_2_gpu_3_hashrate)}</td>
				<td>{core_color(worker_2_gpu_3_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_3_memtemp)}</td>
				<td>{worker_2_gpu_3_fan}</td>
				<td>{worker_2_gpu_3_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_4_name}</td>
				<td>{hashrate_format(worker_2_gpu_4_hashrate)}</td>
				<td>{core_color(worker_2_gpu_4_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_4_memtemp)}</td>
				<td>{worker_2_gpu_4_fan}</td>
				<td>{worker_2_gpu_4_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_5_name}</td>
				<td>{hashrate_format(worker_2_gpu_5_hashrate)}</td>
				<td>{core_color(worker_2_gpu_5_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_5_memtemp)}</td>
				<td>{worker_2_gpu_5_fan}</td>
				<td>{worker_2_gpu_5_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_6_name}</td>
				<td>{hashrate_format(worker_2_gpu_6_hashrate)}</td>
				<td>{core_color(worker_2_gpu_6_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_6_memtemp)}</td>
				<td>{worker_2_gpu_6_fan}</td>
				<td>{worker_2_gpu_6_power}</td>
			</tr>
			<tr>
				<td style="text-align: left;">{worker_2_gpu_7_name}</td>
				<td>{hashrate_format(worker_2_gpu_7_hashrate)}</td>
				<td>{core_color(worker_2_gpu_7_coretemp)}</td>
				<td>{mem_color(worker_2_gpu_7_memtemp)}</td>
				<td>{worker_2_gpu_7_fan}</td>
				<td>{worker_2_gpu_7_power}</td>
			</tr>
		</tbody>
	</table>
    """
#In case of an error
except IndexError:
    worker_2_table = f"""
    <div>
        <a style="color: red;">Index error. Please Check script.<br><br></a>
    <div>
    """
        
except KeyError or Exception:
    worker_2_table = f"""
    <div>
        <h1 style="color: red;">OFFLINE!<br><br></h1>
    <div>
    """

#---------- Farm Total Stats ----------#
try:
    total_gpus = str(hiveos_api_keys_farm["stats"]["gpus_online"])
    if hiveos_api_keys_farm["stats"]["gpus_online"] == 12:
        total_gpus = f"""
        <a style="color: green">{total_gpus}</a>
        """
    else:
        total_gpus = f"""
        <a style="color: yellow">{total_gpus}</a>
        """

    total_gpus_offline = str(hiveos_api_keys_farm["stats"]["gpus_offline"])
    if hiveos_api_keys_farm["stats"]["gpus_offline"] > 0:
        total_gpus_offline = f"""
        <a style="color: red">{total_gpus_offline}!!</a>
        """            
    total_hash = str(hashrate_format(hiveos_api_keys_farm["hashrates"][0]["hashrate"]))
    total_power = str(hiveos_api_keys_farm["stats"]["power_draw"]) + " W"
    
    
    
    total_stats = f"""
        <a>Online: {total_gpus}</a><br>
        <a>Offline: {total_gpus_offline}</a><br>
        <a>Hashrate: {total_hash}</a><br>
        <a>Power: {total_power}</a>
    """

except Exception:
    total_stats = f"""
    <div>
        <a>Data load error.</a>
    <div>
    """
