import { useEffect, useState } from "react";

export default function Calendars() {
  const [calendars, setCalendars] = useState([]);

  useEffect(() => {
    fetch("/ghl/calendars/")
      .then((res) => res.json())
      .then((data) => setCalendars(data.calendars || []))
      .catch(console.error);
  }, []);

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h5 className="card-title mb-3">Calendarios Disponibles</h5>
        {calendars.length > 0 ? (
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-light">
                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Activo</th>
                </tr>
              </thead>
              <tbody>
                {calendars.map((cal) => (
                  <tr key={cal.id}>
                    <td>{cal.id}</td>
                    <td>{cal.name}</td>
                    <td>{cal.isActive ? "✅" : "❌"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <p className="text-center text-muted">No hay calendarios disponibles</p>
        )}
      </div>
    </div>
  );
}
