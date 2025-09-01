function ErrorMessage({ code, message }) {
  if (!code && !message) return null;

  return (
    <div style={{ color: "red", marginTop: "10px" }}>
      {code === 401 || code === 403 ? (
        <p>❌ No autorizado. Revisa tu token o permisos.</p>
      ) : (
        <p>❌ Error: {message || "Ha ocurrido un error inesperado."}</p>
      )}
    </div>
  );
}

export default ErrorMessage;
