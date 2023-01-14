import shodan #chargement de la ibrairie shodan
import requests
import argparse

#Pour que le script puisse utiliser l'API Shodan
SHODAN_API_KEY = "jegaSstSh2fo9zNqKNHn7puZKoSoakQT"

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="nom de domaine")
parser.add_argument("-i", "--ip", help="adresse ip")
parser.add_argument("-o", "--output", help="sortie d'un fichier")
args = parser.parse_args()

if args.domain:
    #Si un nom de domain est entré, Shodan récolte l'adresse IP
    dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + args.domain + '&key=' + SHODAN_API_KEY
    resolved = requests.get(dnsResolve) #Récuperer la sortie de dnsResolve
    args.ip = resolved.json()[args.domain] #Récupération de l'adresse IP


api = shodan.Shodan(SHODAN_API_KEY)
#Analyse de l'adresse IP
host = api.host(args.ip)

# Affichage des différentes informations récoltés par l'API Shodan
print("""
Informations Générale :
Adresse IP : {}
Nom de l'entreprise : {}
Systeme d'opération : {}
Numéro de Système Autonome (ASN) : {}
Fournisseur Internet : {}

Information de géolocalisation :
Pays : {}
Region : {}
Ville : {}
Code Postale : {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('asn', 'n/a'), host.get('isp', 'n/a'),
            host.get('country_name', 'n/a'), host.get('region_code', 'n/a'), host.get('city', 'n/a'), host.get('postal_code', 'n/a')))
