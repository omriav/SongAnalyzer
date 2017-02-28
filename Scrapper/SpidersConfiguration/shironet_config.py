from Model.artist_url import artist_url

class shironet_config:
    SHIRONET_BASE_URL = "http://shironet.mako.co.il"
    SHIRONET_AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    SHIRONET_COOKIE = {'rbzid': 'MzdwR3RzaDhRd1J2TjJPMWVHbTJjN0E1bi9LMUFUVVRXOWJPWElkQVZwYWtaVnJycnFManh3REwvSktVRmVxNXBjejA3UjlyOFNTQzc0RFVhUFFhZ2FmY1J3aGFPZ2lYMjEzcVhrVlZOVzFKZlQ2dnlsanYzTkVYQ2JGaks4VnJEVUxnYVhvaG1JNldlRzNkbU5ZMDMyTzY4UDluSGtYMklGYlRsREJjNHBKbDB4TWNmSkJuQjFOTTZzNjBwUlowL2ZCTEVOZWhQSmloVWY0LzFaM2FLdz09QEBAMEBAQC0xNDgxNDgxNDY4MA'}

    ARTIST_PAGE_PREFIX = "http://shironet.mako.co.il/artist?type=works&lang=1&prfid="
    ARTISTS_URLS = [
        artist_url("Idan Raichel",  ARTIST_PAGE_PREFIX + '1428'),
        artist_url("Eviatar Banai", ARTIST_PAGE_PREFIX + '41'),
        artist_url("Moshe Peretz", ARTIST_PAGE_PREFIX + '3787'),
        artist_url("Dudu Aharon", ARTIST_PAGE_PREFIX + '4592'),
        artist_url("Kobi Peretz", ARTIST_PAGE_PREFIX + '1202'),
        artist_url("Meir Ariel", ARTIST_PAGE_PREFIX + '605'),
        artist_url("Hadag Nahash", ARTIST_PAGE_PREFIX + '333'),
        artist_url("Lior Narkis", ARTIST_PAGE_PREFIX + '594'),
        artist_url("Mooki", ARTIST_PAGE_PREFIX + '620'),
        artist_url("Peer Tasi", ARTIST_PAGE_PREFIX + '7747'),
        artist_url("Eyal Golan", ARTIST_PAGE_PREFIX + '92'),
        artist_url("Omer Adam", ARTIST_PAGE_PREFIX + '10755'),
        artist_url("Regev Hod", ARTIST_PAGE_PREFIX + '2570'),
        artist_url("Sarit Hadad", ARTIST_PAGE_PREFIX + '1015'),
        artist_url("Shlomo Artzi", ARTIST_PAGE_PREFIX + '975'),
        artist_url("Shalom Hanoch", ARTIST_PAGE_PREFIX + '960'),
        artist_url("Arik Einstein", ARTIST_PAGE_PREFIX + '166'),
        artist_url("Rita", ARTIST_PAGE_PREFIX + '905'),
        artist_url("Miri Mesika", ARTIST_PAGE_PREFIX + '4226'),
        artist_url("Keren Peles", ARTIST_PAGE_PREFIX + '4314'),
        artist_url("Assaf Amdursky", ARTIST_PAGE_PREFIX + '150'),
        artist_url("Avraham Tal", ARTIST_PAGE_PREFIX + '7335'),
        artist_url("Mashina", ARTIST_PAGE_PREFIX + '686'),
        artist_url("Yehoram Gaon", ARTIST_PAGE_PREFIX + '465'),
        artist_url("Yishi Levi", ARTIST_PAGE_PREFIX + '559'),
        artist_url("Avi Biter", ARTIST_PAGE_PREFIX + '1145'),
        artist_url("Shlomi Shabat", ARTIST_PAGE_PREFIX + '966'),
        artist_url("Zehava Ben", ARTIST_PAGE_PREFIX + '372'),
        artist_url("Zohar Argov", ARTIST_PAGE_PREFIX + '373'),
        artist_url("Lior Farhi", ARTIST_PAGE_PREFIX + '596'),
        artist_url("Shimi Tavori", ARTIST_PAGE_PREFIX + '955'),
        artist_url("Ofer Levi", ARTIST_PAGE_PREFIX + '783'),
        artist_url("Moshik Afia", ARTIST_PAGE_PREFIX + '623'),
        artist_url("Idan Yaniv", ARTIST_PAGE_PREFIX + '4858'),
        artist_url("Margalit Tzanani", ARTIST_PAGE_PREFIX + '666'),
        artist_url("Boaz Sharabi", ARTIST_PAGE_PREFIX + '183'),
        artist_url("Yehuda Poliker", ARTIST_PAGE_PREFIX + '459'),
        artist_url("Berry Sakharof", ARTIST_PAGE_PREFIX + '202'),
        artist_url("Rami Fortis", ARTIST_PAGE_PREFIX + '915'),
        artist_url("Mosh Ben Ari", ARTIST_PAGE_PREFIX + '1229'),
        artist_url("Hayehudim", ARTIST_PAGE_PREFIX + '341'),
        artist_url("Aviv Geffen", ARTIST_PAGE_PREFIX + '34'),
        artist_url("Chava Alberstein", ARTIST_PAGE_PREFIX + '383'),
        artist_url("Matti Caspi", ARTIST_PAGE_PREFIX + '688'),
        artist_url("Shlomo Gronich", ARTIST_PAGE_PREFIX + '980'),
        artist_url("Yehudit Ravitz", ARTIST_PAGE_PREFIX + '462'),
        artist_url("Gali Atari", ARTIST_PAGE_PREFIX + '268'),
        artist_url("Nurit Galron", ARTIST_PAGE_PREFIX + '713'),
        artist_url("Danny Sanderson", ARTIST_PAGE_PREFIX + '314'),
        artist_url("Alon Oleartchik", ARTIST_PAGE_PREFIX + '122'),
        artist_url("Dani Litani", ARTIST_PAGE_PREFIX + '311'),
        artist_url("Gidi Gov", ARTIST_PAGE_PREFIX + '225'),
        artist_url("Ehud Banai", ARTIST_PAGE_PREFIX + '57'),
        artist_url("Meir Banai", ARTIST_PAGE_PREFIX + '606'),
        artist_url("Knesiyat Hasechel", ARTIST_PAGE_PREFIX + '565'),
        artist_url("Arkadi Duchin", ARTIST_PAGE_PREFIX + '173'),
        artist_url("Maor Cohen", ARTIST_PAGE_PREFIX + '602'),
        artist_url("Yermi Kaplan", ARTIST_PAGE_PREFIX + '557'),
        artist_url("Eran Zur", ARTIST_PAGE_PREFIX + '823'),
        artist_url("Ninet Tayeb", ARTIST_PAGE_PREFIX + '2666'),
        artist_url("Arik Sinai", ARTIST_PAGE_PREFIX + '169')
    ]
