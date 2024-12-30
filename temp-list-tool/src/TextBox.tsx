import { useState } from "react"
import './TextBox.css'

function TextBox(){
    
    const [text, setText] = useState<string>('');
    const [textData, setTextData] = useState<string[]>([]);

    const addText = () => {
        if(text.trim() !== ''){
            setTextData([...textData, text]);
            setText('');
        }
    }

    const removeListElement = (index: number) => {
        setTextData(textData.filter((_, i) => i !== index));
    }

    return (
        <>
            <input
                value = {text}
                onChange = {e => setText(e.target.value)}
            />
            <button onClick={addText}>Add</button>
            <div className="listul">   
                <ul>
                    {textData.map((item, index) => (
                        <li key = {index} onClick={() => removeListElement(index)}>{item}</li>
                    ))}
                </ul>
            </div>    
        </>    
    );
}

export default TextBox