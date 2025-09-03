import { useState } from "react";

export default function PingGHL() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePing = async () => {
    setLoading(true);
    setStatus(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/ghl/ping/"); // 👈 URL completa
      const data = await res.json();

      if (res.ok) {
        setStatus({ success: true, message: "✅ Conexión exitosa con GHL" });
      } else {
        setStatus({
          success: false,
          message: `❌ Error: ${data.message || data.error}`,
        });
      }
    } catch (error) {
      setStatus({ success: false, message: `❌ Error: ${error.message}` });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-body">
        <h5 className="card-title"><strong>Probar Conexión con GHL</strong> </h5>
        <button
          onClick={handlePing}
          disabled={loading}
          className="btn btn-primary"
        >
          {loading ? "En espera de conexion..." : "Conectar"}
        </button>

        {status && (
          <div
            className={`alert mt-3 ${
              status.success ? "alert-success" : "alert-danger"
            }`}
            role="alert"
          >
            {status.message}
          </div>
        )}
      </div>
    </div>
  );
}
