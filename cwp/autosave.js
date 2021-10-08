inputTextToSave.value = localStorage.getItem('inputTextToSave');
inputTextToSave.oninput = () => {
  localStorage.setItem('inputTextToSave', inputTextToSave.value)
};
