import { React, useState, useEffect } from "react";


function List(props) {
  const [searchResult, setSearchResult] =  useState(0);

  useEffect(() => {
    fetch('/api/search').then(res => res.json()).then(result => {
      setSearchResult(result.id)
    });
  }, []);
    
    return (
        <ul>
            { searchResult.map((item) => (
                <li key={item.id}>{item.text}</li>
            ))}
        </ul>
    )
}

export default List;
