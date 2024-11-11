// LoginPage.js
import React, { useState } from 'react';
import axios from 'axios';
import './login.css'
const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    // Handle input changes
    const handleUsernameChange = (e) => setUsername(e.target.value);
    const handlePasswordChange = (e) => setPassword(e.target.value);

    // Login function - send a POST request to the Django backend
    const handleLogin = async (e) => {
        e.preventDefault();  // Prevent default form submission
        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                username: username,
                password: password,
            });
            
            if (response.status === 200) {
                const { token } = response.data;
                // Store the token (in localStorage for simplicity here)
                localStorage.setItem('authToken', token);
                alert('Login successful!');
                // Redirect to a protected page or handle successful login
            }
        } catch (error) {
            setError('Invalid username or password. Please try again.');
        }
    };

    return (
        <div style={{ maxWidth: '400px', margin: 'auto', padding: '1rem' }} className='form'>
            {/* <h2>L
                
            </h2> */}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleLogin}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={handleUsernameChange}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={handlePasswordChange}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default LoginPage;
