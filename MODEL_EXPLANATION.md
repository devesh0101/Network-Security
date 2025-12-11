# Network Security Model - Prediction Explanation

## 🎯 What Does the Model Predict?

Your model is a **Phishing Website Detection System** using machine learning classification.

### **Target Variable: `Result`**
- **Type:** Binary Classification (0 or 1)
- **Meaning:**
  - `0` = **Legitimate website** (safe to visit ✅)
  - `1` = **Phishing website** (dangerous, likely malicious ⚠️)

The model predicts whether a given website URL is phishing or legitimate based on 30 different URL and website characteristics.

---

## 📊 Input Variables (Features)

The model uses **30 input features** to make predictions. All are numeric values (integers) representing URL and website characteristics:

### **1. URL Structure Features**
| Feature | Meaning |
|---------|---------|
| `having_IP_Address` | Does URL contain an IP address instead of domain name? |
| `URL_Length` | Is the URL length suspicious? |
| `Shortining_Service` | Is a URL shortening service used? |
| `having_At_Symbol` | Does URL contain '@' symbol? |
| `double_slash_redirecting` | Does URL have '//' for redirection? |
| `Prefix_Suffix` | Does domain have '-' (prefix/suffix)? |
| `having_Sub_Domain` | Number of subdomains in URL? |

### **2. SSL Certificate & Security**
| Feature | Meaning |
|---------|---------|
| `SSLfinal_State` | Is the SSL certificate valid? |
| `Domain_registeration_length` | Is domain registration period long-term? |
| `HTTPS_token` | Does URL use HTTPS protocol? |

### **3. Page Content & Links**
| Feature | Meaning |
|---------|---------|
| `Favicon` | Does page have a valid favicon? |
| `port` | Is the port number standard/safe? |
| `Request_URL` | Do objects load from external URLs? |
| `URL_of_Anchor` | Do anchor tags point to strange places? |
| `Links_in_tags` | Are links in tags suspicious? |
| `SFH` (Server Form Handler) | Does form submit to legitimate server? |

### **4. User Interaction & Page Behavior**
| Feature | Meaning |
|---------|---------|
| `Submitting_to_email` | Does form submit to email address? |
| `Abnormal_URL` | Is the URL abnormally formatted? |
| `Redirect` | Does page redirect to other pages? |
| `on_mouseover` | Does mouseover trigger suspicious actions? |
| `RightClick` | Is right-click disabled? |
| `popUpWidnow` | Are popup windows used? |
| `Iframe` | Are iframes embedded in page? |

### **5. Domain & Reputation**
| Feature | Meaning |
|---------|---------|
| `age_of_domain` | How old is the domain? |
| `DNSRecord` | Is DNS record available? |
| `web_traffic` | Does site have legitimate web traffic? |
| `Page_Rank` | What is the page's Google PageRank? |
| `Google_Index` | Is the site indexed by Google? |
| `Links_pointing_to_page` | How many legitimate sites link to it? |
| `Statistical_report` | Is site in statistical phishing reports? |

---

## 💡 Feature Values Explanation

All features are encoded as **integer values**, typically:

### **Common Encoding Scheme:**
```
-1 = Suspicious/Phishing indicator
 0 = Neutral (inconclusive)
 1 = Legitimate/Safe indicator
```

### **Example:**
```
having_IP_Address: -1  → URL contains IP address (suspicious) ⚠️
SSLfinal_State: 1      → Valid SSL certificate (safe) ✅
Abnormal_URL: 0        → Neutral/mixed indicators
```

---

## 🤖 ML Models Used for Prediction

Your training pipeline trains multiple models and picks the best one:

1. **Gradient Boosting Classifier** (Usually best performer)
2. Random Forest Classifier
3. Decision Tree Classifier
4. Logistic Regression
5. AdaBoost Classifier

The model automatically selects whichever has the highest accuracy on test data.

---

## 📈 Model Performance Metrics

After training, the model is evaluated on:

- **F1-Score:** Balance between precision and recall
- **Precision:** How many predicted phishing sites are actually phishing
- **Recall:** How many actual phishing sites are detected

---

## 🔄 How Predictions Work in Your App

### **Step 1: User uploads CSV file**
```csv
having_IP_Address, URL_Length, Shortining_Service, ... (30 features)
-1, 1, 1, ... 
1, 0, -1, ...
```

### **Step 2: Preprocessing**
- Load preprocessor from `final_model/preprocessor.pkl`
- Normalize/scale the input features
- Handle any missing values

### **Step 3: Model Prediction**
- Load trained model from `final_model/model.pkl`
- Feed processed features to model
- Get prediction: 0 (legitimate) or 1 (phishing)

### **Step 4: Display Results**
- Show original data + predicted column
- Render as HTML table
- Save output to `prediction_output/output.csv`

---

## 📝 Example Input & Output

### **Input CSV:**
```
having_IP_Address,URL_Length,Shortining_Service,...,Statistical_report
-1,1,1,-1,-1,1,-1,...,0
1,1,0,1,1,-1,1,...,-1
```

### **Model Output:**
```
having_IP_Address,URL_Length,...,Statistical_report,predicted_column
-1,1,...,0,1                        ← Predicted: Phishing ⚠️
1,1,...,-1,0                        ← Predicted: Legitimate ✅
```

---

## 🎓 Use Case

This model is useful for:
- **Email security systems** - Detect phishing emails with suspicious URLs
- **Browser extensions** - Warn users about phishing websites
- **Web security firewalls** - Block phishing attempts
- **Cybersecurity research** - Analyze phishing patterns

---

## ⚙️ Important Notes

1. **All inputs must be numeric** - The model expects integer values (-1, 0, 1)
2. **30 features required** - CSV must have exactly these 30 columns
3. **Feature order matters** - Columns must be in the same order as training data
4. **Preprocessing applied** - Input is automatically normalized/scaled
5. **Binary output** - Prediction is always 0 (safe) or 1 (phishing)

---

## 📊 Training Performance (from last run)

Based on your training pipeline output:
- **Model trained on:** 8,844 samples
- **Tested on:** 2,211 samples
- **Best model:** Usually Gradient Boosting with ~90%+ accuracy
- **Metrics tracked:** F1-Score, Precision, Recall

---

## 🔗 Related Files

- **Model:** `/final_model/model.pkl` - Trained classifier
- **Preprocessor:** `/final_model/preprocessor.pkl` - Feature scaling/normalization
- **Schema:** `/data_schema/schema.yaml` - Feature definitions
- **Training data:** `/Network_Data/phisingData.csv` - Original dataset
- **API:** `/app.py` - FastAPI prediction endpoint
