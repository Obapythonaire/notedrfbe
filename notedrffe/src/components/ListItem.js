import React from 'react'
import { Link } from 'react-router-dom'
// import notes from '../assets/data'


// But it does'nt make sense to have a whole lot of the body of the
// note on the homepage
// Let's clean the code to display little part a s tittle

let getTitle = (note) =>{
    const title = note.body.split('\n')[0]

    if (title.length >25 ){
        return title.slice(0, 25)
    }
    // console.log(title)
    return title
    
}

let getContent = (note) => {
    let title = getTitle(note)
    let content = note.body.replaceAll('\n', ' ')
    content = content.replaceAll(title, "")

    if (content.length > 25){
        return content.slice(0, 25)
    }else{
        return content
    }
}

// To add a date to our note and convert date from the data to more nicer one
let getDate = (note) =>{
    return new Date(note.updated).toLocaleDateString()
}

const ListItem = ({note}) => {
  return (
    <Link to={`/note/${note.id}`}>
        <div className='notes-list-item'>
            {/* <h3>{note.body}</h3> */}
            <h3>{getTitle(note)}</h3>
            <p><span>{getDate(note)}</span>{getContent(note)}</p>
        </div>
    </Link>
    
  )
}

export default ListItem