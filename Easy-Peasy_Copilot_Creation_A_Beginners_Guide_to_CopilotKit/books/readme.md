# Book Explorer with CopilotKit

A simple **Next.js** application that lets users:

- **Search for books** using the Google Books API,  
- **Toggle** favorites (add/remove) in a top “My Favorites” section,  
- **Ask an AI assistant** for info about the books or authors they’ve found.

Built with [CopilotKit](https://docs.copilotkit.ai) to provide a floating chat interface powered by AI.

---

## Features

1. **Book Search**  
   Enter an author, title, or keyword to fetch results from the Google Books API.  
2. **Favorites**  
   Quickly “Add to Favorites” or “Remove from Favorites” from the list. Favorites always appear at the top for easy access.  
3. **AI Chat**  
   A floating chat box powered by CopilotKit. It “knows” which books you’ve searched and favorited, so you can ask for suggestions, summaries, or more details.  

---

## Getting Started

### Prerequisites
- **Node.js** (16 or higher recommended)  
- **npm** or **yarn** (package manager)  
- A Copilot Cloud **public API key** if using the hosted CopilotKit backend. (Otherwise, see the [CopilotKit docs](https://docs.copilotkit.ai) for self-hosting.)

### Installation

1. **Clone** this repository:
   ```bash
   git clone https://github.com/your-username/book-explorer-copilotkit.git
   cd book-explorer-copilotkit
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```
   or
   ```bash
   yarn
   ```
   This grabs both the Next.js dependencies and CopilotKit libraries.

3. **Set Your CopilotKit API Key**  
   - In `.env.local` (create it if missing), add:
     ```bash
     NEXT_PUBLIC_COPILOT_API_KEY=your_public_api_key
     ```
   - Confirm you’re using `NEXT_PUBLIC_COPILOT_API_KEY` in `layout.tsx` (or wherever `<CopilotKit>` is initialized). For example:
     ```tsx
     <CopilotKit publicApiKey={process.env.NEXT_PUBLIC_COPILOT_API_KEY}>
       {children}
     </CopilotKit>
     ```
4. **Development Server**:
   ```bash
   npm run dev
   ```
   or
   ```bash
   yarn dev
   ```
   Then open [http://localhost:3000](http://localhost:3000).

5. **Production Build** (optional):
   ```bash
   npm run build
   npm run start
   ```
   or
   ```bash
   yarn build
   yarn start
   ```

---

## Project Structure

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

- **layout.tsx**: Wraps the entire app in `<CopilotKit>` so the AI chat is available site-wide.  
- **page.tsx**: A home page or landing page.  
- **books/page.tsx**: The main “Book Explorer” logic—searching, listing results, toggling favorites, and a floating CopilotKit chat box.

---

## Usage

1. **Favorites at the Top**: The “My Favorites” section is always visible. If you have none, you’ll see a friendly message.  
2. **Searching**: Type a book title, author, or keyword into the search bar, then click **Search**. The page will display up to 10 Google Books results.  
3. **Toggle Favorites**: Click the **Add to Favorites** or **Remove from Favorites** button to manage your personal list.  
4. **AI Chat**: Click the floating icon in the bottom-right corner to open a chat powered by CopilotKit. Ask about your books, authors, or any general topic.

---

## Customizing

1. **Styling**  
   - Update inline styles in `books/page.tsx` or override CopilotKit’s default styles in your own CSS.  
2. **Prompt Engineering**  
   - Adjust the `instructions` prop in the `<CopilotPopup>` to refine how the AI responds.  
3. **Data Persistence**  
   - Currently, favorites are stored in React state. For a real production app, integrate a database or serverless API route.  

---

## Known Issues / Limitations

1. **CopilotKit** uses large language models, so answers may contain inaccuracies or “hallucinations.”  
2. **Google Books API** may rate-limit excessive queries.  
3. Favorites are not saved beyond the current session (no database). Refreshing will lose them.


---

## License

[MIT](LICENSE) – Feel free to use, modify, and distribute. See the `LICENSE` file for details.

---

## Acknowledgments

- [Next.js](https://nextjs.org/) for the React framework.  
- [CopilotKit](https://docs.copilotkit.ai) for the floating AI chat integration.  
- [Google Books API](https://developers.google.com/books/) for the book data.  

Enjoy exploring books with AI assistance!
