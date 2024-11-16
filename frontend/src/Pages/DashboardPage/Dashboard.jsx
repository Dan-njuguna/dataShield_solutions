import React from 'react';
import Sidenavbar from '../../components/Sidenavbar';
import Topnavbar from '../../components/Topnavbar';
import './dashindex.css';
import DSlogo from '../../img/DSlogo.png';
import Reportspop from './DashContent/ReportsPop/Reportspop';

function Dashboard() {
  const organizationName = "Cannon Ltd"; // Define the organization name

  return (
    <>
      <Topnavbar className="Topnavbar" />
      <div className="dash-container">
        <div className="cont-col-1"><Sidenavbar /></div>
        <div className="cont-col-2">
          <img src={DSlogo} alt="Logo" className="logo" />
          
          <Reportspop organizationName={organizationName} /> {/* Pass the organization name as a prop */}

        </div>
      </div>
    </>
  );
}

export default Dashboard;