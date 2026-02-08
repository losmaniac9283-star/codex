import React, { useEffect, useMemo, useState } from 'react';
import './index.css';

function App() {
  const [companies, setCompanies] = useState([]);
  const [search, setSearch] = useState('');
  const [sortAsc, setSortAsc] = useState(true);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/companies')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Request failed: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        setCompanies(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(`Error fetching data: ${err.message}`);
        setLoading(false);
      });
  }, []);

  const sortedAndFiltered = useMemo(() => {
    const filtered = companies.filter((company) =>
      company.name.toLowerCase().includes(search.toLowerCase())
    );

    return [...filtered].sort((a, b) => (sortAsc ? a.diff - b.diff : b.diff - a.diff));
  }, [companies, search, sortAsc]);

  return (
    <div className="app">
      <h1>Top Companies Stock Dashboard</h1>

      <input
        type="text"
        placeholder="Search companies..."
        value={search}
        onChange={(event) => setSearch(event.target.value)}
      />

      {loading && <p>Loading companies...</p>}
      {error && <p className="error">{error}</p>}

      {!loading && !error && (
        <table>
          <thead>
            <tr>
              <th>Company (Ticker)</th>
              <th>Price</th>
              <th>200-wk SMA</th>
              <th className="sortable" onClick={() => setSortAsc((prev) => !prev)}>
                Diff (%) {sortAsc ? '▲' : '▼'}
              </th>
            </tr>
          </thead>
          <tbody>
            {sortedAndFiltered.map((company) => (
              <tr key={company.ticker}>
                <td>
                  {company.name} ({company.ticker})
                </td>
                <td>{company.price.toFixed(2)}</td>
                <td>{company.sma200.toFixed(2)}</td>
                <td>{company.diff.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
