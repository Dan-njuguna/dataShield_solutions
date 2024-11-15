import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function Regulations() {
    const [reg, setReg] = useState([]);
    const [error, setError] = useState(true)
    const [loading, setLoading] = useState(null);

    //function for fetching data from the server
    useEffect(() => {
        const fetchRegulations = async () => {
        try {
            const response = await axios.get ('http://localhost:8000/regulations/', {
                headers:{
                    Authorization: 'Token 4af02030ad9fe551a32e72afdddf66b385dc5e78',
                },
            });
            console.log('Response data:', response.data);

            //check if the resoponse data is an array
            if (Array.isArray(response.data.results)) {
                setReg(response.data.results);
              } else {
                throw new Error('Response data is not an array');
              }
            } catch (error) {
              console.error('Error fetching reports:', error);
              setError(error.response ? error.response.data : error.message);
            } finally {
              setLoading(false);
            }
          };
        fetchRegulations();
    }, [])
  
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

  return (
    <div>
    <h2>Compliance Reports</h2>
    {reg.length > 0 ? (
      <ul>
        {reg.map(reg => (
          <li key={reg.id}>{reg.title || reg.generated_at || 'Regulation'}</li>
        ))}
      </ul>
    ) : (
      <div>No regulations found.</div>
    )}
  </div>
  )
}
