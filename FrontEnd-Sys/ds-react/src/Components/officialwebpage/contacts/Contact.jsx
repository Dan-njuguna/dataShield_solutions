import React from 'react'
import './contacts.css'
import message_icon from '../../../Assets/msg_icon.png'
import location_icon from '../../../Assets/location_icon.png'
import phone_icon from '../../../Assets/phone_icon.png'
import email_icon from '../../../Assets/email_icon.png'
export default function Contact() {
  return (
    <div className="contact">
        <h3 className = "h3"> Send us a message <img src = {message_icon} alt = ""/></h3><br/>
        <p> Feel free to reach out though contact form or find our contat </p>
        <div className="contact-col">
            <ul>
            <li>contacts@datashield. <img src = {email_icon} alt = ""/></li>
            <li>+254 113188250<img src = {phone_icon} alt = ""/></li>
            <li>009300 Ongata Rongai, Kajiado, Kenya<img src = {location_icon} alt = ""/></li>
            </ul>
        </div>
    {/* <div className = "contact-col">
        <label>Your name</label>
        <input type="text" placeholder="Enter your Name"/>
        <label>Phone number</label>
        <input type="tel" placeholder="Enter your phone number"/>
        <label> Write your message here</label>
        <textarea name='message' rows ="6" placeholder='Enter your message' required></textarea>
        <button type="submit" className= "btn dark-btn">Submit</button>
    </div> */}

    </div>
  )
}
