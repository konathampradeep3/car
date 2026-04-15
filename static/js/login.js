let l=[{'pradeep':1234},{'hari':1234}]

document.getElementById('Submit').addEventListener('click', function (event) {
    event.preventDefault();
    let username=document.getElementById('username').value
    let password=document.getElementById('password').value
    for(let i=0;i<l.length;i++){
        p=l[i]
        for(let key in p){
        if(username==key && password==p[key]){
            window.location.href='/home/';
            return;
        }
    }
}
            alert('please enter valid credentials')

});