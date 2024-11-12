import React from 'react';
import { NavLink } from 'react-router-dom';
import '../index.css'; 

function Sidenavbar() {
  return (
    <div className='Sidenavbar'>
      <ul>
        <li>
          <NavLink to='/dashboard' activeClassName='active'>
            Dashboard
          </NavLink>
        </li>
        <li>
          <NavLink to='/overview' activeClassName='active'>
            Overview
          </NavLink>
        </li>
      </ul>
    </div>
  );
}

export default Sidenavbar;