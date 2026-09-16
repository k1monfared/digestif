---
tags: life, python, observation
---
Finding a phone
--

# My Cellphone Journey: From Obsession to Purpose  

For years, I’ve been particular about the cellphones I use. It’s not just about having a phone—it’s about finding one that genuinely solves my problems without forcing me into unnecessary ecosystems or gimmicks. Here's a look at how my relationship with cellphones evolved over time, from the early days of indestructible feature phones to my current obsession with rugged, no-nonsense devices.  

## **The First Phone: Simplicity that Worked**  

My first cellphone was a **Sony Ericsson J100**. It was a no-frills device, but it did what it needed to do: it was reliable, durable, and hardy. I used it without complaints, and it never let me down.  

For a while, I didn’t even own a phone. Back then, I didn’t feel the need for one. That changed with the release of the **Motorola Droid**, one of the first Android smartphones widely available in the U.S. I bought it on day one, and it quickly became a centerpiece of my life.  

## **The Rise and Fall of Smartphones in My Life**  

The Droid ushered in a new era for me. I explored every feature it offered and even experimented with one of the world’s first smartwatches. For a while, I was captivated. My phone was a tool, an organizer, and a companion rolled into one.  

But the honeymoon phase didn’t last. Over time, I became disillusioned with smartphones. They weren’t solving problems for me; they were creating new ones. Notifications, endless customization, and attention-stealing apps made me feel more like a consumer than a user.  

So, I made a drastic decision: I switched to a **dial-pad phone**.  

## **Experimenting with Solutions**  

After a break from smartphones, I slowly ventured back into the market, testing different devices. I tried it all:  
- **Small screens** and **large screens**  
- **Physical keyboards**  
- **Stylus-equipped phones**  
- The latest **smartwatches**  

But no matter what I tried, the result was the same: these phones were not built for people like me. They were built to sell features I didn’t need, push ads I didn’t want, and lock me into ecosystems I avoided.  

This realization shifted my focus. I started looking for phones that prioritized **functionality over flashiness**.  

## **Redefining My Needs**  

What did I want from a phone? My priorities boiled down to these essentials:  
- **Long battery life**  
- **Waterproofing and shockproofing**  
- **SD card slots and headphone jacks**  
- **Decent mic and speaker quality**  
- **Customization options**  

I didn’t care about:  
- Having the **best camera**—a simple one was fine.  
- AI “enhancements” in photos—frankly, I found them unnecessary.  
- Cloud storage—I preferred offline independence.  

The tech industry’s obsession with connectivity frustrated me. Companies like Apple and Google deliberately limited options for offline use, removing SD card slots and offering minimal onboard storage to push cloud services. I didn’t want that. I wanted to take my phone to the mountains, listen to music, read, and take notes without worrying about connectivity.  

## **Discovering Ulefone: A Rugged Solution**  

This search led me to **Ulefone**, a small Chinese company specializing in rugged phones. These devices were a revelation. Ulefone phones weren’t trying to compete with the likes of Apple or Samsung. Instead, they focused on solving real problems for people who needed tough, reliable devices.  

Here’s what I loved about Ulefone:  
- **Durability:** Waterproof, shockproof, and dustproof.  
- **Practical features:** Dual SIM, SD card slots, headphone jacks.  
- **Battery life:** One model lasted an entire week on a single charge.  
- **Affordability:** These phones cost about **1/10th the price** of flagship devices from major brands.  

I’ve put these phones through hell. I’ve dropped them countless times, taken them swimming, and generally abused them in ways that would destroy most devices. Yet they’ve held up remarkably well. This summer, I dived a bit too deep into a lake with my current Ulefone, and while it started acting up, it still works.  

## **Why This Matters**  

For me, phones are tools, not status symbols. I don’t want a device that decides what’s important for me or forces me to conform to its limitations. I want a phone that fits into my life, solves my problems, and respects my choices.  

The big players in the industry—Apple, Google, Samsung—don’t cater to people like me. Their focus is on creating ecosystems that prioritize profit over genuine user needs. Smaller companies like Ulefone, however, are filling that gap.  

