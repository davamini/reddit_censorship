from google_sheets_upload import scan_reddit_censorship
import schedule

schedule.every().day.at("11:10").do(scan_reddit_censorship)

while True:
    schedule.run_pending()
