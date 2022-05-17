import json
import yt_dlp
import tkinter as tk
import requests

# User basic functionalities
class User():
    max_results = 100

    def __init__(self, username, bearerToken):
        from pytwitter import Api

        self.__username = username
        self.__bearerToken = bearerToken
        self.__api    = Api(bearer_token=self.__bearerToken)
        self.__user   = self.__api.get_user(username=self.__username)
        self.__userId = self.__user.data.id

    def lastTweets(self):
        return self.__api.get_timelines(user_id=self.__userId, max_results=self.max_results)

# App funcionalities
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.frm = tk.Frame(self)
        self.frm.grid()
        self.bearer_token = bearer_token

        tk.Label(self.frm, text="Username: ").grid(column=0, row=0)
        self.username_entry = tk.Entry(self.frm)
        self.username_entry.grid(column=1, row=0)
        
        tk.Label(self.frm, text="N# of videos:").grid(column=0, row=1)
        self.video_results_entry = tk.Entry(self.frm)
        self.video_results_entry.grid(column=1, row=1)
        
        tk.Button(self.frm, text="Download", command=self.download).grid(column=0, row=2)
        tk.Button(self.frm, text="Quit", command=self.quit).grid(column=1, row=2)
        
        self.status_bar = tk.Label(self.frm, text="Ready")
        self.status_bar.grid(column=0, row=3)

    def download(self):
        self.status_bar_update('Getting user data.')

        if self.username_entry.get() != '':
            self.username = self.username_entry.get()
        else:
            self.status_bar_update('Username is empty!')
            return
        if self.video_results_entry.get() != '':
            self.video_results = int(self.video_results_entry.get())
        else:
            self.video_results = 1
            self.status_bar_update('N# of videos is empty! Using 1 as default.')

        self.user = User(self.username, self.bearer_token)

        self.status_bar_update("Getting last tweets...")

        self.status_bar_update('Downloading...')

        counter     = 0
        base_string = 'https://t.co/'
        ytdl        = yt_dlp.YoutubeDL()

        for tweet in self.user.lastTweets().data:
            text = tweet.text
            if base_string in text:
                counter += 1
                self.status_bar_update('Downloading video '+str(counter)+'.')
                index = text.split(base_string)[1]
                url=base_string+index
                if 'video' in requests.get(url).url:
                    ytdl.download([url])
                    if counter == self.video_results:
                        break
        if counter == 0:
            self.status_bar_update('Finished! No video found!')
        elif counter == 1:
            self.status_bar_update('Finished! 1 video downloaded!')
        else:
            self.status_bar_update("Finished! " + str(counter) + ' videos downloaded!')
        

    def status_bar_update(self, msg):
        self.status_bar['text'] = msg
        self.status_bar.update()

if __name__ == '__main__':
    # Preloads configuration file
    configFilePath = 'config.json'
    with open(configFilePath, 'r') as configFile:
        configText = configFile.read()
        configJson = json.loads(configText)
        bearer_token = configJson['bearer_token']

    # Creates Tk object and App
    root = tk.Tk()
    root.title('Video Downloader')
    myapp = App(root)

    # Runs main loop
    myapp.mainloop()