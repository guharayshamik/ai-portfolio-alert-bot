WATCHLISTS = {
    "my_portfolio": {
        "priority": 1,
        "alert_individual": True,
        "description": "Stocks/options I personally hold or actively track.",
        "symbols": {
            "MU": "Micron Technology",
            "MRVL": "Marvell Technology",
            "COHR": "Coherent Corp",
            "NVDA": "NVIDIA Corporation",
            "AMD": "Advanced Micro Devices",
            "ARM": "Arm Holdings",
            "INTC": "Intel Corporation",
            "LAC": "Lithium Americas Corp",
            "NOK": "Nokia Corporation"
        }
    },

    "semiconductors": {
        "priority": 2,
        "alert_individual": False,
        "description": "Broad semiconductor and AI infrastructure companies.",
        "symbols": {
            "NVDA": "NVIDIA Corporation",
            "AMD": "Advanced Micro Devices",
            "AVGO": "Broadcom Inc",
            "MU": "Micron Technology",
            "MRVL": "Marvell Technology",
            "COHR": "Coherent Corp",
            "ARM": "Arm Holdings",
            "INTC": "Intel Corporation",
            "QCOM": "Qualcomm Inc",
            "TSM": "Taiwan Semiconductor Manufacturing",
            "ASML": "ASML Holding",
            "AMAT": "Applied Materials",
            "LRCX": "Lam Research",
            "KLAC": "KLA Corporation",
            "WDC": "Western Digital",
            "STX": "Seagate Technology"
        }
    },

    "ai_infrastructure": {
        "priority": 2,
        "alert_individual": False,
        "description": "AI datacenter infrastructure and networking names.",
        "symbols": {
            "NVDA": "NVIDIA Corporation",
            "AVGO": "Broadcom Inc",
            "MRVL": "Marvell Technology",
            "COHR": "Coherent Corp",
            "ANET": "Arista Networks",
            "VRT": "Vertiv Holdings",
            "SMCI": "Super Micro Computer"
        }
    },

    "big_tech": {
        "priority": 3,
        "alert_individual": False,
        "description": "Mega-cap technology and AI platform companies.",
        "symbols": {
            "AAPL": "Apple Inc",
            "MSFT": "Microsoft Corporation",
            "GOOGL": "Alphabet Inc",
            "AMZN": "Amazon.com Inc",
            "META": "Meta Platforms",
            "TSLA": "Tesla Inc",
            "NFLX": "Netflix Inc"
        }
    },

    "cybersecurity": {
        "priority": 3,
        "alert_individual": False,
        "description": "Cybersecurity leaders.",
        "symbols": {
            "PANW": "Palo Alto Networks",
            "CRWD": "CrowdStrike",
            "ZS": "Zscaler",
            "NET": "Cloudflare",
            "FTNT": "Fortinet",
            "CHKP": "Check Point Software",
            "OKTA": "Okta",
            "CYBR": "CyberArk"
        }
    },

    "power_datacenter": {
        "priority": 3,
        "alert_individual": False,
        "description": "Power, cooling, and datacenter infrastructure names.",
        "symbols": {
            "VRT": "Vertiv Holdings",
            "ETN": "Eaton Corporation",
            "CEG": "Constellation Energy",
            "VST": "Vistra Corp"
        }
    },

    "defensive_old_economy": {
        "priority": 4,
        "alert_individual": False,
        "description": "Defensive and consumer staple companies.",
        "symbols": {
            "WMT": "Walmart Inc",
            "KO": "Coca-Cola Company",
            "PEP": "PepsiCo Inc",
            "PG": "Procter & Gamble",
            "JNJ": "Johnson & Johnson",
            "MCD": "McDonald's Corporation",
            "COST": "Costco Wholesale",
            "CL": "Colgate-Palmolive"
        }
    },

    "financials": {
        "priority": 4,
        "alert_individual": False,
        "description": "Major banks and financial institutions.",
        "symbols": {
            "JPM": "JPMorgan Chase",
            "BAC": "Bank of America",
            "WFC": "Wells Fargo",
            "GS": "Goldman Sachs",
            "MS": "Morgan Stanley",
            "C": "Citigroup"
        }
    },

    "energy": {
        "priority": 4,
        "alert_individual": False,
        "description": "Energy majors.",
        "symbols": {
            "XOM": "Exxon Mobil",
            "CVX": "Chevron",
            "COP": "ConocoPhillips",
            "SLB": "Schlumberger"
        }
    },

    "healthcare": {
        "priority": 4,
        "alert_individual": False,
        "description": "Healthcare and pharmaceutical companies.",
        "symbols": {
            "LLY": "Eli Lilly",
            "UNH": "UnitedHealth Group",
            "ABBV": "AbbVie",
            "PFE": "Pfizer",
            "MRK": "Merck & Co"
        }
    },

    "sector_etfs": {
        "priority": 1,
        "alert_individual": True,
        "description": "ETF signals used to detect sector-wide pressure.",
        "symbols": {
            "QQQ": "Invesco QQQ Trust",
            "SPY": "SPDR S&P 500 ETF",
            "SMH": "VanEck Semiconductor ETF",
            "SOXX": "iShares Semiconductor ETF",
            "HYG": "iShares High Yield Corporate Bond ETF",
            "JNK": "SPDR Bloomberg High Yield Bond ETF",
            "TLT": "iShares 20+ Year Treasury Bond ETF",
            "VIXY": "ProShares VIX Short-Term Futures ETF",
            "USO": "United States Oil Fund",
            "DXY": "US Dollar Index"
        }
    }
}


