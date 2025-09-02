import { useState } from "react";

export default function PingGHL() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePing = async () => {
    setLoading(true);
    setStatus(null);

    try {
      const res = await fetch("/ghl/ping/");
      const data = await res.json();

      if (res.ok) {
        setStatus({ success: true, message: "✅ Conexión exitosa con GHL" });
      } else {
        setStatus({ success: false, message: `❌ Error: ${data.message || data.error}` });
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
        <h5 className="card-title">Probar Conexión con GHL</h5>
        <button
          onClick={handlePing}
          disabled={loading}
          className="btn btn-primary"
        >
          {loading ? "Conectando..." : "Probar Conexión"}
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
