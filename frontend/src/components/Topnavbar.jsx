import React, { useState, useContext } from 'react';
import { NavLink } from 'react-router-dom';
import '../Pages/DashboardPage/dashindex.css';
import UserProfile from '../Pages/UserProfile/UserProfile'; 
import AuditLogs from '../Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs'; 
import { AuthContext } from '../Pages/context/AuthContext'; 

function Topnavbar({ onLinkClick, userId }) {
    const [showProfile, setShowProfile] = useState(false);
    const { user, logout } = useContext(AuthContext); // Get user state and logout function from context

    const handleProfileClick = () => {
        setShowProfile(!showProfile);
    };

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
                        to='/audit_log' 
                        onClick={() => onLinkClick({ title: 'Audit Logs', content: <AuditLogs /> })}>
                        Audit Logs
                    </NavLink>
                </li>
                <li>
                    <NavLink to='/compliance-reports' activeClassName='active'>
                        Compliance Reports
                    </NavLink>
                </li>
                <li>
                    <button onClick={handleProfileClick}>
                        Profile
                    </button>
                    {showProfile && <UserProfile userId={userId} />}
                </li>
                <li>
                    {user ? (
                        <button onClick={logout}>Logout</button>
                    ) : (
                        <>
                            <NavLink to='/login'>Login</NavLink>
                            <NavLink to='/signup'>Sign Up</NavLink>
                        </>
                    )}
                </li>
            </ul>
        </div>
    );
}

export default Topnavbar;