If there’s one thing I’ve learned, it’s that you don’t have to settle for what the market says you need. With a bit of searching, you can find tools that work for you—not against you.  

## **Final Thought**  

My journey with cellphones has been about rejecting trends and seeking solutions. While the world chases megapixels and AI gimmicks, I’ll be here with my rugged, reliable phone, ready for whatever life throws at me.  

---

But just as black Friday was approaching I got fooled by a deal from my network provider and ordered a latest version of google pixel, people had generally good things to say about it, and I was thinking to maybe go back to the always connected life for a while to see what I was missing, but while I was waiting for the phone to arrive I was getting anxious that I knew I'm paying a hefty amount of money to first lock myself in for a couple of years and then have to pay the remaining amount to buy the phone while I knew I am not going to enjoy it because they are going to limit my choices as much as they can. Fortunately, I hadn't paid for anything yet and when the phone arrived they started to bring up some extra charges for random things which I declined and got back on the market to see what else is there to explore. I got a couple of recommendations from friends but that wasn't enough. So I went searching. Recently LLM models are getting better, so I asked openAI's O1 model to give me a list of phones from smaller companies that have the features I want, 5G, e-sim, SD card, good battery, water proof, and decent camera. It gave me a bunch of them with generally wrong specs, but the model names where correct. So, I searched for them and found specs on all of them in gsmarena.com. It got hard to compare them, so again I asked gpt-4o-mini to to write some python code that when I provide a list of links, scrapes the phone specs from those websites and put them in a table that I can then use to compare.

Here is a modified version of the code (there are a bunch of unused code there too):

```python
import time
from random import uniform
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# List of common user agents to rotate through
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59'
]

# List of proxy servers (you would need to add your own proxy servers here)
PROXY_LIST = [
    # Add your proxy servers here in the format:
    # 'http://proxy1.example.com:8080',
    # 'http://proxy2.example.com:8080',
]

def get_random_headers():
    """Generate random headers for each request"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

def get_phone_specs(urls):
    # Create a session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=3,  # number of retries
        backoff_factor=1,  # wait 1, 2, 4 seconds between retries
        status_forcelist=[429, 500, 502, 503, 504]  # status codes to retry on
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    all_phones = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    for url in urls:
        # Add random delay between requests (2-5 seconds)
        time.sleep(uniform(2, 5))

        try:
            # Use session instead of requests directly
            response = session.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"Failed to fetch {url}")
                print(f"Status code: {response.status_code}")
                print(f"Response content: {response.text[:200]}...")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the phone's title
            title = soup.find('h1', class_='specs-phone-name-title').text.strip()

            # Initialize dict for this phone's specs
            phone_specs = {'Phone Name': title}

            # Extract the specifications table
            specs = soup.find('div', id='specs-list')
            if specs:
                for category in specs.find_all('table'):
                    for row in category.find_all('tr'):
                        spec_name = row.find('td', class_='ttl').text.strip() if row.find('td', class_='ttl') else "N/A"
                        spec_value = row.find('td', class_='nfo').text.strip() if row.find('td', class_='nfo') else "N/A"
                        phone_specs[spec_name] = spec_value
                        phone_specs['url'] = url

            all_phones.append(phone_specs)
        except:
            pass
    # Convert list of dicts to DataFrame
    phones_df = pd.DataFrame(all_phones)

    return phones_df
```

