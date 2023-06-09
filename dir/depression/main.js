// Wrap your code in a function to prevent scope conflicts
var text_3_content = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem officia quia eveniet dicta, blanditiis quas ea obcaecati ipsum! Vitae, assumenda cumque veritatis natus repellat aperiam adipisci nulla architecto consectetur, commodi qui tempora at laborum et ab ad soluta hic culpa dolorum placeat cum! Architecto voluptate sint commodi alias eligendi laudantium est corporis eveniet perferendis atque veritatis saepe odit voluptates asperiores numquam obcaecati fugiat, animi deserunt ad. Dolor magni quasi, officia ullam accusamus quas repellendus eius ut velit aliquid maiores illo fugit autem eligendi iste rem totam repellat excepturi dolorum, iure, quaerat corporis beatae ab doloremque? Quaerat, obcaecati accusamus. Quis delectus adipisci, cumque modi molestiae illo inventore laboriosam quibusdam, repudiandae, dolore vero. Ipsam, veritatis ea quas facere a hic nihil neque quae incidunt assumenda ad qui corrupti, ut maiores molestias expedita, et unde recusandae nemo debitis! Quae consequuntur delectus iusto ab numquam in autem fugiat libero perferendis?";
function startAnimation() {
  const text_1 = document.getElementById("movable-text");
  const text_2 = document.getElementById("start-coding-text");
  const div_wrapper = document.getElementById("main");
  const style = document.getElementById("main_style");

  async function change_text_1() {
    text_1.innerHTML = "DEPRESSE";
    await sleep(500);
    text_1.innerHTML = "DEPRESS";
    await sleep(500);
    text_1.innerHTML = "DEPRES";
    await sleep(400);
    text_1.innerHTML = "DEPRE";
    await sleep(300);
    text_1.innerHTML = "DEPR";
    await sleep(200);
    text_1.innerHTML = "DEP";
    await sleep(200);
    text_1.innerHTML = "DE";
    await sleep(100);
    text_1.innerHTML = "D";
    await sleep(50);
    text_1.innerHTML = "?";

    setTimeout(start_coding, 100);
  }

  async function start_coding() {
    text_2.innerHTML = "start ";
    await sleep(100);
    text_2.innerHTML = "start feeling  ";
    await sleep(300);
    text_2.innerHTML = "start feeling  the ";
    await sleep(400);
    text_2.innerHTML = "start feeling  the CODE";
    div_wrapper.innerHTML = '<h1 id="movable-text">?</h1><h2 style="background-color: white; background-image: none;" id="start-coding-text">start feeling  the CODE</h2><img class="bottom-img" src="images/bottom-img.png" alt=""><p id="text-content" class="text-content"></p>';
    style.innerHTML = ".wrapper {overflow-y: auto;}";
    const text_3 = document.getElementById("text-content");
    text_3.innerHTML = text_3_content;

  }

  setTimeout(change_text_1, 500);
}

// Utility function to pause execution for a specified duration
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Call the startAnimation function after the document has loaded
document.addEventListener("DOMContentLoaded", startAnimation);