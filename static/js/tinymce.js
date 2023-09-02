tinymce.init({
    selector: '#text',
    plugins: 'ai tinycomments mentions anchor upload autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed permanentpen footnotes advtemplate advtable advcode editimage tableofcontents mergetags powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss',
    toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image upload table mergetags | align lineheight | tinycomments | checklist numlist bullist indent outdent | emoticons charmap | removeformat| upload',

image_title: true,
image_caption: true,

image_advtab: true,
file_picker_types: "image media",  
  automatic_uploads: true,
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',

    file_picker_callback: function (cb, value, meta) {
          var input = document.createElement("input");
          input.setAttribute("type", "file");
          if (meta.filetype == "image") {
              input.setAttribute("accept", "image/*");}
          if (meta.filetype == "media") {
          input.setAttribute("accept", "video/*");}
  
          input.onchange = function () {     
              var file = this.files[0];
              var reader = new FileReader();
              reader.onload = function () {
                  var id = "blobid" + (new Date()).getTime();
                  var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
                  var base64 = reader.result.split(",")[1];
                  var blobInfo = blobCache.create(id, file, base64);
                  blobCache.add(blobInfo);
                 cb(blobInfo.blobUri(), { title: file.name });
               };
               reader.readAsDataURL(file);
           };
           input.click();
        },
        content_style: "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
        
    ai_request: (request, respondWith) => respondWith.string(() => Promise.reject("See docs to implement AI Assistant"))
  });
  