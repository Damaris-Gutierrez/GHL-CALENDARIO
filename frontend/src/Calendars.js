import { useEffect, useState } from "react";

export default function Calendars() {
  const [calendars, setCalendars] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/ghl/calendars/")
      .then((res) => res.json())
      .then((data) => setCalendars(data.calendars || []))
      .catch(console.error);
  }, []);

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h5 className="card-title mb-3"><strong>Calendarios Disponibles</strong></h5>
        {calendars.length > 0 ? (
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead>
                <tr>
                  <th style={{ backgroundColor: " darkorange", color: "white" , fontFamily: "sans-serif", padding: "1rem 0"}}>ID</th>
                  <th style={{ backgroundColor: " darkorange", color: "white" , fontFamily: "sans-serif", padding: "1rem 0"}}>Nombre</th>
                  <th style={{ backgroundColor: " darkorange", color: "white" , fontFamily: "cursive", padding: "1rem 0"}}>Activo</th>
                </tr>
              </thead>
              <tbody>
                {calendars.map((cal) => (
                  <tr key={cal.id}>
                    <td>{cal.id}</td>
                    <td>{cal.name}</td>
                    <td>{cal.status === "Activo" ? "✅" : "❌"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <p className="text-center text-muted">
            No hay calendarios disponibles
          </p>
        )}
      </div>
    </div>
  );
}
