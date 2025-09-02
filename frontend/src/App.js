import PingGHL from "./PingGHL";
import Calendars from "./Calendars";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="container my-5">
      <h1 className="text-center mb-5">Integración con GHL</h1>
      <PingGHL />
      <Calendars />
    </div>
  );
}

export default App;
