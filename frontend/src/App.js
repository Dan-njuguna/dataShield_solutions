import React from 'react';
import OverviewPage from './Pages/Overview/OverviewPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './Pages/DashboardPage/Dashboard';
 import Webpage from './Pages/officialwebpage/body';
 import LoginPage from './Pages/Login/Login';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<OverviewPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/webpage" element = {<Webpage/>}></Route>
        <Route path = "/login" element = {<LoginPage/>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
