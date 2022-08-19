import React, { useState, useEffect } from 'react'

function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/test").then(
            res => res.json()
        ).then(
            data => {
                console.log("data is", data)
                setData(data)
                console.log(data)
            }
        )
    }, [])

  return (
      <div>
          {(typeof data.test === 'undefined') ? (
              <p>Loading...</p>
          ): (
              data.test.map((test, i) => (
                  <p key={i}>{test}</p>
              ))
          )
          }
      </div>
  )
}

export default App