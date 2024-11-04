//the AuditLogs compnentsreceives the properties in line five from the paent component that mananges th state which is the Topnavbar
import React from 'react';

function AuditLogs({ content, isOpen, onClose, data }) {
  if (!isOpen) return null;

  const columnStyle = {
    width: '75%',
    backgroundColor: '#f2f2f2',
    padding: '20px 40px',
  };

  return (
    <div className="side-column" style={columnStyle}>
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
}

export default AuditLogs;
