import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { PhonemicKeyboard } from "./features/phonemic-keyboard/pages/phonemic-keyboard";
import PrivacyPolicy from "./pages/PrivacyPolicy";
import "./App.css";

function App() {
  return (
    <Router>
      <div className={"App"}>
        <Routes>
          <Route 
            path="/" 
            element={
              <>
                <h1 className="header">Phonemic Keyboard</h1>
                <PhonemicKeyboard />
              </>
            } 
          />
          <Route path="/privacy-policy" element={<PrivacyPolicy />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
