    // let input = document.querySelector('.outputBox');
    // let buttons = document.querySelectorAll('button');

    // let string = "";
    // let arr = Array.from(buttons);
    // arr.forEach(button => {
    //     button.addEventListener('click', (e) => {
    //         if (e.target.innerHTML == '=') {
    //             try {
    //                 string = eval(string);
    //             } catch (err) {
    //                 string = "Error";
    //             }
    //             input.value = string;
    //         } else if (e.target.innerHTML == 'AC') {
    //             string = "";
    //             input.value = string;
    //         } else if (e.target.innerHTML == 'DEL') {
    //             string = string.substring(0, string.length - 1);
    //             input.value = string;
    //         } else {
    //             string += e.target.innerHTML;
    //             input.value = string;
    //         }
    //     })
    // });
let input = document.querySelector('.outputBox');
    let buttons = document.querySelectorAll('button');

    let string = "";
    let arr = Array.from(buttons);

    arr.forEach(button => {
        button.addEventListener('click', (e) => {
            let btn = e.target.innerText;

            if (btn === '=') {
                try {
                    string = eval(string);
                } catch (err) {
                    string = "Error";
                }
                input.value = string;
            } else if (btn === 'AC') {
                string = "";
                input.value = string;
            } else if (btn === 'DEL') {
                string = string.slice(0, -1);
                input.value = string;
            }

            // ✅ Handle trigonometric functions
            else if (btn === 'sin') {
                string = Number(Math.sin(toRadians(eval(string)))).toFixed(4);
                 input.value = string;
            }
            else if (btn === 'cos') {
                string = Number(Math.cos(toRadians(eval(string)))).toFixed(4);
                input.value = string;
            } 
            else if (btn === 'tan') {
                string = Number(Math.tan(toRadians(eval(string)))).toFixed(4);
                input.value = string;
            
            } 
            else if (btn === 'cot') {
                string = Number(1 / Math.tan(toRadians(eval(string)))).toFixed(4);
                input.value = string;
            } 
            else if (btn === 'sec') {
                string = Number(1 / Math.cos(toRadians(eval(string)))).toFixed(4);
                input.value = string;
            }           
            else if (btn === 'cosec') {
                string = Number(1 / Math.sin(toRadians(eval(string)))).toFixed(4);
                input.value = string;
            }

            else if (btn.includes('x²')) {
                try {
                    string = (eval(string) ** 2).toString();
                } catch (err) {
                    string = "Error";
                }
                input.value = string;
            } else if (btn.includes('x³')) {
                try {
                    string = (eval(string) ** 3).toString();
                } catch (err) {
                    string = "Error";
                }
                input.value = string;
            }

            // ✅ For other buttons
            else {
                string += btn;
                input.value = string;
            }
        });
    });
        function toRadians(degree) {
        return degree * (Math.PI / 180);
    }