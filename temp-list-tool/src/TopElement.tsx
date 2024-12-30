import myLogo from './assets/penimg.jpeg'
import './TopElement.css'

function TopElement() {
  return (
    <div className="App">
      <img src={myLogo} className="mylogo" alt="logo" />
      <p className="info">
        This is a small tool for creating temporary lists.
      </p>
    </div>
  )
}

export default TopElement;
