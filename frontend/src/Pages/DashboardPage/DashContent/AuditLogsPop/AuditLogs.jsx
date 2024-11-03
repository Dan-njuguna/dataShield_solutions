//the AuditLogs compnentsreceives the properties in line five from the paent component that mananges th state which is the Topnavbar
 function AuditLogs({content, isOpen, onClose }) {
  if (!isOpen) return null;
const columStyle = {
  width: '75%',
  backgroundColor: '#f2f2f2',
  padding: '20px 40px',
  }
  return (
    <>
    {/* // in theline bellow qw use a template lieral that alows us to include varibales and expressions in a string
    //AuditLogs is a static varibale while the rest of the expression is a conditional variable */}
  <div className="side-column" style = {columStyle}>
  <div className={`AuditLogs ${isOpen?  'open': ''}`}>
    <button onClick={onClose}>Close</button>
    </div>
    <div> {content.status}</div>
    <h2>{content.title}</h2>
    <p>{content.content}</p>
    
  </div>
    
    </>
  );
}
export default AuditLogs;