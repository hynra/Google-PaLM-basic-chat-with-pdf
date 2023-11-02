# Google-PaLM-basic-chat-with-pdf
Basic QnA app with PDF using Google PaLM

* Blog post: https://hynra.medium.com/ai-chat-pdf-dengan-google-palm-model-80fd3204e5ca

* Create Google PaLM API key here: https://makersuite.google.com/app/apikey

* Create `.env` file

* put API KEY  `GOOGLE_API_KEY=<your-api-key-here>` in `.env`

* For embedding, use `models/embedding-gecko-001`

* For text generation, use `models/text-bison-001`

* Available models (v1beta3):

```
"models/chat-bison-001",
"models/text-bison-001",
"models/embedding-gecko-001",
```

* run project: `streamlit.cmd run .\main.py`

* Demo

![image info](https://raw.githubusercontent.com/hynra/Google-PaLM2-basic-chat-with-pdf/master/ss/1.png)
