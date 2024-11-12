//the AuditLogs compnentsreceives the properties in line five from the paent component that mananges th state which is the Topnavbar
import React from 'react';
import axios from 'axios';
import {useState, useEffect} from 'react';
function AuditLogs({ content, isOpen, onClose, data }) {
const [audits, setAudits] = useState([])
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
useEffect(() => {

   // Function to fetch data from the backend for AuditLogs
  const fetchAuditlogsData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/audit/audit_log/', {
        headers: {
          Authorization: 'Token 4af02030ad9fe551a32e72afdddf66b385dc5e78',
        },
      });

      console.log('Response data:', response.data);

      // Check if response.data.results is an array
      if (Array.isArray(response.data.results)) {
        setAudits(response.data.results);
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
  fetchAuditlogsData();
}, []);

  if (!isOpen) return null;

  const columnStyle = {
    width: '75%',
    backgroundColor: '#f2f2f2',
    padding: '20px 40px',
  };
 
 

  // Use useEffect to fetch data when AuditLogs is opened


  return (
    <div>
      <h2>Compliance Reports</h2>
      {audits.length > 0 ? (
        <ul>
          {audits.map(report => (
            <li key={audits.id}>{audits.title || audits.generated_at || 'Report'}</li>
          ))}
        </ul>
      ) : (
        <div>No reports found.</div>
      )}
    </div>
  );
};
    
    

export default AuditLogs;
