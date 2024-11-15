import React, { useState, useEffect } from 'react';
import Sidenavbar from '../../components/Sidenavbar';
import Topnavbar from '../../components/Topnavbar';
//import AuditLogs from '../../Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs';
import './dashindex.css';
import DSlogo from '../../img/DSlogo.png';
//import axios from 'axios';
import Reportspop from './DashContent/ReportsPop/Reportspop';

function Dashboard() {
  


  return (
    <>
      <Topnavbar className="Topnavbar" />
      <div className="dash-container">
        <div className="cont-col-1"><Sidenavbar /></div>
        <div className="cont-col-2">
          <img src={DSlogo} alt="Logo" className="logo" />
          <p>Welcome to Data Shield</p>
          <Reportspop/>

         
        </div>
      </div>
    </>
  );
}

export default Dashboard;
