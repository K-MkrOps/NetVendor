# NetVendor

## What vendors are lurking on your network? 

*This software figures this out!* 

## How?
This program reviews an ARP or MAC Address table (Such as a Cisco IOS ```sh ip arp``` or ```sh mac add``` output), and produces information on your network like:
* How many different vendors (as in companies) exist within your network?
* How many different types of hardware (MAC OUIs) exist within your network?
* Where are all these things, and what are their IPs?
* A list (and total) of all the Apple, Cisco, Dell, HP, and Mitel products that exist on your network
* Are there any hidden VLANs lurking within your network? *This answers this too!*

Table of Contents:
  - [Why?](#why)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Why?
* Understanding what *exactly* is in your network is **_essential_** for security reasons... <br>
* Benchmarks your network so you can easily see changes

## Dependencies 
* This uses a restful API to search for the vendors, so it needs a working internet connection
* This needs the output of an ARP or MAC Address table as a text file (such as the Cisco IOS ```#sh ip arp ``` format seen below), as it is using this to do the lookup
## Input
* Contents of an ARP or MAC Address table as a text file (such as a Cisco ```#sh ip arp``` output, like below):</br></br>
 ![image](https://user-images.githubusercontent.com/48565067/144638643-f26b64fe-e992-4163-a0a9-a1c90b0b6028.png)
## Output
* Example of the output: </br></br>
![image](https://user-images.githubusercontent.com/48565067/164489106-50b4310c-8a42-4715-824c-beba926dfcba.png)
![program_output2](https://user-images.githubusercontent.com/48565067/156942018-807a5762-dcb8-49b0-b8df-fc33dec61433.png)
![image](https://user-images.githubusercontent.com/48565067/159778884-924f1c9c-ecf6-46ea-88aa-c4529eb741c3.png)

 - If Chrome or Firefox is available (on a Windows, Mac or Linux system), it will create an interactive web-based pie chart and display it in the browser:
 ![2022-03-06 18 43 25](https://user-images.githubusercontent.com/48565067/156947443-4510c608-b49f-4f3c-a8c9-60da13627ba6.png)
 * Created text file "company_list.txt" output:</br></br>
 ![image](https://user-images.githubusercontent.com/48565067/144633574-5bc13c04-a712-490d-b186-a30b4d9d8a73.png)
* Created text file "oui_final_list.txt" output:</br></br>
 ![image](https://user-images.githubusercontent.com/48565067/144633706-24bbe2ef-6965-4847-b3a9-0f22242ff95f.png)
* Created Vendor-Devices.txt file:</br></br>
  ![image](https://user-images.githubusercontent.com/48565067/144880526-74cc7658-ae97-4841-812e-24f4f274525d.png)
* Creates a list of CSV "spreadsheet" device files and puts them in a new ```csv_files``` folder
* Puts all the ```*.txt``` files created into the ```text_files``` folder 

## To Do / Updates
- [x] Automatically attempts to upgrade required libraries (05/22/2022)
- [x] Added a banner and info box (see output section of readme, 04/21/22)
- [x] Fixed issue if text / CSV files already exist (04/07/2022)
- [x] Added a timeout to the Vendor lookup, and *significantly* improved company lookup time (04/06/2022)
- [x] Created CSV files for every created device text file in a separate ```csv_files``` folder, for easy review by any spreadsheet app like [visidata](https://www.visidata.org) (added 03/23/2022)
- [x] Added code to move all the ```*.txt``` files to a created ```text_files``` folder (added 03/23/2022)
- [x] Fixed a bug where a created csv file may have contents from more than one device file in it (resolved 03/23/2022)
- [x] Used the [rich](https://github.com/Textualize/rich) library to colorize cli output (added 03/06/2022)
- [x] Style Improvements [on-going, started 03/06/2022]
- [x] Added lookup for Mitel Corperation Phones (02/11/2022)
- [x] Streamlined API call, add support for Apple Macs (supporting Windows, Linux or Mac computers (Added 02/10/2022)
- [x] Added a progress bar for collecting oui info via “tqdm” (added 12/22/2021)
- [ ] Use the sanitized OUI list [here](https://linuxnet.ca/ieee/oui/), to increase filtering (on-going)
-----
## This app is free❗
* However if you want to help fund my development of this app, feel free using my tag, ```$StewAlexander``` via [cash app]( https://cash.app/)
*  [Click here for further instructions on how to send money via Cash App](https://cash.app/help/us/en-us/1105-sending-a-payment)
<br>
<br>

