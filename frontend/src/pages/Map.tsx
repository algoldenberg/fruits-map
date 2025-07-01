import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { useEffect, useState } from 'react';
import { fetchPlaces } from '../api';
import type { Place } from '../api';


// 🔧 Фикс для иконок Leaflet
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: "https://unpkg.com/leaflet@1.9.3/dist/images/marker-icon-2x.png",
  iconUrl: "https://unpkg.com/leaflet@1.9.3/dist/images/marker-icon.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.3/dist/images/marker-shadow.png",
});

export default function MapPage() {
  const [places, setPlaces] = useState<Place[]>([]);

  useEffect(() => {
    fetchPlaces().then(setPlaces);
  }, []);

  return (
    <div className="h-screen w-screen flex">
      {/* Sidebar */}
      <div className="w-72 bg-white text-black shadow-md p-4 flex flex-col">
        <h2 className="text-xl font-bold mb-4">Fruits Map</h2>
        <div className="flex-1">
          <p className="text-sm">🔍 Фильтры и поиск</p>
          {/* Тут будут фильтры */}
        </div>
        <div className="text-xs text-gray-500 mt-4">© 2025 Fruits Map</div>
      </div>

      {/* Map */}
      <div className="flex-1">
        <MapContainer
          center={[32.0853, 34.7818]}
          zoom={8}
          scrollWheelZoom={true}
          className="h-full w-full"
        >
          <TileLayer
            attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {places.map((marker) => (
            <Marker key={marker.id} position={[marker.lat, marker.lon]}>
              <Popup>
                <b>{marker.name}</b>
                <br />
                {marker.address}
              </Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>
    </div>
  );
}
