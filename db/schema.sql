PRAGMA foreign_keys = ON;

----------------------------------------------------
-- COMPANIES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS companies (

    company_id INTEGER PRIMARY KEY,

    company_name TEXT NOT NULL,

    ticker TEXT NOT NULL UNIQUE,

    sector TEXT

);

----------------------------------------------------
-- PROFIT & LOSS
----------------------------------------------------

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

----------------------------------------------------
-- BALANCE SHEET
----------------------------------------------------

CREATE TABLE IF NOT EXISTS balancesheet (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    year INTEGER NOT NULL,

    assets REAL,

    liabilities REAL,

    equity REAL,

    UNIQUE(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- CASH FLOW
----------------------------------------------------

CREATE TABLE IF NOT EXISTS cashflow (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    year INTEGER NOT NULL,

    operating_cf REAL,

    investing_cf REAL,

    financing_cf REAL,

    UNIQUE(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- ANALYSIS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    year INTEGER,

    summary TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- DOCUMENTS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS documents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    annual_report_url TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- PROS & CONS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS prosandcons (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    pros TEXT,

    cons TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- SECTORS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS sectors (

    sector_name TEXT PRIMARY KEY

);

----------------------------------------------------
-- STOCK PRICES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS stock_prices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER NOT NULL,

    date TEXT,

    close_price REAL,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)

);

----------------------------------------------------
-- PEER GROUPS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS peer_groups (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ticker TEXT,

    peer_group TEXT

);

----------------------------------------------------
-- INDEXES
----------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_company
ON companies(company_id);

CREATE INDEX IF NOT EXISTS idx_pnl_company
ON profitandloss(company_id);

CREATE INDEX IF NOT EXISTS idx_bs_company
ON balancesheet(company_id);

CREATE INDEX IF NOT EXISTS idx_cf_company
ON cashflow(company_id);

CREATE INDEX IF NOT EXISTS idx_analysis_company
ON analysis(company_id);

CREATE INDEX IF NOT EXISTS idx_documents_company
ON documents(company_id);

CREATE INDEX IF NOT EXISTS idx_stock_company
ON stock_prices(company_id);

CREATE INDEX IF NOT EXISTS idx_peer_ticker
ON peer_groups(ticker);