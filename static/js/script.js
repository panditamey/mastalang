function autoResize(textarea) {
  textarea.style.height = "auto";
  textarea.style.height = textarea.scrollHeight + "px";
}

function preserveHeight() {
  const textarea = document.getElementById("code");
  textarea.style.height = "auto";
  textarea.style.height = textarea.scrollHeight + "px";
}

document.addEventListener("DOMContentLoaded", () => {
  const textarea = document.getElementById("code");
  autoResize(textarea);
});

function copyAndInjectCode(button) {
  const codeElement = button.nextElementSibling.querySelector("code");
  const codeText = codeElement.innerText.trim();

  // Copy to clipboard code
  navigator.clipboard
    .writeText(codeText)
    .then(() => {
      button.innerText = "Copied!";
      setTimeout(() => {
        button.innerText = "Copy Code";
      }, 2000);
    })
    .catch((err) => {
      console.error("Failed to copy text: ", err);
    });

  // Inject code into the textarea
  const textarea = document.getElementById("code");
  textarea.value = codeText;
  autoResize(textarea); // Adjust the textarea height based on content

  // Scroll to the textarea
  textarea.scrollIntoView({ behavior: "smooth", block: "start" });
  textarea.focus(); // Focus the textarea to highlight it for the user
}
