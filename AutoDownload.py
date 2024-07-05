from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

numbers = [
    "1313450343",
    "618436646",
    "1297733465",
    "1260175659",
    "1199463928",
    "1178914597",
    "1321009617",
    "1313314809",
    "1337325148",
    "1294722736",
    "1316909834"
]

login_page = 'https://www.mdsystem.com/imdsnt/faces/login'
download_dir = './downloads'

def run(playwright):
    load_dotenv()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    print("Login ...")

    # Open the login page
    page.goto(login_page)

    # Log in to the website
    page.fill('#pt1\\:itUserId\\:\\:content', os.getenv("MDS_username"))
    page.fill('#pt1\\:itPassword\\:\\:content', os.getenv("MDS_password"))
    page.press('#pt1\\:itPassword\\:\\:content', 'Enter')

    # Wait for the login to complete
    page.wait_for_selector('#pt1\\:pt_ctbToolBarInbound\\:\\:popArea', timeout=35000)

    # Navigate to the download page
    page.click('#pt1\\:pt_ctbToolBarInbound\\:\\:popArea')
    page.click('#pt1\\:pt_cmiSearchInboxB')

    # Wait for the ID field to be present
    page.wait_for_selector('#pt1\\:dcCmds\\:sfIbLU\\:itModuleId\\:\\:content', timeout=35000)

    for number in numbers:
        # Input the file ID and search
        page.fill('#pt1\\:dcCmds\\:sfIbLU\\:itModuleId\\:\\:content', number)
        page.press('#pt1\\:dcCmds\\:sfIbLU\\:itModuleId\\:\\:content', 'Enter')

        # Wait for the search results to load
        page.wait_for_selector('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:tResult\\:0\\:cName', timeout=5000)

        # Perform the three clicks to download the file
        page.click('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:ctbMenT')
        page.wait_for_selector('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:tResult\\:pt_mReports', timeout=3000)
        page.click('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:tResult\\:pt_mReports')
        page.wait_for_selector('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:tResult\\:pt_cmiReport', timeout=3000)
        with page.expect_download() as download_info:
            page.click('#pt1\\:dcCmds\\:sfIbLU\\:pc2\\:tResult\\:pt_cmiReport')
        download = download_info.value
        download_path = os.path.join(download_dir, f"MDSReport_{number}.pdf")
        download.save_as(download_path)
        print(f"Finish Download ID: {number}")

    # Logout and Close the browser
    page.click('#pt1\\:pt_mFile')
    page.click('#pt1\\:pt_mLogoff')
    browser.close()
    print("Finish!")

with sync_playwright() as playwright:
    run(playwright)
