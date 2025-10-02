Document loaders
DocumentLoaders load data into the standard LangChain Document format.

Each DocumentLoader has its own specific parameters, but they can all be invoked in the same way with the .load method. An example use case is as follows:

from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(
    ...  # <-- Integration specific parameters here
)
data = loader.load()

Webpages
The below document loaders allow you to load webpages.

See this guide for a starting point: How to: load web pages.

Document Loader	Description	Package/API
Web	Uses urllib and BeautifulSoup to load and parse HTML web pages	Package
Unstructured	Uses Unstructured to load and parse web pages	Package
RecursiveURL	Recursively scrapes all child links from a root URL	Package
Sitemap	Scrapes all pages on a given sitemap	Package
Spider	Crawler and scraper that returns LLM-ready data.	API
Firecrawl	API service that can be deployed locally.	API
Docling	Uses Docling to load and parse web pages	Package
Hyperbrowser	Platform for running and scaling headless browsers, can be used to scrape/crawl any site	API
AgentQL	Web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt	API
Oxylabs	Web intelligence platform enabling the access to various data sources.	API
PDFs
The below document loaders allow you to load PDF documents.

See this guide for a starting point: How to: load PDF files.

Document Loader	Description	Package/API
PyPDF	Uses `pypdf` to load and parse PDFs	Package
Unstructured	Uses Unstructured's open source library to load PDFs	Package
Amazon Textract	Uses AWS API to load PDFs	API
MathPix	Uses MathPix to load PDFs	Package
PDFPlumber	Load PDF files using PDFPlumber	Package
PyPDFDirectry	Load a directory with PDF files	Package
PyPDFium2	Load PDF files using PyPDFium2	Package
PyMuPDF	Load PDF files using PyMuPDF	Package
PyMuPDF4LLM	Load PDF content to Markdown using PyMuPDF4LLM	Package
PDFMiner	Load PDF files using PDFMiner	Package
Upstage Document Parse Loader	Load PDF files using UpstageDocumentParseLoader	Package
Docling	Load PDF files using Docling	Package
Cloud Providers
The below document loaders allow you to load documents from your favorite cloud providers.

Document Loader	Description	Partner Package	API reference
AWS S3 Directory	Load documents from an AWS S3 directory	❌	S3DirectoryLoader
AWS S3 File	Load documents from an AWS S3 file	❌	S3FileLoader
Azure AI Data	Load documents from Azure AI services	❌	AzureAIDataLoader
Azure Blob Storage Container	Load documents from an Azure Blob Storage container	❌	AzureBlobStorageContainerLoader
Azure Blob Storage File	Load documents from an Azure Blob Storage file	❌	AzureBlobStorageFileLoader
Dropbox	Load documents from Dropbox	❌	DropboxLoader
Google Cloud Storage Directory	Load documents from GCS bucket	✅	GCSDirectoryLoader
Google Cloud Storage File	Load documents from GCS file object	✅	GCSFileLoader
Google Drive	Load documents from Google Drive (Google Docs only)	✅	GoogleDriveLoader
Huawei OBS Directory	Load documents from Huawei Object Storage Service Directory	❌	OBSDirectoryLoader
Huawei OBS File	Load documents from Huawei Object Storage Service File	❌	OBSFileLoader
Microsoft OneDrive	Load documents from Microsoft OneDrive	❌	OneDriveLoader
Microsoft SharePoint	Load documents from Microsoft SharePoint	❌	SharePointLoader
Tencent COS Directory	Load documents from Tencent Cloud Object Storage Directory	❌	TencentCOSDirectoryLoader
Tencent COS File	Load documents from Tencent Cloud Object Storage File	❌	TencentCOSFileLoader
Social Platforms
The below document loaders allow you to load documents from different social media platforms.

Document Loader	API reference
Twitter	TwitterTweetLoader
Reddit	RedditPostsLoader
Messaging Services
The below document loaders allow you to load data from different messaging platforms.

Document Loader	API reference
Telegram	TelegramChatFileLoader
WhatsApp	WhatsAppChatLoader
Discord	DiscordChatLoader
Facebook Chat	FacebookChatLoader
Mastodon	MastodonTootsLoader
