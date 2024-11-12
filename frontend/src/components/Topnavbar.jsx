import React from 'react';
import { NavLink } from 'react-router-dom';
import '../Pages/DashboardPage/dashindex.css';
import PolicyPop from '../Pages/DashboardPage/DashContent/PolicyPop/PolicyPop';
import AuditLogs from '../Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs';

function Topnavbar({ onLinkClick }) {
  return (
    <div className='Topnavbar'>
      <ul>
        <li>
          <NavLink to='/regulation-overview' activeClassName='active'>
            Regulations Overview
          </NavLink>
        </li>
        <li>
          <NavLink 
            to='#' 
            onClick={() => onLinkClick({ title: 'Audit Logs', content: <AuditLogs /> })}>
            Audit Logs
          </NavLink>
        </li>
        <li>
          <NavLink 
            to='#' 
            onClick={() => onLinkClick({ title: 'Policy Management', content: <PolicyPop /> })}>
            Policy Management
          </NavLink>
        </li>
        <li>
          <NavLink to='/compliance-reports' activeClassName='active'>
            Compliance Reports
          </NavLink>
        </li>
        <li>
          <NavLink to='/user-management' activeClassName='active'>
            User Management
          </NavLink>
        </li>
      </ul>
    </div>
  );
}

export default Topnavbar;