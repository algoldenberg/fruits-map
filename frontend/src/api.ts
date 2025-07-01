const BASE_URL = "http://127.0.0.1:8000";

export interface Place {
  id: number;
  name: string;
  address: string;
  lat: number;
  lon: number;
  category_id: number;
  description?: string;
  photo?: string;
}

export async function fetchPlaces(): Promise<Place[]> {
  const response = await fetch(`${BASE_URL}/places/places/`);
  if (!response.ok) {
    throw new Error("Failed to fetch places");
  }
  return await response.json();
}
