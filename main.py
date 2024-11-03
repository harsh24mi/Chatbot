import tkinter as tk    #for gui
from tkinter import scrolledtext #for scrollbar widget
import google.generativeai as genai #for Generative AI function
import datetime #for date and time
import smtplib # for  sending email
import webbrowser #for opening websites
import os # for system level operations
import requests #for making request to external APIs

# Creditionals
source = 'the-times-of-india' #  news source
News_API_KEY = '7336385df27b4a6f9ec35e2b94ca51ab'#  news API key
url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={News_API_KEY}'  
weather_api_key = "5f6c1fa428f74bd8b95171144240311"# weather  API key
genai.configure(api_key="AIzaSyAMN9jcjdpIHgeHzfqcSBSsL17YrQdcY48")  #gemini api

#Fuctions

#greet user based on time
def greet():
    hour = int(datetime.datetime.now().hour)# get current time
    if hour >= 0 and hour < 12:
        add_message("bot","Good Morning!") # morning
    elif hour >= 12 and hour < 18:
        add_message("bot","Good Afternoon!") #afternoon
    else:
        add_message("bot","Good Evening!")#eveneing
    add_message("bot","Hi, this is Buzz, how can I help you?")

#function to send emails
def sendEmail(to, content):
    try:
        # Establish connection to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls() # Secure the connection
        server.login('harshrajbro@gmail.com', 'fgnh pfnn turg elye') # Login to the email account 
        server.sendmail('harshrajbro@gmail.com', to, content) # Send the email
        server.close() # Close the connection 
    except Exception as e:
        print(f"Error sending email: {e}") # Print error

# Function to get Recipient email for sending email
def send_email_input(event=None):
    recipient = entry.get() #get email by user input
    to = recipient 

    add_message("bot", "What should I say?") # add a bot message on chatbox field
    entry.delete(0, tk.END) # clear the entry box

    
    send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0,
                            command=lambda: send_email_content(to)) #directing send button to  send_email_content function

    send_button.grid(row=0, column=1, padx=10)  # place send button on grid

    entry.bind("<Return>", lambda event: send_email_content(to))  # bind enter key to send_email_content function


# Function to get content for sending email
def send_email_content(to, event=None):
    content = entry.get() #get content by user input
    if not content:  
        add_message("bot", "Message cannot be empty!")# add a bot message on chatbox field
        return
    sendEmail(to, content) # calling sendEmail function with email and content as a parameter
    add_message("bot", "Email has been sent.")# add a bot message on chatbox field

    entry.delete(0, tk.END)# clear the entry box

    send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0,
                            command=lambda: send_message)  #directing send button to  send_message function

    send_button.grid(row=0, column=1, padx=10)   # place send button on grid

    entry.bind("<Return>", send_message)   # bind enter key to send_message function

#function to open websites
def open_website(url):
    name = url
    if not url.startswith(('http://', 'https://')): #check  if url is valid

        if url.startswith('www.'): #check  if url starts with www.
            url = 'https://' + url  #if  yes, add https:// to the starting of url
        else:
            url = 'https://www.' + url   #if  no, add https://www. to the starting of url
    add_message("bot",f"Opening {name}") # add a bot message on chatbox field

    webbrowser.open(url)  #open the url in default browser


# Function to get website name input
def website_input(event=None):
    url = entry.get() #get website name by user input
    if not url:
        add_message("bot", "Please enter a website!")  # add a bot message on chatbox field

        return
    open_website(url)  # Call the function to open the website

    entry.delete(0, tk.END)# clear the entry box
    send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0,
                            command=send_message)   #directing send button to  send_message function

    send_button.grid(row=0, column=1, padx=10)    # place send button on grid

    entry.bind("<Return>", send_message)    # bind enter key to send_message function

 # function to get weather deatils
def weather(city):
    city = entry.get() # get city name by user input
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no"
    response = requests.get(url)  # send get request to the url

    if response.status_code == 200:  # check if response is 200 , (error code 200 = OK)
        data = response.json() #  convert response to json format
        current = data['current']  # get current weather data from json format
        temp_c = current['temp_c']   # get temperature in celsius
        condition = current['condition']['text']   # get weather condition
        wind_kph = current['wind_kph']   # get wind speed in km/h

        add_message("bot","Weather in :" + city)  # add a bot message on chatbox field
        add_message("bot", f"Temperature: {str(temp_c)}°C") 
        add_message("bot","Condition: " + condition)
        add_message("bot", "Wind Speed: " + str(wind_kph) + " km/h")
    else:
        add_message("bot","Error fetching weather data")
    
#  Function to get city name for website
def weather_input(event = None):
    city=entry.get()  # get city name by user input
    if not url:
        add_message("bot", "Please enter a city!")   # add a bot message on chatbox field
        return
    weather(city)   # Call the function to get weather details with city name as parameter
    entry.delete(0, tk.END)  # clear the entry box
    send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0,
                            command=send_message)
    send_button.grid(row=0, column=1, padx=10)
    entry.bind("<Return>", send_message)

#function to get gemini responses
def get_gemini_response(user_input):
    generation_config = {
        "temperature": 1,# Controls the randomness of the output; higher values make output more random
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192, # Maximum number of tokens in the output
        "response_mime_type": "text/plain", # the response is returned as plain text
    }   # configuration for the model

    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",    # Specify the model 
        generation_config=generation_config,
    )
    
    chat_session = model.start_chat(
        history=[{
            "role": "user",
            "parts": [user_input],
        }]
    )
    
       # Send the user input and get a response
    response = chat_session.send_message(user_input)
    
    return response.text    # Return the response text received from the model

