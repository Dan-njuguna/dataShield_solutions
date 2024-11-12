
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ComplianceReports = () => {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const response = await axios.get('http://localhost:8000/compliance/compliance-reports/', {
          headers: {
            Authorization: 'Token 4af02030ad9fe551a32e72afdddf66b385dc5e78',
          },
        });

        console.log('Response data:', response.data);

        // Check if response.data.results is an array
        if (Array.isArray(response.data.results)) {
          setReports(response.data.results);
        } else {
          throw new Error('Response data is not an array');
        }
      } catch (error) {
        console.error('Error fetching reports:', error);
        setError(error.response ? error.response.data : error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchReports();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Compliance Reports</h2>
      {reports.length > 0 ? (
        <ul>
          {reports.map(report => (
            <li key={report.id}>{report.title || report.generated_at || 'Report'}</li>
          ))}
        </ul>
      ) : (
        <div>No reports found.</div>
      )}
    </div>
  );
};

export default ComplianceReports;
