import { useState } from "react";
import Login from "./Login";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  if (!token) {
    return <Login onLogin={setToken} />;
  }

  return (
    <div>
      <h1>Bienvenido</h1>
      <p>Token guardado en localStorage</p>
      <button
        onClick={() => {
          localStorage.removeItem("token");
          setToken(null);
        }}
      >
        Logout
      </button>
    </div>
  );
}

export default App;
