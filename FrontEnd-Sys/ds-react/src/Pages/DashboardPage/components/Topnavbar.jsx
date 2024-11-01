import React from 'react';
import {Link} from 'react-router-dom';
import '../dashindex.css'
import PolicyPop from '../DashContent/PolicyPop/PolicyPop';
import Reportspop from '../DashContent/ReportsPop/Reportspop'
import UserMng from '../DashContent/UserManangementPop/UserMng';
import AuditLogs from '../DashContent/AuditLogsPop/AuditLogs';
import Regulations from '../DashContent/RegulationsPop/Regulations';

 function Topnavbar({onLinkClick}) {
// const closeColumn =() => {
//     setIsOpen(false);
//   };

  return (
    <div className='Topnavbar'><ul>
      <Link to = '#' onClick = {()=>  onLinkClick({title: 'Regulations overview', content:<Regulations/>})}>Regulation Overview</Link>
      <Link to = '#' onClick = {()=>  onLinkClick({title: 'Audit Logs', content: <AuditLogs/>})}>Audit Logs</Link>
      <Link to = '#' onClick = {()=>  onLinkClick({title: 'Policy Management', content: <PolicyPop/>})}>Policy Management</Link>
      <Link to = '#' onClick = {()=>  onLinkClick({title: 'User Management', content: <UserMng/>})}>User Management</Link>
      <Link to = '#' onClick = {()=>  onLinkClick({title: 'Reports', content: <Reportspop/>})}>Reports</Link>
      </ul>
      {/* we then render the side page that's supposed to show up */}
      </div>

  )
}
export default Topnavbar;
