import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [joke, setJoke] = useState("Loading joke...")

  useEffect(() => {
    // Rely on Server-Sent Events (SSE) instead of setInterval polling.
    // The server waits for Celery task to update the database, then pushes to React.
    const eventSource = new EventSource('http://localhost:8000/api/joke/stream/');

    eventSource.onmessage = (event) => {
      setJoke(event.data);
    };

    eventSource.onerror = (error) => {
      console.error("EventSource failed:", error);
      eventSource.close();
    };

    return () => eventSource.close();
  }, []);

  return (
    <>
      <section id="center">

        <div>
          <h1>Jokes on you!</h1>
          <p>
            {joke}
          </p>
        </div>
      </section>

     </>
  )
}
export default App
