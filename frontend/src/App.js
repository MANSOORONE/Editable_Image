import './App.css';
import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);

  const uploadImage = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/process-image",
      formData
    );

    alert("SVG Created: " + res.data.svg_file);
  };

  return (
    <div>
      <h1>Image → Editable SVG</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadImage}>Convert</button>
    </div>
  );
}

export default App;
