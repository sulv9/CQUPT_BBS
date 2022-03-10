{/* <script> */ }
const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");


signupBtn.onclick = (() => {
    loginForm.style.marginLeft = "-50%";
    loginText.style.marginLeft = "-50%";

});
loginBtn.onclick = (() => {
    loginForm.style.marginLeft = "0%";
    loginText.style.marginLeft = "0%";

});
signupLink.onclick = (() => {
    signupBtn.click();
    return false;
});
// Modal 模块
const viewBtn = document.querySelector(".view-modal"),
    popup = document.querySelector(".popup"),
    close = popup.querySelector(".close");
// 添加show类
viewBtn.onclick = () => {
    popup.classList.toggle("show");
}
// 再次除法取消
close.onclick = () => {
    // 触发 login 按钮初始化
    loginBtn.click();
    // 触发 viewBtn 改变 show状态
    viewBtn.click();
}

// </script>