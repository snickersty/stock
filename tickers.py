#TICKERS SOURCE

tickers_list = ['AAPL','ABNB','AFRM', 'AI','AR', 'ARCB', 'BABA', 'BIGC', 'BIIB', 'BMY',
'CAT','CCL','COST',  'COIN', 'COUR', 'CRWD', 'CVS',
'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCN','DOCS', 'DRVN', 'ENPH','EURN','FCX','GDRX', 'GM','GOOGL',
'IAC','ICE','INMD','KOS', 'MAR', 'MAXR', 'MQ','MSFT','MTDR', 'MTTR','MU',
'NET', 'NKE', 'NFLX', 'NVDA', 'NTR','OKTA','ONON', 'PFE', 'PG', 'PLTR','PYPL',
'QCOM','RDWR','REGN', 'RIVN', 'RBLX','RPRX', 'SBLK','SEER','SEMR', 'SPCE', 'SQ',
'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'UPST','WST',
'V', 'VALE', 'VLDR', 'XMTR', 'ZM','ZKIN',
'SPXS','GLD','HDV','SPYD','VYM','MGV','DIA','QQQ','VAW','VDE','VT','VTI','VWO','XLE',
'EWY','TUR','ACWI','GLIN','FXI','EWZ','EWW','EPOL',
'CADJPY=X','GBPJPY=X','EURJPY=X','SGDJPY=X','HKDJPY=X','JPY=X','CNYJPY=X']

tickers_list_analysis = ['AAPL','AFRM', 'AI','AR', 'BABA', 'BIGC', 'BIIB', 'BMY',
'COST', 'CAT', 'COIN', 'COUR', 'CRWD', 'CVS',
'DDOG', 'DAL', 'DIS', 'DKNG', 'DOCS', 'DRVN', 'GDRX','GOOGL',
'EURN', 'GM', 'IAC','ICE','KOS', 'MAR', 'MAXR','MQ', 'MSFT',
'NKE', 'NFLX', 'OKTA', 'PFE', 'PG', 'PYPL',
'REGN', 'RBLX','RPRX', 'SEER', 'SPCE', 'SBLK',
'TSLA', 'TSM', 'TTD', 'TWLO', 'U', 'UPST',
'V', 'VALE', 'VLDR', 'XMTR', 'ZM','ZKIN']

tickers1 = {'^TNX':'金利','^DJI':'ダウ','^IXIC':'ナスダック', '^GSPC':'SP500',
            '^RUT':'ラッセル', '^VIX':'VIX指数','^N225':'日経', 'GLD':'GOLD', 'JPY=X':'USD/JPY', 'BTC-USD':'BTC'}

tickers2 = {'VIS':'資本財', 'VAW':'素材', 'VCR':'一般消費財'
 , 'VDE':'エネルギー', 'VPU':'公益', 'VDC':'生活必需品'
 , 'VHT':'ヘルスケア', 'VOX':'電気通信', 'VFH':'金融'
 , 'VGT':'情報技術', 'VNQ':'不動産'}

tickers3 = {'DIA':'ダウ', 'QQQ':'ナスダック', 'VTI':'トータル',
            'IWM':'ラッセル20','IWB':'ラッセル10',
            'CLOU':'クラウド', 'VUG':'大型グロース','VBK':'小型グロース',
            'MGV':'大型バリュー', 'VBR':'小型バリュー','VT':'全世界', 'VWO':'新興国',
            'SPYD':'高配当', 'HDV':'高配当', 'VYM':'高配当'
}

tickers4 = {'MSFT':'マイクロソフト', 'AAPL':'アップル', 'FB':'フェイスブック',
            'GOOGL':'グーグル', 'AMZN':'アマゾン', 'TSLA':'テスラ', 'NVDA':'エヌビディア'
 }

tickers5 = {'AFRM':'Affirm', 'BIGC':'BIGC', 'COUR':'Coursera',
 'CRWD':'Crowdstrike', 'DDOG':'DataDog', 'DLO':'Dlocal', 'DOCN':'DigitalOcean','DOCS':'Doximity',
 'MQ':'Marqeta','OKTA':'OKTA','PLTR':'Palantir', 'RBLX':'Roblox','RIVN':'Rivian', 'SQ':'Block',
 'TTD':'Tradedesk','UPST': 'Upstart'}
#, 'RBLX':'Roblox', 'XMTR':'Xometry'
categ = {'指数＋その他':tickers1, 'セクター':tickers2, 'ETF':tickers3, 'GAFAMTN':tickers4,  '小型・近年IPO':tickers5}