def bot_response(query):
    if 'send mail' in query:   # check if the query is send mail
        try:
            add_message("bot", "To whom?")
            send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0, command=send_email_input)
            send_button.grid(row=0, column=1, padx=10)
            entry.bind("<Return>", send_email_input)
        except Exception as e:
            add_message("bot", "Sorry, I was not able to send the mail.")

    elif 'open website' in query:    # check if the query is open website

        try:
            add_message("bot","Which website do you want to open?")  
            send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0, command=website_input) #  Call the function to get website details with website name as parameter

            send_button.grid(row=0, column=1, padx=10) #  add a button to the input frame

            entry.bind("<Return>", website_input) #  bind the return key to the function

        except Exception as e:
            add_message("bot", "Sorry, I was not able to open website")
    elif 'weather' in query:     # check if the query is weather

        try:
            add_message("bot","of which city")  
            send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0, command=weather_input)
            send_button.grid(row=0, column=1, padx=10)
            entry.bind("<Return>", weather_input)
        except Exception as e:
            add_message("bot", "Sorry, I was not able to open website")
    
    # Some custom messages for bot to interact with users
    elif 'how are u' in query:
        add_message("bot",'i am good , what about u')
    elif 'How are you' in query:
        add_message("bot","I am fine. What about you")
    elif 'when you were born' in query:
        add_message("bot","I am still in development")
    elif 'where you were born' in query:
        add_message("bot","In School of computer engineering campus")  
    elif 'what do you like to do' in query:
        add_message("bot","Serving my master is the most enjoyable thing for me")
    elif 'good morning buzz' in query :
        add_message("bot","good morning, master have a beautifu day ahead")
    elif 'good afternoon buzz' in query :
        add_message("bot","good afternoon, master")  
    elif 'good evening buzz' in query :
        add_message("bot","good evening, master")  
    elif 'good night buzz' in query :
        add_message("bot","good night, master")
    elif 'who is your favourite superhero' in query :
        add_message("bot","Iron man, love you 3000")
    elif 'which is your favourite movie' in query :
        add_message("bot","I don't watch movies very often but Interstellar is my favourite")

    #system commands
    elif 'shutdown' in query or 'turn off' in query:  # check if the query is shutdown or turn off
        add_message("bot","Shutting down")
        print('shutting down.....')   # print the shutdown message
        os.system(r"shutdown /s /t 1")   # shutdown the system after 1 second

    elif 'restart' in query:   # check if the query is restart
        add_message("bot","Restarting")
        print('restarting.....')
        os.system(r"shutdown /r /t 1")    # restart the system after 1 second

    elif 'sleep' in query:      # check if the query is sleep
        add_message("bot","Sleep mode activated")
        print('sleep mode.....')
        os.system(r"rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    # put the system to sleep

    elif 'lock' in query or 'lock screen' in query:   # check if the query is lock or lock screen
        add_message("bot","Locking screen")
        print('locking screen.....')
        os.system(r"rundll32.exe user32.dll,LockWorkStation") #  lock the screen

    elif 'news' in query:    # check if the query is news
            response = requests.get(url)       # get the news from the url
            news_data = response.json()         #  convert response to json format
            if news_data['status'] == 'ok':      # check if the status is ok

                for i, article in enumerate(news_data['articles'][:5], 1):  #for loop for printing top 5 articles
                    add_message("bot",f"{i}. {article['title']}")
            else:
                add_message("bot","Error fetching news:", news_data['message'])

    else: # if the query is not in the list of commands gemini give responses
        gemini_response=get_gemini_response(query)  # get the response from gemini
        add_message("bot",gemini_response)

def send_message(event=None): 
    user_input = entry.get()   # get the user input from the entry field

    if user_input:
        add_message("user", user_input)
        entry.delete(0, tk.END)

        bot_response(user_input)   # call the bot_response function with the user input as parameter


def add_message(role, message):
    if role == "user":
        chat_window.config(state=tk.NORMAL)  
        chat_window.insert(tk.END, f"You: {message}\n", "user")
        chat_window.config(state=tk.DISABLED)  
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"BuZz: {message}\n", "bot")
        chat_window.config(state=tk.DISABLED)

    chat_window.yview(tk.END)  

# Gui setup
root = tk.Tk() # Initialize a tkinter window
root.title("Buzz ChatBot")  # Set the title of the window
root.geometry("500x600")   # Set the size of the window
root.config(bg="#2c3e50")    # Set the background color of the window

chat_window = scrolledtext.ScrolledText(root, bg="#2c3e50", fg="white", font=("Helvetica", 14), wrap=tk.WORD, state=tk.DISABLED)   # Create a scrolled text widget
chat_window.pack(pady=(10, 0), padx=10, fill=tk.BOTH, expand=True)   # Pack the scrolled text widget

chat_window.tag_configure("user", foreground="#4caf50", font=("Helvetica", 12, "bold"))   # Configure the user message color and font
chat_window.tag_configure("bot", foreground="#ffffff", font=("Helvetica", 12, "bold"))    # Configure the bot message color and font

input_frame = tk.Frame(root, bg="#34495e")    # Create a frame for the input field
input_frame.pack(fill=tk.X, pady=10)    # Pack the input frame

entry = tk.Entry(input_frame, width=40, font=("Helvetica", 14), bg="#ffffff", fg="#34495e", bd=0, highlightthickness=0)    # Create an entry field for user input
entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")    # Grid the entry field

send_button = tk.Button(input_frame, text="→", font=("Helvetica", 14), bg="#4caf50", fg="white", bd=0, highlightthickness=0, command=send_message)     # Create a send button
send_button.grid(row=0, column=1, padx=10)    # Create a send button and pack it

entry.bind("<Return>", send_message)   # Bind the enter key to the send_message function
input_frame.grid_columnconfigure(0, weight=1)    # Make the input field expandable

greet()    # Call the greet function to display the message
root.mainloop()    # Start the main loop of the application

