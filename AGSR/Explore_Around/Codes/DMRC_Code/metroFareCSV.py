import csv
import string

def metroFare(fromS,toS):
    day = string.capwords('sunday')
    if day != "Sunday":
        day = ""
    fileName = "DMRC_Code\csv\MetroFare" + day + ".csv"
    #fileName = "Users\Sachin Roy\Desktop\AGSR\Explore_Around\Codes\DMRC_Code\csv\MetroFare" + day + ".csv"
    #fileName = "Users/Sachin Roy/Desktop/AGSR/Explore_Around/Codes/DMRC_Code/csv/MetroFare" + day + ".csv"
    toStation = string.capwords(toS)
    fromStation = string.capwords(fromS)

    list = "S.No.,Stations,Dilshad Garden,Jhilmil,Mansrovar park,Shahdara,Welcome,Seelampur,Shastri Park,Kashmere Gate,Tis Hazari,Pul Bangash,Pratap Nagar,Shastri Nagar,Inder Lok,Kanhaiya Nagar,Keshav Puram,Netaji Subash Place,Kohat Enclave,Pitam Pura,Rohini East,Rohini West,Rithala,Samaypur Badli,Rohini Sector - 18,Haiderpur Badli Mor,Jahangirpuri,Adarsh Nagar,Azadpur,Model Town,GTB Nagar,Vishwavidyalaya,Vidhan Sabha,Civil Lines,Kashmere Gate,Chandhni Chowk,Chawri Bazar,New Delhi,Rajiv Chowk,Patel Chowk,Central Secretariat,Udyog Bhawan,Lok Kalyan Marg,Jorbagh,INA,AIIMS,Green Park,Hauz Khas,Malviya Nagar,Saket,Qutab Minar,Chhattarpur,Sultanpur,Ghitorni,Arjan Garh,Guru Dronacharya,Sikandarpur,MG Road,IFFCO Chowk,Huda City Centre,Noida City Centre,Golf Course,Botanical Garden,Noida Sect 18,Noida Sect 16,Noida Sect 15,New Ashok Nagar,Mayur Vihar Ext,Mayur Vihar-I,Akshardham,Yamuna Bank,Indraprastha,Pragati Maidan,Mandi House,Barakhamba Road,Rajiv Chowk,RK Ashram Marg,Jhandewalan,Karol Bagh,Rajendra Place,Patel Nagar,Shadipur,Kirti Nagar,Moti Nagar,Ramesh Nagar,Rajouri Garden,Tagore Garden,Subash Nagar,Tilak Nagar,Janak Puri East,Janak Puri West,Uttam Nagar East,Uttam Nagar West,Nawada,Dwarka Mor,Dwarka,Dwarka Sector - 14,Dwarka Sector - 13,Dwarka Sector - 12,Dwarka Sector - 11,Dwarka Sector - 10,Dwarka Sector - 9,Dwarka Sector - 8,Dwarka Sector - 21,Vaishali,Kaushambi,Anand Vihar,Karkar Duma,Preet Vihar,Nirman Vihar,Laxmi Nagar,City Park,Bus Stand,Modern Industrial Estate,Tikri Border,Tikri Kalan,Ghevra Metro Station,Mundka Industrial Area,Mundka,Rajdhani Park,Nangloi Rly. Station,Nangloi,Surajmal Stadium,Udyog Nagar,Peera Garhi,Paschim Vihar (West),Paschim Vihar (East),Madi Pur,Shivaji Park,Punjabi Bagh,Ashok Park Main,Inder Lok,Satguru Ram Singh Marg,Kirti Nagar,Kashmere Gate,Lal Quila,Jama Masjid,Delhi Gate,ITO,Mandi House,Janpath,Central Secretariat,Khan Market,JLN,Jangpura,Lajpat Nagar,Moolchand,Kailash Colony,Nehru Place,Kalkaji Mandir,Govindpuri,Okhla,Jasola-Apollo,Sarita Vihar,Mohan Estate,Tuglakabad,Badarpur,Sarai,NHPC Chowk,Mewala Maharajpur,Sector-28,Badkal Mor,Old Faridabad,Neelam Chowk Ajronda,Bata Chowk,Escorts Mujesar,Sant Surdas,Raja Nahar Singh,Botanical Garden,Okhla Bird Sanctuary,Kalindi Kunj,Jasola Vihar,Okhla Vihar,Jamia Milia Islamiya,Sukhdev Vihar,NSIC Okhla,Kalkaji Mandir,Nehru Enclave,Greater Kailash,Chirag Delhi,Panchsheel Park,Hauz Khas,I.I.T,R.K.Puram,Munirka,Vasant Vihar,Shankar Vihar,IGD Airport,Sadar Bazar,Palam,Dashrathpuri,Dabri Mor,Janak Puri West,Majlis Park,Azadpur,Shalimar Bagh,Netaji Subash Place,Shakurpur,Punjabi Bagh West,ESI Hospital,Rajouri Garden,Mayapuri,Naraina Vihar,Delhi Cantt.,Durgabai Deshmukh South Campus,Sir Vishweshwaraiah Moti Bagh,Bhikaji Cama Place,Sarojini Nagar,INA,South Extension,Lajpat Nagar,Trilokpuri,Vinod Nagar East,Vinod Nagar,I.P. Extension,Anand Vihar,Karkar Duma,Karkarduma Court,Krishna Nagar,East Azad Nagar,Welcome,Jafrabad,Maujpur,Gokulpuri,Johri Enclave,Shiv Vihar,Sector 55-56,Sector 54 Chowk,Sector 53-54,Sector 42-43,Phase-I,Sikanderpur,Phase 2,Belvedere Towers,Cyber City,Moulsari Avenue,Phase 3"
    list = list.split(",")

    idx = 0
    flag = -1
    for i in list:
        if toStation == i and idx > 1:
            flag = 0
            break
        idx = idx + 1
    if flag == -1:
        return "Destination station not found"
    elif flag == 0:
        with open(fileName) as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            next(reader)
            for list in reader:
                if list[1] == fromStation:
                    flag = 1
                    return "Price of your route is :" + list[idx]
        if flag == 0:
            return "Starting station not found"