STOCK_METADATA = {
    "MU": {"name": "Micron Technology", "industry": "Memory", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "WDC": {"name": "Western Digital", "industry": "Memory", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "STX": {"name": "Seagate Technology", "industry": "Memory", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},

    "MRVL": {"name": "Marvell Technology", "industry": "Networking Chips", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "COHR": {"name": "Coherent Corp", "industry": "Optical / Photonics", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "NVDA": {"name": "NVIDIA Corporation", "industry": "AI Accelerators", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "AMD": {"name": "Advanced Micro Devices", "industry": "AI / CPUs / GPUs", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "ARM": {"name": "Arm Holdings", "industry": "Chip IP", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},
    "INTC": {"name": "Intel Corporation", "industry": "CPUs / Foundry", "sector": "Semiconductors", "portfolio": True, "alert_threshold": -3},

    "AVGO": {"name": "Broadcom Inc", "industry": "AI Networking / ASICs", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "QCOM": {"name": "Qualcomm Inc", "industry": "Mobile Chips", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "TSM": {"name": "Taiwan Semiconductor Manufacturing", "industry": "Foundry", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "ASML": {"name": "ASML Holding", "industry": "Semiconductor Equipment", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "AMAT": {"name": "Applied Materials", "industry": "Semiconductor Equipment", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "LRCX": {"name": "Lam Research", "industry": "Semiconductor Equipment", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},
    "KLAC": {"name": "KLA Corporation", "industry": "Semiconductor Equipment", "sector": "Semiconductors", "portfolio": False, "alert_threshold": -3},

    "ANET": {"name": "Arista Networks", "industry": "AI Networking", "sector": "AI Infrastructure", "portfolio": False, "alert_threshold": -3},
    "VRT": {"name": "Vertiv Holdings", "industry": "Datacenter Infrastructure", "sector": "AI Infrastructure", "portfolio": False, "alert_threshold": -3},
    "SMCI": {"name": "Super Micro Computer", "industry": "AI Servers", "sector": "AI Infrastructure", "portfolio": False, "alert_threshold": -4},
    "ETN": {"name": "Eaton Corporation", "industry": "Power Infrastructure", "sector": "Industrial / Datacenter", "portfolio": False, "alert_threshold": -3},
    "CEG": {"name": "Constellation Energy", "industry": "Power Infrastructure", "sector": "Energy / Datacenter", "portfolio": False, "alert_threshold": -3},
    "VST": {"name": "Vistra Corp", "industry": "Power Infrastructure", "sector": "Energy / Datacenter", "portfolio": False, "alert_threshold": -3},

    "LAC": {"name": "Lithium Americas Corp", "industry": "Lithium", "sector": "Materials", "portfolio": True, "alert_threshold": -4},
    "NOK": {"name": "Nokia Corporation", "industry": "Telecom Equipment", "sector": "Communications", "portfolio": True, "alert_threshold": -3},

    "AAPL": {"name": "Apple Inc", "industry": "Consumer Tech", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},
    "MSFT": {"name": "Microsoft Corporation", "industry": "Cloud / Software", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},
    "GOOGL": {"name": "Alphabet Inc", "industry": "Cloud / Ads", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},
    "AMZN": {"name": "Amazon.com Inc", "industry": "Cloud / Ecommerce", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},
    "META": {"name": "Meta Platforms", "industry": "Social / AI", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},
    "TSLA": {"name": "Tesla Inc", "industry": "EV / AI", "sector": "Big Tech", "portfolio": False, "alert_threshold": -4},
    "NFLX": {"name": "Netflix Inc", "industry": "Streaming", "sector": "Big Tech", "portfolio": False, "alert_threshold": -3},

    "PANW": {"name": "Palo Alto Networks", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "CRWD": {"name": "CrowdStrike", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "ZS": {"name": "Zscaler", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "NET": {"name": "Cloudflare", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "FTNT": {"name": "Fortinet", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "CHKP": {"name": "Check Point Software", "industry": "Cybersecurity", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "OKTA": {"name": "Okta", "industry": "Identity Security", "sector": "Software", "portfolio": False, "alert_threshold": -3},
    "CYBR": {"name": "CyberArk", "industry": "Identity Security", "sector": "Software", "portfolio": False, "alert_threshold": -3},

    "WMT": {"name": "Walmart Inc", "industry": "Retail Defensive", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "KO": {"name": "Coca-Cola Company", "industry": "Consumer Staples", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "PEP": {"name": "PepsiCo Inc", "industry": "Consumer Staples", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "PG": {"name": "Procter & Gamble", "industry": "Consumer Staples", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "JNJ": {"name": "Johnson & Johnson", "industry": "Healthcare Defensive", "sector": "Healthcare", "portfolio": False, "alert_threshold": -2},
    "MCD": {"name": "McDonald's Corporation", "industry": "Restaurants Defensive", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "COST": {"name": "Costco Wholesale", "industry": "Retail Defensive", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},
    "CL": {"name": "Colgate-Palmolive", "industry": "Consumer Staples", "sector": "Defensive", "portfolio": False, "alert_threshold": -2},

    "JPM": {"name": "JPMorgan Chase", "industry": "Banks", "sector": "Financials", "portfolio": False, "alert_threshold": -3},
    "BAC": {"name": "Bank of America", "industry": "Banks", "sector": "Financials", "portfolio": False, "alert_threshold": -3},
    "WFC": {"name": "Wells Fargo", "industry": "Banks", "sector": "Financials", "portfolio": False, "alert_threshold": -3},
    "GS": {"name": "Goldman Sachs", "industry": "Investment Banking", "sector": "Financials", "portfolio": False, "alert_threshold": -3},
    "MS": {"name": "Morgan Stanley", "industry": "Investment Banking", "sector": "Financials", "portfolio": False, "alert_threshold": -3},
    "C": {"name": "Citigroup", "industry": "Banks", "sector": "Financials", "portfolio": False, "alert_threshold": -3},

    "XOM": {"name": "Exxon Mobil", "industry": "Oil & Gas", "sector": "Energy", "portfolio": False, "alert_threshold": -3},
    "CVX": {"name": "Chevron", "industry": "Oil & Gas", "sector": "Energy", "portfolio": False, "alert_threshold": -3},
    "COP": {"name": "ConocoPhillips", "industry": "Oil & Gas", "sector": "Energy", "portfolio": False, "alert_threshold": -3},
    "SLB": {"name": "Schlumberger", "industry": "Oilfield Services", "sector": "Energy", "portfolio": False, "alert_threshold": -3},

    "LLY": {"name": "Eli Lilly", "industry": "Pharma / GLP-1", "sector": "Healthcare", "portfolio": False, "alert_threshold": -3},
    "UNH": {"name": "UnitedHealth Group", "industry": "Health Insurance", "sector": "Healthcare", "portfolio": False, "alert_threshold": -3},
    "ABBV": {"name": "AbbVie", "industry": "Pharma", "sector": "Healthcare", "portfolio": False, "alert_threshold": -3},
    "PFE": {"name": "Pfizer", "industry": "Pharma", "sector": "Healthcare", "portfolio": False, "alert_threshold": -3},
    "MRK": {"name": "Merck & Co", "industry": "Pharma", "sector": "Healthcare", "portfolio": False, "alert_threshold": -3},
    "USO": {"name": "United States Oil Fund", "industry": "Oil ETF", "sector": "Energy / Macro", "portfolio": False, "alert_threshold": -3},
    #"DXY": {"name": "US Dollar Index", "industry": "Dollar Index", "sector": "Macro", "portfolio": False, "alert_threshold": 1},
    "DXY": {
    "name": "US Dollar Index",
    "industry": "Dollar Index",
    "sector": "Macro",
    "portfolio": False,
    "alert_threshold": -1
    }
}


FAST_SYMBOLS = [
    "QQQ", "SPY", "SMH", "SOXX", "HYG", "JNK", "TLT", "VIXY", "USO", "DXY",
    "MU", "MRVL", "COHR", "NVDA", "AMD",
    "PANW", "CRWD"
]

SLOW_SYMBOLS = [
    "ARM", "INTC", "LAC", "NOK",
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NFLX",
    "WMT", "KO", "PEP", "PG", "JNJ", "MCD", "COST", "CL",
    "JPM", "BAC", "WFC", "GS", "MS", "C",
    "XOM", "CVX", "COP", "SLB",
    "LLY", "UNH", "ABBV", "PFE", "MRK",
    "ZS", "NET", "FTNT", "CHKP", "OKTA", "CYBR",
    "AVGO", "ASML", "AMAT", "LRCX", "KLAC", "QCOM", "TSM",
    "WDC", "STX", "ANET", "VRT", "SMCI", "ETN", "CEG", "VST"
]

PREMARKET_SYMBOLS = [
    "QQQ",
    "SMH",
    "MU",
    "MRVL",
    "COHR",
    "NVDA",
    "AMD"
]

EARNINGS_WATCHLIST = [
    # Portfolio
    "MU",
    "MRVL",
    "COHR",
    "NVDA",
    "AMD",
    "ARM",
    "INTC",

    # AI Chips
    "AVGO",
    "QCOM",
    "TSM",
    "ASML",
    "AMAT",
    "LRCX",
    "KLAC",
    "WDC",
    "STX",

    # AI Infrastructure
    "ANET",
    "VRT",
    "SMCI",
    "ETN",
    "CEG",
    "VST",

    # AI Software
    "MSFT",
    "GOOGL",
    "META",
    "AMZN",

    # Cybersecurity
    "PANW",
    "CRWD",
    "ZS",
    "NET",
    "FTNT",
    "CYBR",

    # Datacenter / Enterprise
    "ORCL",
    "IBM",
    "SNOW",
    "PLTR",

    # Networking
    "CSCO",
    "NOK",

    # Others
    "TSLA",
    "AAPL",

    "CRM",
    "DDOG",
    "DELL",
    "HPE",
    "JNPR",
    "MDB",
]

PORTFOLIO_SYMBOLS = [
    "MU",
    "MRVL",
    "COHR",
    "NVDA",
    "AMD",
    "ARM",
    "INTC",
]

MACRO_SYMBOLS = [
    "VIXY",   # fear
    "TLT",    # rates
    "DXY",    # dollar
    "USO",    # energy
    "HYG",    # credit
    "JNK",    # credit
    "QQQ",    # growth
    "SOXX"    # semis
]