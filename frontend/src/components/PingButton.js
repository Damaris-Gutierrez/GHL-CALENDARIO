import { useState } from "react";
import api from "../services/api";

function PingTest() {
  const [data, setData] = useState(null);

  const handlePing = async () => {
    try {
      const res = await api.get("/ghl/ping/");
      setData(res.data);
    } catch (error) {
      setData({ error: error.message });
    }
  };

  return (
    <div>
      <button onClick={handlePing}>Probar Conexión con GHL</button>
      <pre>{data && JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default PingTest;
