<a href="https://github.com/SafetImamovic/ForgeAI/blob/main/README.md"><img src="https://img.shields.io/badge/Lang-EN-red" alt="Lang EN" height="23"></a> <a href="https://github.com/SafetImamovic/ForgeAI/blob/main/README.bs.md"><img src="https://img.shields.io/badge/Lang-BS-blue" alt="Lang BS" height="24"></a>
<a href="https://safetimamovic.github.io/ForgeAI"><img src="https://img.shields.io/badge/Project%20Documentation-black" alt="Project Documentation" height="28"></a>


# ForgeAI

**ForgeAI** is a VST plugin (currently in prototype as a website) designed for generating **[MIDI](https://en.wikipedia.org/wiki/MIDI)** files based on user-input textual data.

It utilizes advanced AI models to convert textual descriptions into MIDI format, making the music creation process more intuitive and efficient.

## Technical Description

### Architecture

- **User Interface**: Intuitive interface for entering textual prompts.
- **Authentication**: Secure authentication system and subscription management.
- **Backend Server**: Processes user queries, communicates with **Google Gemini**, and manages data.
- **Google Gemini**: External API for generating music from textual descriptions.
- **Conversion Algorithm**: Converts JSON responses from the **Google Gemini** API into MIDI format.

### MIDI File Generation Process

- **User Input**: User enters a textual prompt in the plugin's UI.
- **Authentication**: Validates user subscription.
- **Server Processing**: Query is sent to the server and forwarded to the **Google Gemini** API.
- **Response Generation**: **Google Gemini** API returns a JSON response based on the prompt.
- **Conversion to MIDI**: Algorithm converts JSON into a MIDI file.
- **File Download**: User downloads the MIDI file for use in a **[DAW](https://en.wikipedia.org/wiki/Digital_audio_workstation)**.

### Technologies

- **Frontend**: HTML, CSS, JavaScript
- **Backend + Database**: Django (Python)
- **API Integration**: Google Gemini
- **Payment**: Stripe
- **Algorithms**: Custom algorithms for converting JSON to MIDI


## Conclusion

**ForgeAI** represents advanced technology in the field of music production, enabling users to intuitively and efficiently generate music.

By using textual prompts and advanced AI models, ForgeAI simplifies the music creation process, providing high quality and flexibility.

This project has the potential to significantly enhance how music professionals and enthusiasts create music, making it more accessible and efficient.