Then I gave it the list of URLs for the phone I'm interested in
```python

urls = [
    "https://www.gsmarena.com/vivo_iqoo_z7-12163.php",
    "https://www.gsmarena.com/realme_narzo_60-12395.php",
    "https://www.gsmarena.com/xiaomi_poco_f5_pro-12257.php",
    "https://www.gsmarena.com/oneplus_nord_n30-12220.php",
    "https://www.gsmarena.com/asus_zenfone_10-12380.php",
    "https://www.gsmarena.com/motorola_edge_40-12204.php",
    "https://www.gsmarena.com/xiaomi_redmi_note_12_pro-11955.php",
    "https://www.gsmarena.com/nothing_phone_(2)-12386.php",
    "https://www.gsmarena.com/fairphone_4-11136.php",
    "https://www.gsmarena.com/realme_11_pro+-12246.php",
    "https://www.gsmarena.com/infinix_zero_ultra-11922.php",
    "https://www.gsmarena.com/oppo_a78-12073.php",
    "https://www.gsmarena.com/vivo_v27e-12118.php",
    "https://www.gsmarena.com/vivo_v27_pro-12117.php",
    "https://www.gsmarena.com/tecno_phantom_x2-12009.php",
    "https://www.gsmarena.com/xiaomi_poco_x5_pro-12094.php",
    "https://www.gsmarena.com/motorola_moto_g_power_(2024)-12867.php",
    "https://www.gsmarena.com/realme_narzo_60-12395.php",
]
df = get_phone_specs(urls)
df.to_csv("smartphone_specs.csv", index=False)
```

I wish there were websites that would allow me to do these analysis simply without scraping them.

and the results is something I can play with. Let me first clean it a bit. Asking claude-3.5 sonnet: "I am only interested in these specs:
- brand
- model
- does it have 5g?
- does it have e-sim
- year released
- screen size in inches to 1 decimal place
-  does it have dual sim or not
- battery capacity in mAh
- does it have sd card slot?
- the largest back camera mpx
- the selfie camera mpx
- charing speed
- price in USD
write a python code that cleans df to show only those imformation, do necessary string manipulation"
it didn't consider what is in df rows. Then I prompted it as "the columns are not clean info, consider the output of the df.head() cell and adjust the code based on that input", then a few more prompts and it made it mostly work. I haven't checked any of this and I assume it has made several errors, but it gives a good starting point.

```python
def clean_phone_specs(df):
    """Clean and extract specific smartphone specifications"""

    cleaned_df = pd.DataFrame()

    # Extract brand and model from Phone Name
    cleaned_df['brand'] = df['Phone Name'].apply(lambda x: x.split()[0].lower())
    cleaned_df['model'] = df['Phone Name'].apply(lambda x: ' '.join(x.split()[1:]))

    # Check for 5G support
    cleaned_df['has_5g'] = df['Technology'].str.contains('5G', case=False, na=False)

    # Check for eSIM support
    cleaned_df['has_esim'] = df['SIM'].str.contains('eSIM', case=False, na=False)

    # Extract release year from Announced
    cleaned_df['release_year'] = df['Announced'].str.extract(r'(\d{4})')

    # Extract screen size in inches
    cleaned_df['screen_size'] = df['Size'].str.extract(r'(\d+\.?\d*)').astype(float).round(1)

    # Check for dual SIM
    cleaned_df['has_dual_sim'] = df['SIM'].str.contains('Dual', case=False, na=False)

    # Extract battery capacity (checking both old and new battery columns)
    def get_battery_capacity(row):
        if pd.notna(row.get('Type')):
            match = re.search(r'(\d+)\s*mAh', str(row['Type']), re.IGNORECASE)
            if match:
                try:
                    capacity = float(match.group(1))
                    # Sanity check: battery capacity should be between 1000 and 10000 mAh
                    if 1000 <= capacity <= 10000:
                        return capacity
                except ValueError:
                    pass
        return None

    cleaned_df['battery_mah'] = df.apply(get_battery_capacity, axis=1)



    # Extract charging speed (checking Features and Charging columns)
    def get_charging_speed(row):
        # Check Features first
        if pd.notna(row.get('Features')):
            match = re.search(r'(\d+)W?\s*(?:fast\s*charging|charging|wired)', str(row['Features']), re.IGNORECASE)
            if match:
                return float(match.group(1))
        # Check Charging column as fallback
        if pd.notna(row.get('Charging')):
            match = re.search(r'(\d+)W', str(row['Charging']))
            if match:
                return float(match.group(1))
        return None

    cleaned_df['charging_speed'] = df.apply(get_charging_speed, axis=1)

    # Check for SD card slot
    cleaned_df['has_sd_slot'] = df['Card slot'].notna() & ~df['Card slot'].str.contains('No', case=False, na=False)

    # Extract main camera MPX
    def get_max_camera_mpx(row):
        cameras = []
        if pd.notna(row['Triple']):
            mpx = re.findall(r'(\d+)(?:\.?\d*)?MP', row['Triple'])
            cameras.extend([float(x) for x in mpx])
        return max(cameras) if cameras else None

    def get_max_camera_mpx(row):
        cameras = []
        # Check Triple column first
        if pd.notna(row.get('Triple')):
            mpx = re.findall(r'(\d+)(?:\.?\d*)?(?:\s*MP|\s*megapixels)', str(row['Triple']))
            cameras.extend([float(x) for x in mpx if x])
        # Check Single column if no Triple
        elif pd.notna(row.get('Single')):
            mpx = re.findall(r'(\d+)(?:\.?\d*)?(?:\s*MP|\s*megapixels)', str(row['Single']))
            cameras.extend([float(x) for x in mpx if x])
        return max(cameras) if cameras else None

    cleaned_df['main_camera_mpx'] = df.apply(get_max_camera_mpx, axis=1)

    # Extract selfie camera MPX (from Single column which contains front camera info)
    def get_selfie_mpx(row):
        if pd.notna(row.get('Single')):
            mpx = re.findall(r'(\d+)(?:\.?\d*)?(?:\s*MP|\s*megapixels)', str(row['Single']))
            return float(mpx[0]) if mpx else None
        return None

    cleaned_df['selfie_camera_mpx'] = df.apply(get_selfie_mpx, axis=1)

    # Extract price in USD (looking for patterns like "$199.99" or "$1,199.99")
    def extract_price(price_str):
        if pd.isna(price_str):
            return None
        match = re.search(r'\$\s*(\d+(?:,\d+)?(?:\.\d+)?)', str(price_str))
        if match:
            return float(match.group(1).replace(',', ''))
        return None

    cleaned_df['price_usd'] = df['Price'].apply(extract_price)

    return cleaned_df

# Add necessary import
import re

# Clean the dataframe
cdf = clean_phone_specs(df)
```

