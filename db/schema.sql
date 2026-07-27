PRAGMA foreign_keys = ON;

-- Companies
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT NOT NULL UNIQUE,
    sector TEXT
);

CREATE TABLE IF NOT EXISTS profitandloss (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    year INTEGER NOT NULL,

    sales REAL,

    net_profit REAL,

    eps REAL,

    UNIQUE(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);


CREATE TABLE IF NOT EXISTS balancesheet (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    year INTEGER NOT NULL,

    assets REAL,

    liabilities REAL,

    UNIQUE(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

-- Cash Flow
CREATE TABLE IF NOT EXISTS cashflow (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    operating_cf REAL,
    investing_cf REAL,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);
-- Analysis
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER,
    analysis TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Documents
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    document_url TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Pros and Cons
CREATE TABLE IF NOT EXISTS prosandcons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Sectors
CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sector_name TEXT UNIQUE
);

-- Stock Prices
CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    trade_date TEXT,
    close_price REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Peer Groups
CREATE TABLE IF NOT EXISTS peer_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    peer_company TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);