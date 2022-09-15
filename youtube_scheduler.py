import schedule
import time
import webbrowser

def job():
    # 定期実行させたい処理
    print('Opening motivative video on YouTube...')
    webbrowser.open("https://www.youtube.com/watch?v=j1WTP4Q7KGE&ab_channel=AlexBecker%27sChannel")
    
def main():
    # 10分ごと
    # schedule.every(1).minutes.do(job)

    # 2時間ごと
    # schedule.every(2).hours.do(job)

    # 毎日09時
    schedule.every().day.at("9:00").do(job)

    # 毎週月曜日
    # schedule.every().monday.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)

main()