The results are:
|    | brand     | model               | has_5g   | has_esim   |   release_year |   screen_size | has_dual_sim   |   battery_mah |   charging_speed | has_sd_slot   |   main_camera_mpx |   selfie_camera_mpx |   price_usd |
|---:|:----------|:--------------------|:---------|:-----------|---------------:|--------------:|:---------------|--------------:|-----------------:|:--------------|------------------:|--------------------:|------------:|
|  0 | vivo      | iQOO Z7             | True     | False      |           2023 |           6.4 | True           |          4500 |               44 | True          |                16 |                  16 |      nan    |
|  1 | realme    | Narzo 60            | True     | False      |           2023 |           6.4 | True           |          5000 |               33 | True          |                16 |                  16 |      nan    |
|  2 | xiaomi    | Poco F5 Pro         | True     | False      |           2023 |           6.7 | True           |          5160 |               67 | False         |                64 |                  16 |      438.96 |
|  3 | oneplus   | Nord N30            | True     | False      |           2023 |           6.7 | True           |          5000 |               50 | True          |               108 |                  16 |      279.99 |
|  4 | asus      | Zenfone 10          | True     | False      |           2023 |           5.9 | True           |          4300 |               30 | False         |                32 |                  32 |     1199    |
|  5 | motorola  | Edge 40             | True     | True       |           2023 |           6.6 | True           |          4400 |               68 | False         |                32 |                  32 |      389.99 |
|  6 | xiaomi    | Redmi Note 12 Pro   | True     | False      |           2022 |           6.7 | True           |          5000 |               67 | False         |                50 |                  16 |      170    |
|  7 | nothing   | Phone (2)           | True     | False      |           2023 |           6.7 | True           |          4700 |               45 | False         |                32 |                  32 |      529.99 |
|  8 | fairphone | 4                   | True     | True       |           2021 |           6.3 | False          |          3905 |               20 | True          |                25 |                  25 |      nan    |
|  9 | realme    | 11 Pro+             | True     | False      |           2023 |           6.7 | True           |          5000 |              100 | False         |               200 |                  32 |      nan    |
| 10 | infinix   | Zero Ultra          | True     | False      |           2022 |           6.8 | True           |          4500 |              180 | False         |               200 |                  32 |      nan    |
| 11 | oppo      | A78                 | True     | False      |           2023 |           6.6 | True           |          5000 |               33 | True          |                 8 |                   8 |      nan    |
| 12 | vivo      | V27e                | False    | False      |           2023 |           6.6 | True           |          4600 |               66 | True          |                64 |                  32 |      nan    |
| 13 | vivo      | V27 Pro             | True     | False      |           2023 |           6.8 | True           |          4600 |               66 | False         |                50 |                  50 |      nan    |
| 14 | tecno     | Phantom X2          | True     | False      |           2022 |           6.8 | True           |          5160 |               45 | False         |                64 |                  32 |      nan    |
| 15 | xiaomi    | Poco X5 Pro         | True     | False      |           2023 |           6.7 | True           |          5000 |               67 | False         |               108 |                  16 |      241.19 |
| 16 | motorola  | Moto G Power (2024) | True     | True       |           2024 |           6.7 | False          |          5000 |               30 | True          |                16 |                  16 |      169.98 |
| 17 | realme    | Narzo 60            | True     | False      |           2023 |           6.4 | True           |          5000 |               33 | True          |                16 |                  16 |      nan    |

