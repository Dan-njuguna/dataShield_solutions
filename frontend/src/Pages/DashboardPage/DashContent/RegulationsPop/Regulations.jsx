import React from 'react'
//import summaryData from '../../../../data'
import './Rindex.css'

const Regulations= ({content, isOpen, onClose, data }) =>{
  if (!isOpen) return null;

  return (
    <div className="side-column">
      <div className={`AuditLogs ${isOpen ? 'open' : ''}`}>
        <button onClick={onClose}>Close</button>
      </div>
      <div>{content.status}</div>
      <h2>{content.title}</h2>

      {/* Display fetched data here */}
      {data ? (
        <div>
          <h3>Audit Logs</h3>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      ) : (
        <p>Loading data...</p>
      )}
      </div>
  );
};
export default Regulations;