import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import OverviewPage from './Pages/Overview/OverviewPage';
import Dashboard from './Pages/DashboardPage/Dashboard';
import Webpage from './Pages/officialwebpage/body';
import ComplianceReports from './Pages/DashboardPage/DashContent/ComplianceReports';
import Regulations from './Pages/DashboardPage/DashContent/Regulations/Regulations';
import AuditLogs from './Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs';
import PolicyPop from './Pages/DashboardPage/DashContent/PolicyPop/PolicyPop';
import NotFound from './Pages/NotFound.jsx'; 
import { AuthProvider } from './components/context/AuthContext.js'; // Import AuthProvider

function App() {
  return (
    <AuthProvider> {/* Wrap your application with AuthProvider */}
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<OverviewPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/webpage" element={<Webpage />} />
          
          <Route path="/compliance-reports" element={<ComplianceReports />} />
          <Route path="/audit_log" element={<AuditLogs />} />
          <Route path="/regulation-overview" element={<Regulations />} />
          <Route path="/policy" element={<PolicyPop />} />
          <Route path="*" element={<NotFound />} /> {/* Catch-all route for 404 */}
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;