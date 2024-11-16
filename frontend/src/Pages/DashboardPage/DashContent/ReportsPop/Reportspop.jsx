import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Reportspop({ organizationName }) {
  const [generalreports, setGeneralreports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const reportsPerPage = 3; // Number of reports per page

  useEffect(() => {
    const fetchGeneralreports = async () => {
      setLoading(true);
      setError(null);
      console.log('Fetching reports for organizationName:', organizationName);

      try {
        const response = await axios.get('http://localhost:8000/report/scheduled-reports/', {
          headers: {
            Authorization: 'Token a59dffe6150c2dc30be516b6a819b560bf72b8d6',
          },
          params: {
            organization_name: organizationName,
          },
        });

        console.log('Full response:', response.data);

        if (Array.isArray(response.data.results)) {
          const uniqueReports = Array.from(new Set(response.data.results.map(report => report.id)))
            .map(id => response.data.results.find(report => report.id === id));
          setGeneralreports(uniqueReports);
        } else {
          throw new Error('Response data is not an array');
        }
      } catch (error) {
        console.error('Error fetching reports:', error);
        if (error.response) {
          console.error('Response status:', error.response.status);
          console.error('Response data:', error.response.data);
          setError(error.response.data.detail || error.message);
        } else {
          setError(error.message);
        }
      } finally {
        setLoading(false);
      }
    };

    if (organizationName) {
      fetchGeneralreports();
    } else {
      setLoading(false);
    }
  }, [organizationName]);

  // Calculate total pages
  const totalPages = Math.ceil(generalreports.length / reportsPerPage);

  // Get current reports for the current page
  const indexOfLastReport = currentPage * reportsPerPage;
  const indexOfFirstReport = indexOfLastReport - reportsPerPage;
  const currentReports = generalreports.slice(indexOfFirstReport, indexOfLastReport);

  // Handle pagination
  const nextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(prev => prev + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(prev => prev - 1);
    }
  };

  const goToAllReports = () => {
    setCurrentPage(1);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div style={{ color: 'red' }}>Error: {error}</div>;

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h2 style={{ textAlign: 'center' }}>Scheduled Compliance Reports</h2>
      {currentReports.length > 0 ? (
        <ul style={{ listStyleType: 'none', padding: '0' }}>
          {currentReports.map(report => (
            <li key={report.id} style={{ marginBottom: '20px', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
              <h3>Report Type: {report.report_type}</h3>
              <p><strong>Organization:</strong> {report.organization?.name || 'N/A'}</p>
              <p><strong>Scheduled Time:</strong> {new Date(report.schedule_time).toLocaleString() || 'N/A'}</p>
              <p><strong>Email Recipients:</strong> {report.email_recipients || 'N/A'}</p>
            </li>
          ))}
        </ul>
      ) : (
        <div>No reports found for this organization. Please check if the organization name is correct and has scheduled reports.</div>
      )}

      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
        <button onClick={prevPage} disabled={currentPage === 1} style={buttonStyle}>
          Previous
        </button>
        <button onClick={nextPage} disabled={currentPage === totalPages} style={buttonStyle}>
          Next
        </button>
        <button onClick={goToAllReports} style={buttonStyle}>
          All
        </button>
      </div>

      <div style={{ textAlign: 'center', marginTop: '20px' }}>
        <p>
          Page {currentPage} of {totalPages}
        </p>
      </div>
    </div>
  );
}

// Basic button styling
const buttonStyle = {
  padding: '10px 15px',
  border: 'none',
  borderRadius: '5px',
  backgroundColor: '#007BFF',
  color: 'white',
  cursor: 'pointer',
  transition: 'background-color 0.3s',
};

buttonStyle[':hover'] = {
  backgroundColor: '#0056b3',
};

buttonStyle[':disabled'] = {
  backgroundColor: '#ccc',
  cursor: 'not-allowed',
};