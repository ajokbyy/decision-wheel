async function spinWheel(){
    const input = document.getElementById("options").value;

    console.log("Raw input:", input);

    const options  = input.split(",").map(opt => opt.trim()).filter(opt => opt.length > 0);

    
}