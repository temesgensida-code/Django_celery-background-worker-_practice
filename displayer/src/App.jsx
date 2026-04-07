import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [joke, setJoke] = useState("Loading joke...")

  useEffect(() => {
    const fetchJoke = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/joke/');
        const data = await response.json();
        setJoke(data.joke);
      } catch (error) {
        console.error("Error fetching joke:", error);
      }
    };

    fetchJoke(); // initial fetch
    const interval = setInterval(fetchJoke, 5000); // fetch every 5 seconds

    return () => clearInterval(interval);
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
