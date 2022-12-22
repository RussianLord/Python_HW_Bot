from datetime import datetime 
def show_time():
    showT = datetime.now().strftime('%H:%M')
    return showT
show_time()