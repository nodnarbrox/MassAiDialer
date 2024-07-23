🤖 ☎️ WholesaleVa
Summary

A full stack app for interruptible, low-latency, and near-human quality AI phone calls built from stitching LLMs, speech understanding tools, text-to-speech models, and Twilio’s phone API.

The following components have been implemented and wrangled together in streaming fashion to achieve the tasks of low-latency and interruptible AI calls:

    ☎️ Phone Service: Makes and receives phone calls through a virtual phone number (Twilio).
    🗣️ Speech-to-Text Service: Converts the caller’s voice to text (Whisper by OpenAI) and understands speech patterns such as when the user is done speaking and interruptions to facilitate interruptibility.
    🤖 Text-to-text LLM: Understands the phone conversation, can make “function calls,” and steers the conversation towards accomplishing specific tasks specified through a “system” message (Hugging Face GPT-Neo).
    🔈 Text-to-Speech Service: Converts the LLM response to high-quality speech (Coqui TTS).
    ⚙️ Web Server: A FastAPI-based web server that provides endpoints for:
        Answering calls using Twilio’s Markup Language (Twilio ML).
        Enabling audio streaming to/from Twilio through a per-call WebSocket.
        Interacting with the basic Streamlit web UI.
    📊 Frontend UI: Simple Streamlit frontend to initiate/end calls and view call progress in real-time in a browser.
    📋 CRM Integration: Integrates with Podio to manage conversations and log call summaries.
    🛡️ Compliance: Checks against the U.S. National Do Not Call (DNC) list before making calls.
    🔍 Skip Tracing: Uses SkipEngine to perform skip tracing when only partial contact information is available.

Installation
1. Install dependencies:

(You might want to create a Python Virtual Environment to minimize the chance of conflicts.)

pip install -r requirements.txt

3. Configure .env file

Make a copy of the .env.example file and rename it to .env. Then set the required credentials and configurations.
# Server Configuration
SERVER=your_local_server
PORT=3000

# Twilio Credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token

# AI Services Configuration
TTS_SERVICE=local_coqui
LLM_SERVICE=local_gpt_neo

# CRM Integration
PODIO_APP_ID=your_podio_app_id
PODIO_ACCESS_TOKEN=your_podio_access_token

# Compliance
DNC_API_URL=https://api.ftc.gov/v0/dnc-complaints?api_key=your_dnc_api_key

# Skip Trace Service (SkipEngine)
SKIP_TRACE_SERVICE=https://api.skipengine.com/append
SKIP_TRACE_API_KEY=your_skipengine_api_key

# When you call a number, what should the caller ID be?
APP_NUMBER=your_app_number

# When UI launches, what number should it call by default
YOUR_NUMBER=your_number

# When a call needs to be transferred, what number should it be transferred to?
TRANSFER_NUMBER=your_transfer_number

# AI Configuration
SYSTEM_MESSAGE="You are a representative called Sarah from El Camino Hospital. Your goal is to obtain a prior authorization for a patient called John Doe for a knee surgery. Be brief in your correspondence."
INITIAL_MESSAGE="Hello, my name is Sarah, and I'm calling from El Camino Hospital. I need to discuss a prior authorization for a patient. Could you please direct me to the appropriate representative?"

# Should calls be recorded? (this has legal implications, so be careful)
RECORD_CALLS=false
4. Configure the Twilio end point

Assuming that you have created a Twilio phone number and installed Twilio's CLI, run the following to configure Twilio to use your app's endpoint:

sql

twilio phone-numbers:update YOURNUMBER --voice-url=https://NGROKURL/incoming

5. Run the FastAPI server

python app.py

6. Run the Frontend server

bash

streamlit ui/streamlit_app.py

Contribution

Contributions are welcome! Please feel free to submit a Pull Request.
License

Copyright JessicaCodes, 2024

Code shared under MIT License
Acknowledgement

This project would not have been possible without this great TypeScript example from Twilio Labs. GPT-Neo, Whisper by OpenAI, and Coqui TTS also provided ample help in writing parts of this code base 🦾
