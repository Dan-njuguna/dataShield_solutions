import React, { useState, useEffect } from 'react';
import Sidenavbar from '../../components/Sidenavbar';
import Topnavbar from '../../components/Topnavbar';
import AuditLogs from '../../Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs';
import './dashindex.css';
import DSlogo from '../../img/DSlogo.png';
import axios from 'axios';

function Dashboard() {
  const [selectedContent, setSelectedContent] = useState('');
  const [data, setData] = useState(null); // State to hold fetched data for AuditLogs

  const handleTopnavbarContent = (pageContent) => {
    setSelectedContent(pageContent);
  };

  const closeSideColumn = () => {
    setSelectedContent('');
  };

  // Function to fetch data from the backend for AuditLogs
  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/logs/');
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Use useEffect to fetch data when AuditLogs is opened
  useEffect(() => {
    if (selectedContent.title === 'AuditLogs') {
      fetchData();
    }
  }, [selectedContent]);

  return (
    <>
      <Topnavbar className="Topnavbar" onLinkClick={handleTopnavbarContent} />
      <div className="dash-container">
        <div className="cont-col-1"><Sidenavbar /></div>
        <div className="cont-col-2">
          <img src={DSlogo} alt="" className="logo" />
          <p>Welcome to data shield</p>

          {/* Render the selected content here */}
          {selectedContent ? (
            <div>
              <h2>{selectedContent.title}</h2>
              <p>{selectedContent.content}</p>
              <button className="close-btn" onClick={closeSideColumn}>Close</button>

              {/* Render AuditLogs only when selected */}
              {selectedContent.title === 'AuditLogs' && (
                <AuditLogs content={selectedContent} isOpen={!!selectedContent} onClose={closeSideColumn} data={data} />
              )}
            </div>
          ) : (
            <p></p>
          )}
        </div>
      </div>
    </>
  );
}

export default Dashboard;
