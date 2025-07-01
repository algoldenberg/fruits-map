import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MapPage from './pages/Map';
import Place from './pages/Place';

export default function App() {
  return (
    <Router>
      <nav className="bg-gray-900 p-4 flex gap-4">
        <Link to="/" className="text-white hover:underline">Map</Link>
        <Link to="/place" className="text-white hover:underline">Place</Link>
      </nav>
      <Routes>
        <Route path="/" element={<MapPage />} />
        <Route path="/place" element={<Place />} />
      </Routes>
    </Router>
  );
}
