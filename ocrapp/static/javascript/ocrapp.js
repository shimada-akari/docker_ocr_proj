window.onload = function() {
    console.log("読み込みテスト")
    
}

function ImagePreview(img_element){
    var fileslist = img_element.files;
    if (fileslist.length == 1){
        var fileReader = new FileReader();
        fileReader.onload = function() {
            document.getElementById("img_preview").setAttribute('src', this.result);
            }
        // ファイルの読み込み(Data URI Schemeの取得)
        fileReader.readAsDataURL( fileslist[0] );
    }

}