import { React, useState, useEffect } from "react";


function List(props) {
  const [searchResult, setSearchResult] =  useState(0);
  searchResult => {
    fetch('/api/search').then(res => res.json()).then(data => 
	    {
  };
  useEffect(() => {
      searchResult = (data.result);
    s});
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
