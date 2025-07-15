import React from 'react';
import './PrivacyPolicy.css';

const PrivacyPolicy: React.FC = () => {
  return (
    <div className="privacy-policy">
      <div className="privacy-policy-container">
        <h1>Privacy Policy</h1>
        <p>Your privacy is important to us. This Privacy Policy explains how we collect, use, and share information when you use our Arabic Keyboard application for Android and iOS.</p>
        <section>
          <h2>1. Information We Collect</h2>
          <p>
            We want to be clear about what information we do and don't collect, especially since our App offers unique Prosodic text features.
          </p>
          <ul>
            <li>
              <b>Keyboard Usage Data (Anonymized):</b> To improve our diacritization suggestions Dictionary, we may collect anonymized and aggregated data related to the patterns of your input. This includes:
              <ul>
                <li><b>Keystroke patterns: </b>only texts with full diacritics that are ready for audio Synthesis.</li>
                <li><b>Application performance data:</b> Information about how the App functions, crashes, or errors, to help us improve stability.</li>
              </ul>
            </li>
            <li><b>Crucially, we do NOT collect the actual content of your typed messages, personal communications, or any sensitive data that could identify you or reveal the meaning of your texts. Such personal data is without diacritics, and it has no use in our public Dictionary.</b></li>
            <li><b>Non-Personal Device Information:</b> We may collect non-identifiable information about your device, such as device model, operating system version, and general locale settings. This helps us optimize the App for different devices and ensure compatibility, but it does not identify you personally.</li>
          </ul>
        </section>

        <section>
          <h2>2. How We Use Your Information</h2>
          <p>
            The limited information we collect is used solely to enhance your experience with the Arabic Keyboard app:
          </p>
          <ul>
            <li>
              <b>To Provide and Improve App Features:</b> The anonymized keyboard usage data is essential for developing text suggestions, adding diacritics for Audio Synthesis, and and language Prosodic analysis algorithms used in Poetry. This helps the App better understand, predict, and suggest next words and syllables while synthesizing Poetry.
            </li>
            <li>
              <b>To Maintain and Optimize the App:</b> Non-personal device information and performance data help us identify and fix bugs, improve app stability, and ensure the App runs smoothly on various devices.
            </li>
            <li>
              <b>For Research and Development:</b> Aggregated, anonymized data may be used for internal research to further improve the intelligence and features of the rhythmic text generation.
            </li>
          </ul>
        </section>

        <section>
          <h2>3. Information Sharing</h2>
          <p>
            We are committed to protecting your privacy and do not share your personal information.
          </p>
          <ul>
            <li>
              <b>No Personal Data Sharing:</b> We do not sell, trade, or otherwise transfer your <b>personal information</b> to third parties. As we do not collect personal text content, there is no personal content to share.
            </li>
          </ul>
        </section>

        <section>
          <h2>4. Data Security</h2>
          <p>
            We take reasonable measures to protect the information we collect from unauthorized access, disclosure, alteration, or destruction. Given the nature of the data we collect (anonymized keyboard patterns and non-personal device information), the risk of sensitive data breaches is significantly minimized. All data processed on our servers, if any, is handled with industry-standard security protocols.
          </p>
        </section>

        <section>
          <h2>5. Your Rights</h2>
          <p>
            As a user of our App, you have certain rights regarding your data:
          </p>
          <ul>
            <li>
              <b>Access and Correction:</b> Since we do not collect personally identifiable information from your keyboard input, there is no personal data for you to access or correct in our systems.
            </li>
            <li>
              <b>Opt-Out of Data Collection: </b> If you wish to prevent the collection of anonymized usage data for analysis, you may be able to do so through the App's settings. Please refer to the App's in-app settings for more details on available privacy controls.
            </li>
            <li>
              <b>Deletion: </b> If you uninstall the App, any locally stored anonymized usage data will be removed from your device.
            </li>
          </ul>
        </section>

        <section>
          <h2>6. Contact Us</h2>
          <p>
            If you have any questions or concerns about this Privacy Policy or our data practices, please contact us at: 
 <b> admin@Arabiyy.com</b>

          </p>
        </section>

        <div className="privacy-policy-footer">
          <p>Last updated: {new Date().toLocaleDateString()}</p>
        </div>
      </div>
    </div> 
  );
};

export default PrivacyPolicy; 