now let's see which ones have what I need
```python
cdf.loc[
    (cdf['has_5g'] == True) &
    (cdf['has_esim'] == True) &
    (cdf['has_sd_slot'] == True),
    ['brand', 'model', 'release_year', 'screen_size', 'battery_mah', 'charging_speed', 'main_camera_mpx', 'selfie_camera_mpx','price_usd']
]
```
OK, only fairphone 4 and Moto G Power have 5g, esim, and sdcard slot. Their cameras are not great, but I can live with that and screen sizes are too big. Also fairphone 4 seems a bit too old (2021). I might have to expand my search a little bit.

It's interesting, I wanted to compare motorola edge 40 but it didn't show up. it seems like it doesn't have sd card slot!

The BeautifulSoup approach is not great, it misses a lot of details, pandas has this `read_html` functionality which reads very well from this website. I also need to manage how many requests I'm sending to the webpage and change the proxy so that it doesn't block me. Will do that next.


---

### Update 2025-01-05
I've tried the [TCL 50 XE NXTPAPER](https://www.gsmarena.com/tcl_50_xe_nxtpaper-13302.php) for a couple of weeks. It is pretty weak in terms of performance. It got pretty hot while on a video call to the point it was uncomfortable. And worst of all, the screen wasn't at all readable in direct light, even lamp light. It definitely is less glossy, but that not only it doesn't make it easier to read the screen, it makes it much much worse. I compared it in various conditions with my old phone that has a simple screen, and also with other phones that have no claim of more readability. It is almost impossible to see the content of the screen when there is direct light shining on it. With regular screens you can turn the screen slightly and it will be resolved, with this phone, even that is not possible! The camera is so so, nothing exciting, nothing particularly bad. Also, the paper color and ink color modes are good ideas, but not best implemented, there's lots of restrictions and not much customizable. Even going to dark mode, or changing the background in those modes seems to need tricks! If they continue improving it, it might become a good option. Initially, they had advertised it so that I thought the ink color mode is actually e-ink screen under a regular screen that when activated the regular screen turns off and the e-ink will be used, but that's not the case, it is just a blakc and while mode. So, I've returned it.

Next I'm going to try a motorolla [Motorola G85](https://www.gsmarena.com/motorola_moto_g85-13144.php). I wanted a [G75](https://www.gsmarena.com/motorola_moto_g75-13372.php) model since it is more waterproof (IP68), but I couldn't find it in any stores. G85 only has a water repellent design, but still similar in other aspects. Motorla generally is not supposed to have good camera, so I'm not going to expect much there.
