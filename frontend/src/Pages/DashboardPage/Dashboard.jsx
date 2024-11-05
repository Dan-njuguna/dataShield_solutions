import React, { useState, useEffect } from 'react';
import Sidenavbar from '../../components/Sidenavbar';
import Topnavbar from '../../components/Topnavbar';
import AuditLogs from '../../Pages/DashboardPage/DashContent/AuditLogsPop/AuditLogs';
import Regulations from '../../Pages/DashboardPage/DashContent/RegulationsPop/Regulations';
import './dashindex.css';
import DSlogo from '../../img/DSlogo.png';
import axios from 'axios';

function Dashboard() {
    const [selectedContent, setSelectedContent] = useState(null);
    const [auditLogsData, setAuditLogsData] = useState(null);
    const [regulationsData, setRegulationsData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleTopnavbarContent = (pageContent) => {
        setSelectedContent(pageContent);
    };

    const closeSideColumn = () => {
        setSelectedContent(null);
    };

    const fetchAuditLogsData = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get('http://localhost:8000/audit/logs/');
            setAuditLogsData(response.data.logs); // Adjust according to your API response structure
        } catch (error) {
            console.error("Error fetching AuditLogs data:", error);
            setError("Failed to fetch audit logs.");
        } finally {
            setLoading(false);
        }
    };

    const fetchRegulationsData = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get('http://localhost:8000/compliance/data-protection-regulations/');
            setRegulationsData(response.data); // Adjust according to your API response structure
        } catch (error) {
            console.error("Error fetching Regulations data:", error);
            setError("Failed to fetch regulations.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (selectedContent) {
            if (selectedContent.title === 'AuditLogs') {
                fetchAuditLogsData();
            } else if (selectedContent.title === 'Regulations') {
                fetchRegulationsData();
            }
        }
    }, [selectedContent]);

    return (
        <>
            <Topnavbar className="Topnavbar" onLinkClick={handleTopnavbarContent} />
            <div className="dash-container">
                <div className="cont-col-1"><Sidenavbar /></div>
                <div className="cont-col-2">
                    <img src={DSlogo} alt="Data Shield Logo" className="logo" />
                    <p>Welcome to Data Shield</p>

                    {loading && <p>Loading...</p>}
                    {error && <p style={{ color: 'red' }}>{error}</p>}

                    {selectedContent ? (
                        <div>
                            <h2>{selectedContent.title}</h2>
                            <p>{selectedContent.content}</p>
                            <button className="close-btn" onClick={closeSideColumn}>Close</button>

                            {/* Render AuditLogs when selected */}
                            {selectedContent.title === 'AuditLogs' && (
                                <AuditLogs 
                                    content={selectedContent} 
                                    isOpen={!!selectedContent} 
                                    onClose={closeSideColumn} 
                                    data={auditLogsData} 
                                />
                            )}

                            {/* Render Regulations when selected */}
                            {selectedContent.title === 'Regulations' && (
                                <Regulations 
                                    content={selectedContent} 
                                    isOpen={!!selectedContent} 
                                    onClose={closeSideColumn} 
                                    data={regulationsData} 
                                />
                            )}
                        </div>
                    ) : (
                        <p>Select an option from the sidebar to view content.</p>
                    )}
                </div>
            </div>
        </>
    );
}

export default Dashboard;