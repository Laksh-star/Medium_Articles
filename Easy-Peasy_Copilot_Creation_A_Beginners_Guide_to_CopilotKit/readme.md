This folder contains book explorer app that needs to be copied under /app after copilotkit installation.
Refer the folliwing to install copilotkit:
1. https://docs.copilotkit.ai/quickstart
2. https://medium.com/@LakshmiNarayana_U/easy-peasy-copilot-creation-a-beginners-guide-to-copilotkit-ceab6a815bcc?sk=d5ad76cdce70571031445929b44a2867
   
**Sample Project Structure**

```
├─ app/
│   ├─ layout.tsx          # Global layout (includes CopilotKit provider)
│   ├─ page.tsx            # Optional home page
│   ├─ books/
│   │   └─ page.tsx        # The main "Book Explorer" page
│   ├─ globals.css         # Global CSS
├─ components/             # (Optional) any shared components
├─ public/                 # Static assets
├─ .env.local.example      # Example env file
├─ package.json
├─ README.md
└─ ...
```
