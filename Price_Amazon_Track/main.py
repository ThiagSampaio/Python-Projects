from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
GMAIL ="smtp.gmail.com"
email = "thiagosampaio60@gmail.com"
senha = "312907Thiago"

URL = "https://www.amazon.com.br/Monitor-Professional-Widescreen-P2419H-Preto/dp/B07FDNTS33/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=monitor+dell&qid=1617462846&sr=8-2"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"

}
response = requests.get(URL,  headers= header)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")
price_div = soup.find(id="priceblock_ourprice").get_text()
price_str = price_div.split("R$")[1]
price_str = price_str.replace(".","")
price_str = price_str.replace(",",".")
price_final = float(price_str)

if price_final < 950:
    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(email,senha)
        connection.sendmail(from_addr=email,
                            to_addrs="thiagosampaioparticular@gmail.com",
                            msg = f"Subject: AMAZON PRICE ALERT! \n\nPreco de 1299 foi para {price_final}\n{URL}")