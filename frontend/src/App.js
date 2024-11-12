import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import OverviewPage from './Pages/Overview/OverviewPage';
import Dashboard from './Pages/DashboardPage/Dashboard';
import Webpage from './Pages/officialwebpage/body';
import UserMng from './Pages/DashboardPage/DashContent/UserMng';
import ComplianceReports from './Pages/DashboardPage/DashContent/ComplianceReports';
import Regulations from './Pages/DashboardPage/DashContent/Regulations';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<OverviewPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/webpage" element={<Webpage />} />
        <Route path="/user-management" element={<UserMng />} />
        <Route path="/compliance-reports" element={<ComplianceReports />} />
        <Route path="/regulation-overview" element={<Regulations isOpen={true} onClose={() => {}} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;