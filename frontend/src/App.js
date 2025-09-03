import PingGHL from "./PingGHL";
import Calendars from "./Calendars";
import Footer from "./Footer"
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

function App() {
  return (
    <div className="container my-5">
      <h1 className="text-center mb-5" > 👩‍⚕️📝 Integración con GHL</h1>
      <main>
        <div className="btn-conexion">
          <PingGHL />
        </div>
        <div className="Calendars">
            <Calendars />
        </div>
        </main>
      <Footer/>
    </div>
  );
}

export default App;
