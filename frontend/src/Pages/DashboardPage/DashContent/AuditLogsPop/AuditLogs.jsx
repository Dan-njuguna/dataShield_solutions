import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { Container, Row, Col, Spinner, Alert, Pagination } from 'react-bootstrap';

function AuditLogs() {
    const [data, setData] = useState({ results: [], count: 0 });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage] = useState(10);

    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.get(
                'http://localhost:8000/audit/logs/',
                {
                    headers: {
                        Authorization: 'Token a59dffe6150c2dc30be516b6a819b560bf72b8d6', // Ensure you use the correct token format
                    },
                    params: {
                        page: currentPage, // Pass the current page
                        limit: itemsPerPage // Pass the items per page
                    }
                }
            );
            setData(response.data); // Set the entire response
        } catch (error) {
            console.error("Error fetching data:", error);
            setError('An error occurred while fetching data. Please try again later.');
        } finally {
            setLoading(false);
        }
    }, [currentPage, itemsPerPage]);

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    const totalPages = Math.ceil(data.count / itemsPerPage); // Calculate total pages based on count

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    return (
        <Container className="audit-logs">
            <Row>
                <Col md={12}>
                    <h2>Audit Logs</h2>
                    {loading ? (
                        <Spinner animation="border" role="status">
                            <span className="sr-only">Loading...</span>
                        </Spinner>
                    ) : error ? (
                        <Alert variant="danger">{error}</Alert>
                    ) : data.results.length > 0 ? (
                        <ul className="audit-logs-list">
                            {data.results.map(item => (
                                <li key={item.id} className="audit-log-item">
                                    <h4>{item.action_description || `Log ${item.id}`}</h4>
                                    <p><strong>Organization:</strong> {item.organization?.name || 'N/A'}</p>
                                    <p><strong>User:</strong> {item.user?.username || 'N/A'}</p>
                                    <p><strong>Action:</strong> {item.action || 'N/A'}</p>
                                    <p><strong>Affected Resource:</strong> {item.affected_resource || 'N/A'}</p>
                                    <p><strong>IP Address:</strong> {item.ip_address || 'N/A'}</p>
                                    <p><strong>Is Compliant:</strong> {item.is_compliant ? 'Yes' : 'No'}</p>
                                    <p><strong>Compliance Notes:</strong> {item.compliance_notes || 'N/A'}</p>
                                    <p><strong>Additional Data:</strong> {JSON.stringify(item.additional_data) || 'N/A'}</p> {/* If it's an object, stringify it */}
                                    <p><strong>Generated At:</strong> {new Date(item.created_at).toLocaleString() || 'N/A'}</p>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <div>No data found.</div>
                    )}
                    
                    {totalPages > 1 && (
                        <Pagination>
                            <Pagination.First onClick={() => handlePageChange(1)} disabled={currentPage === 1}>
                                First
                            </Pagination.First>
                            <Pagination.Prev onClick={() => handlePageChange(currentPage - 1)} disabled={currentPage === 1}>
                                Previous
                            </Pagination.Prev>
                            {[...Array(totalPages)].map((_, i) => (
                                <Pagination.Item 
                                    key={i + 1} 
                                    active={currentPage === i + 1} 
                                    onClick={() => handlePageChange(i + 1)}
                                >
                                    {i + 1}
                                </Pagination.Item>
                            ))}
                            <Pagination.Next onClick={() => handlePageChange(currentPage + 1)} disabled={currentPage === totalPages}>
                                Next
                            </Pagination.Next>
                            <Pagination.Last onClick={() => handlePageChange(totalPages)} disabled={currentPage === totalPages}>
                                Last
                            </Pagination.Last>
                        </Pagination>
                    )}
                </Col>
            </Row>
        </Container>
    );
}

export default AuditLogs;