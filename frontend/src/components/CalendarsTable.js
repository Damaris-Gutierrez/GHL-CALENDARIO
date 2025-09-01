import { useState } from "react";
import api from "../services/api";
import Loader from "./Loader";
import ErrorMessage from "./ErrorMessage";

function CalendarsTable() {
  const [calendars, setCalendars] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const loadCalendars = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await api.get("/ghl/calendars/");
      const data = res.data.calendars || res.data || [];
      setCalendars(data);
    } catch (err) {
      setCalendars([]);
      setError({
        code: err.response?.status,
        message: err.response?.data?.error || err.message,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ margin: "20px" }}>
      <button onClick={loadCalendars}>Cargar Calendarios</button>

      {loading && <Loader />}
      {error && <ErrorMessage code={error.code} message={error.message} />}

      {(!loading && !error && calendars.length === 0) && (
        <p>No existen calendarios disponibles.</p>
      )}

      {(!loading && !error && calendars.length > 0) && (
        <table border="1" cellPadding="8" style={{ marginTop: "10px", borderCollapse: "collapse" }}>
          <thead style={{ background: "#f0f0f0" }}>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {calendars.map((cal) => (
              <tr key={cal.id}>
                <td>{cal.id}</td>
                <td>{cal.name}</td>
                <td>{cal.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default CalendarsTable;
