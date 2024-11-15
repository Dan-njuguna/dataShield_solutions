import React from 'react';
import { NavLink } from 'react-router-dom';
import '../index.css';

function Tabs() {
  return (
    <div className='Tabs'>
      <ul>
        <li>
          <NavLink to='/dashboard' activeClassName='active'>
            <div className='tabs-container'>Dashboard</div>
          </NavLink>
        </li>
        <li>
          <NavLink to='/current-metrics' activeClassName='active'>
            <div className='tabs-container'>Current Metrics</div>
          </NavLink>
        </li>
        <li>
          <NavLink to='/quick-access' activeClassName='active'>
            <div className='tabs-container'>Quick Access</div>
          </NavLink>
        </li>
      </ul>
    </div>
  );
}

export default Tabs;