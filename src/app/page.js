import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <div>
          <h1>
            <span>
              Hello<span className={styles.yellowText}>.</span>
            </span>
            <br />
            <span>
              <span>I am</span>
            </span>
            <br />
            <span>josh carlson</span>
          </h1>
        </div>
      </header>
      <section className={styles.infoSection}>
        <img
          src="/imagen-para-website.png"
          alt="imagen"
          ClassName={styles.image}
        />   
        <div className={styles.infoContainer}>
          <span className={styles.tittle + " " +styles.yellowText}>josh</span>
          <br />
          <span className={styles.tittle}>carlson</span>
        </div>
        <div> className={styles.list}
          <ul>
            <li>
              <span className={styles.grayText}>Age: </span>27
             </li>
             <li>
            <span className={styles.grayText}>Nationatily: </span>German
            </li>
            <li>
            <span className={styles.grayText}>Skill set: </span> Project Managment and financial Performance
            </li>
            <li>
            <span className={styles.grayText}>Languages: </span> English, German
            </li>
          </ul>
        </div>    
      </section>
    </main>
  );
}
