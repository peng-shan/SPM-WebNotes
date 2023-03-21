import React, { useState, useEffect } from 'react'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import { Link } from 'react-router-dom' 
import { useHistory } from 'react-router-dom';


function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const history = useHistory();
  const handleSubmit = async (event) => {
    event.preventDefault()

    // Send login request to backend server with username and password
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
      headers: { 'Content-Type': 'application/json' }
    })

    if (response.ok) {
      // User is authenticated, redirect to NotesListPage
      history.push('/')
    } else {
      // Authentication failed, show error message
      history.push('/')
      alert('Invalid username or password')
    }
  }

  return (
    <div className="login-page">
      <h1>Login</h1>
      <hr />
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input  id="username-input" type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <br />
        <label>
          Password :
          <input  id="password-input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label> 
        <button type="submit">Login</button>
      </form>
    </div>
  )
}

export default LoginPage