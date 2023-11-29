class Example{
    constructor(isRed,timevalue){
        this.isRed = false;
        this.inputvalue = 1;
        this.initElements();
        this.initEvents();
    }

    initElements(){
        this.btn = document.getElementById('btn');
        this.inputElement = document.getElementById('username');
        this.btn.classList = 'btn';
        //this.inputElement.value = this.inputvalue;
    }

    initEvents(){
        this.btn.addEventListener('click',this.toggleBtn.bind(this));
    }

    toggleBtn(){
        if(!this.isRed){
            this.btn.classList.add('beatuty');
            this.isRed = true;
        }else{
            this.btn.classList.remove('beatuty');
            this.isRed = false;
        }
        
        
    }

    incrementTimer(){
        this.inputElement.value = this.inputvalue++;
    }
    createtimer(){
        setInterval(this.toggleBtn.bind(this),2000);
        var self = this;
        setInterval(this.incrementTimer.bind(this),1000);
    }

    
}

var obj = new Example(false,1000);
obj.createtimer()
