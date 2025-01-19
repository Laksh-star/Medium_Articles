"use client";

import React, { useState } from "react";
import { CopilotPopup } from "@copilotkit/react-ui";

export const dynamic = "force-dynamic"; // Force dynamic rendering if needed

interface BookItem {
  id: string;
  volumeInfo: {
    title: string;
    authors?: string[];
    description?: string;
    imageLinks?: {
      thumbnail?: string;
    };
  };
}

export default function BookExplorerPage() {
  const [query, setQuery] = useState("");
  const [books, setBooks] = useState<BookItem[]>([]);
  const [favorites, setFavorites] = useState<BookItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  // -- TOGGLE FAVORITE LOGIC --
  function toggleFavorite(book: BookItem) {
    const index = favorites.findIndex((f) => f.id === book.id);
    if (index === -1) {
      // Not a favorite yet => add
      setFavorites((prev) => [...prev, book]);
    } else {
      // Already in favorites => remove
      setFavorites((prev) => prev.filter((fav) => fav.id !== book.id));
    }
  }

  // Check if a book is currently in favorites
  function isFavorited(bookId: string): boolean {
    return favorites.some((f) => f.id === bookId);
  }

  async function handleSearch(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!query.trim()) return;

    setError("");
    setIsLoading(true);
    setBooks([]);

    try {
      const res = await fetch(
        `https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(query)}`
      );
      if (!res.ok) {
        throw new Error(`Request failed with status ${res.status}`);
      }
      const data = await res.json();

      if (data.items) {
        setBooks(data.items);
      } else {
        setError("No results found.");
      }
    } catch (err: any) {
      console.error("Error searching books:", err);
      setError("An error occurred while searching for books.");
    } finally {
      setIsLoading(false);
    }
  }

  // Summarize search results & favorites for the Copilot instructions
  function generateBooksSummary() {
    let summary = "";

    if (books.length > 0) {
      summary += "\nCurrent search results:\n";
      summary += books
        .map((b) => {
          const title = b.volumeInfo.title;
          const authors = b.volumeInfo.authors?.join(", ") ?? "Unknown author(s)";
          return `• "${title}" by ${authors}`;
        })
        .join("\n");
    } else {
      summary += "\nNo current search results.\n";
    }

    if (favorites.length > 0) {
      summary += "\n\nUser's favorites:\n";
      summary += favorites
        .map((f) => {
          const title = f.volumeInfo.title;
          const authors = f.volumeInfo.authors?.join(", ") ?? "Unknown author(s)";
          return `• "${title}" by ${authors}`;
        })
        .join("\n");
    } else {
      summary += "\n\nFavorites list is empty.\n";
    }

    return summary;
  }

  return (
    <main style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      {/* TOP BAR */}
      <header
        style={{
          background: "#333",
          color: "#fff",
          padding: "1rem",
          marginBottom: "1rem",
        }}
      >
        <h1 style={{ margin: 0 }}>Enhanced Book Explorer</h1>
        <p style={{ margin: "0.5rem 0 0" }}>
          Search for books & manage favorites. Ask the AI about them in the chat!
        </p>
      </header>

      {/* FAVORITES AT THE TOP */}
      <section style={{ padding: "0 1rem" }}>
        <h2 style={{ marginTop: 0 }}>My Favorites</h2>
        {favorites.length === 0 ? (
          <p>No favorite books yet. Try adding some from the search results below!</p>
        ) : (
          <ul style={{ listStyle: "none", paddingLeft: 0 }}>
            {favorites.map((fav) => {
              const { title, authors } = fav.volumeInfo;
              return (
                <li
                  key={fav.id}
                  style={{
                    marginBottom: "0.5rem",
                    borderBottom: "1px solid #eee",
                    paddingBottom: "0.5rem",
                  }}
                >
                  <strong>{title}</strong>
                  {authors && ` by ${authors.join(", ")}`}

                  <button
                    onClick={() => toggleFavorite(fav)}
                    style={{
                      marginLeft: "1rem",
                      padding: "0.3rem 0.6rem",
                      background: "#f33",
                      color: "#fff",
                      border: "none",
                      borderRadius: "4px",
                      cursor: "pointer",
                    }}
                  >
                    Remove from Favorites
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </section>

      {/* SEARCH SECTION */}
      <section style={{ padding: "0 1rem", marginTop: "1rem" }}>
        <form onSubmit={handleSearch} style={{ marginBottom: "1rem" }}>
          <input
            type="text"
            placeholder="Enter a title or author"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={{ padding: "0.5rem", width: 300 }}
          />
          <button
            type="submit"
            style={{
              marginLeft: "0.5rem",
              padding: "0.5rem 1rem",
              background: "#0070f3",
              color: "#fff",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            Search
          </button>
        </form>

        {isLoading && <p>Searching books...</p>}
        {error && <p style={{ color: "red" }}>{error}</p>}

        {/* SEARCH RESULTS */}
        {books.length > 0 && (
          <>
            <h2>Search Results</h2>
            <ul style={{ listStyle: "none", paddingLeft: 0 }}>
              {books.map((book) => {
                const { title, authors, imageLinks, description } = book.volumeInfo;
                const favorited = isFavorited(book.id);

                return (
                  <li
                    key={book.id}
                    style={{
                      marginBottom: "1rem",
                      borderBottom: "1px solid #eee",
                      paddingBottom: "1rem",
                    }}
                  >
                    <h3>{title}</h3>
                    {authors && (
                      <p>
                        <strong>Authors:</strong> {authors.join(", ")}
                      </p>
                    )}
                    {imageLinks?.thumbnail && (
                      <img
                        src={imageLinks.thumbnail}
                        alt={`${title} cover`}
                        style={{ maxWidth: 80, marginBottom: "0.5rem" }}
                      />
                    )}
                    {description && (
                      <p>{description.substring(0, 200)}...</p>
                    )}

                    {/* TOGGLE FAVORITE BUTTON */}
                    <button
                      onClick={() => toggleFavorite(book)}
                      style={{
                        padding: "0.4rem 0.8rem",
                        background: favorited ? "#f33" : "#ffa500",
                        color: "#fff",
                        border: "none",
                        borderRadius: "4px",
                        cursor: "pointer",
                      }}
                    >
                      {favorited ? "Remove from Favorites" : "Add to Favorites"}
                    </button>
                  </li>
                );
              })}
            </ul>
          </>
        )}
      </section>

      {/* COPILOTKIT POPUP */}
      <CopilotPopup
        instructions={`
          You are assisting the user in discovering and managing books. 
          The user can search for new books, toggle favorites, etc.
          Here's the current session data:
          ---
          ${generateBooksSummary()}
          ---
          If the user references these books or authors, provide helpful info. 
          If a book isn't in the summary, rely on general knowledge.
        `}
        labels={{
          title: "Book Assistant",
          initial: "Ask about your favorite or new books!",
        }}
      />
    </main>
  );
}
