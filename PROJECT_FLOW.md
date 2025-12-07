# Network Security Project - Complete Flow Architecture

## 🎯 Project Overview
This is a **Network Security/Phishing Detection Machine Learning Project** that follows a modular architecture with a clear data pipeline flow.

---

## 📊 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   NETWORK SECURITY PROJECT                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────┐
            │      Step 1: Data Push to MongoDB   │
            │       (push_data.py)                 │
            └─────────────────────────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────┐
            │    Step 2: Run ML Pipeline          │
            │       (main.py)                      │
            └─────────────────────────────────────┘
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
            ┌──────────────┐   ┌──────────────┐
            │Data Ingestion│   │ Data Cleaning│
            │  Component   │   │   Component  │
            └──────────────┘   └──────────────┘
```

---

## 🔄 Detailed Workflow

### **Phase 1: Data Preparation (push_data.py)**
```
push_data.py
    │
    ├─ Load CSV: Network_Data/phisingData.csv
    │
    ├─ Create NetworkDataExtractor class
    │
    ├─ Convert CSV → JSON format
    │
    ├─ Connect to MongoDB using MONGO_DB_URL (.env)
    │
    └─ Insert 11,055 records into:
       └─ Database: "NetworkSecurityDB"
       └─ Collection: "PhishingDataCollection"
```

**Key Functions:**
- `get_data_as_json()` - Reads CSV and converts to JSON
- `insert_data_mongodb()` - Connects to MongoDB and inserts data

**Output:** Data stored in MongoDB ✓

---

### **Phase 2: Machine Learning Pipeline (main.py)**
```
main.py
    │
    ├─ 1. Create TrainingPipelineConfig
    │      └─ Sets up artifact directory with timestamp
    │         └─ Path: Artifacts/MM_DD_YYYY_HH_MM_SS/
    │
    ├─ 2. Create DataIngestionConfig
    │      └─ Configures data paths and MongoDB connection
    │
    ├─ 3. Initialize DataIngestion component
    │      │
    │      ├─ Step A: export_collection_as_dataframe()
    │      │    └─ Fetch from MongoDB
    │      │    └─ Remove '_id' column
    │      │    └─ Handle missing values
    │      │
    │      ├─ Step B: export_data_into_feature_store()
    │      │    └─ Save full dataset as CSV
    │      │    └─ Path: Artifacts/.../feature_store/phisingData.csv
    │      │
    │      └─ Step C: split_data_as_train_test()
    │           └─ Split ratio: 80% train, 20% test
    │           └─ Train file: train.csv
    │           └─ Test file: test.csv
    │           └─ Path: Artifacts/.../ingested/
    │
    ├─ 4. Create DataIngestionArtifact
    │      └─ Return paths to train and test files
    │
    └─ 5. Print artifact information
```

---

## 📂 Directory Structure & Data Flow

```
Network security (Project Root)
│
├── push_data.py ............................ [Data Push Script]
│   └── Reads: Network_Data/phisingData.csv
│   └── Writes to: MongoDB
│
├── main.py ................................ [ML Pipeline Entry Point]
│   └── Triggers: DataIngestion component
│
├── Network_Security/
│   │
│   ├── components/
│   │   └── data_ingestion.py .............. [DataIngestion Class]
│   │       ├── export_collection_as_dataframe()
│   │       ├── export_data_into_feature_store()
│   │       ├── split_data_as_train_test()
│   │       └── initiate_data_ingestion()
│   │
│   ├── entity/
│   │   ├── config_entity.py .............. [Configuration Classes]
│   │   │   ├── TrainingPipelineConfig
│   │   │   └── DataIngestionConfig
│   │   │
│   │   └── artifact_entity.py ............ [Output/Artifact Classes]
│   │       └── DataIngestionArtifact
│   │
│   ├── constant/
│   │   └── training_pipeline/
│   │       └── __init__.py .............. [Pipeline Constants]
│   │           ├── DATABASE: "NetworkSecurityDB"
│   │           ├── COLLECTION: "PhishingDataCollection"
│   │           ├── SPLIT RATIO: 0.2
│   │           └── etc.
│   │
│   ├── exception/
│   │   └── exception.py ................. [Custom Exception Handler]
│   │       └── NetworkSecurityException
│   │
│   ├── logging/
│   │   └── logger.py .................... [Logging Configuration]
│   │
│   └── pipline/
│       └── (Future: Complete pipeline orchestration)
│
├── Network_Data/
│   └── phisingData.csv ................... [Raw Data Source]
│       └── 11,055 records
│
├── Artifacts/ (Generated during execution)
│   └── NetworkSecurity/MM_DD_YYYY_HH_MM_SS/
│       └── data_ingestion/
│           ├── feature_store/
│           │   └── phisingData.csv (Complete dataset)
│           └── ingested/
│               ├── train.csv (80% - 8,844 records)
│               └── test.csv (20% - 2,211 records)
│
├── setup.py .............................. [Package Installation]
├── requirement.txt ....................... [Dependencies]
│   ├── python-dotenv
│   ├── pandas
│   ├── numpy
│   ├── pymongo
│   ├── certifi
│   └── scikit-learn
│
└── .env .................................. [Environment Variables]
    └── MONGO_DB_URL: mongodb+srv://...
```

---

## 🔗 How Scripts Are Interconnected

### **1. Data Flow Connection**

```
CSV File (Network_Data/phisingData.csv)
         ↓
   push_data.py (Step 1)
         ↓
   MongoDB Database
         ↓
   main.py (Step 2)
         ↓
   DataIngestion Component
         ↓
   Artifacts (Train/Test splits)
```

### **2. Class Dependencies**

```
main.py
  │
  ├─ imports: TrainingPipelineConfig (config_entity.py)
  ├─ imports: DataIngestionConfig (config_entity.py)
  ├─ imports: DataIngestion (data_ingestion.py)
  ├─ imports: NetworkSecurityException (exception.py)
  └─ imports: logging (logger.py)

data_ingestion.py
  │
  ├─ uses: DataIngestionConfig (config_entity.py)
  ├─ uses: DataIngestionArtifact (artifact_entity.py)
  ├─ uses: NetworkSecurityException (exception.py)
  ├─ uses: logging (logger.py)
  ├─ uses: constants (training_pipeline/__init__.py)
  └─ connects to: MongoDB
```

### **3. Configuration Chain**

```
TrainingPipelineConfig (Initialized first)
         ↓
    Sets: artifact_dir with timestamp
    Example: "Artifacts/12_04_2025_14_30_45"
         ↓
DataIngestionConfig (Depends on TrainingPipelineConfig)
         ↓
    Builds paths:
    - feature_store_file_path
    - training_file_path
    - testing_file_path
         ↓
DataIngestion (Uses DataIngestionConfig)
         ↓
    Executes 3-step process
```

---

## 🎮 Execution Flow with Example

### **Complete Execution Timeline:**

```
1. User runs: python push_data.py
   ├─ Reads Network_Data/phisingData.csv (11,055 rows)
   ├─ Connects to MongoDB
   └─ Inserts all records ✓

2. User runs: python main.py
   ├─ Creates TrainingPipelineConfig
   │  └─ artifact_dir = "Artifacts/12_04_2025_14_30_45"
   │
   ├─ Creates DataIngestionConfig
   │  └─ database_name = "NetworkSecurityDB"
   │  └─ collection_name = "PhishingDataCollection"
   │  └─ train_test_split_ratio = 0.2
   │
   ├─ Initializes DataIngestion
   │
   ├─ Calls initiate_data_ingestion() which:
   │  ├─ Fetches 11,055 records from MongoDB
   │  ├─ Saves as: Artifacts/12_04_2025_14_30_45/
   │  │            data_ingestion/feature_store/phisingData.csv
   │  ├─ Splits into train/test (80/20)
   │  ├─ Saves train: Artifacts/.../ingested/train.csv (8,844 rows)
   │  └─ Saves test: Artifacts/.../ingested/test.csv (2,211 rows)
   │
   └─ Returns DataIngestionArtifact with file paths

3. Output: Prints artifact information
   └─ Ready for next phases (preprocessing, model training, etc.)
```

---

## 🛠️ Key Components Explained

### **1. Exception Handling (exception.py)**
- Custom `NetworkSecurityException` class
- Captures: error message, file name, line number
- Used throughout for consistent error handling

### **2. Logging (logger.py)**
- Sets up logging to file: `logs/YYYY-MM-DD_HH-MM-SS.log`
- Logs important steps in data processing
- Format: `[timestamp] levelname - message`

### **3. Configuration (config_entity.py)**
- `TrainingPipelineConfig`: Sets up artifact directories
- `DataIngestionConfig`: Configures data paths and parameters
- Follows DRY principle by centralizing configuration

### **4. Artifacts (artifact_entity.py)**
- `DataIngestionArtifact`: Dataclass storing output file paths
- Easy to pass artifact info between pipeline stages

### **5. Constants (training_pipeline/__init__.py)**
- Centralized configuration values
- Easy to modify without code changes
- Examples: database name, split ratio, file names

---

## 📋 Dependencies & Requirements

From `requirement.txt`:
- **python-dotenv**: Load MongoDB URL from .env
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **pymongo**: MongoDB connection
- **certifi**: SSL certificate for secure connection
- **scikit-learn**: `train_test_split()` function

---

## 🔮 Future Pipeline Stages

Based on structure, the project will likely extend with:

```
Data Ingestion ✓
         ↓
Data Preprocessing (TODO)
         ↓
Data Validation (TODO)
         ↓
Model Training (TODO)
         ↓
Model Evaluation (TODO)
         ↓
Model Deployment (TODO)
```

Each new stage would follow the same pattern:
- `components/` - Main logic
- `entity/config_entity.py` - Configuration class
- `entity/artifact_entity.py` - Output dataclass

---

## 🚀 How to Run the Project

```bash
# Step 1: Set up Python environment
python3.11 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
pip install -r requirement.txt

# Step 3: Push data to MongoDB
python push_data.py
# Output: 11055 records inserted to MongoDB

# Step 4: Run ML pipeline
python main.py
# Output: Train/test datasets created in Artifacts/

# Step 5: Check generated files
ls Artifacts/NetworkSecurity/MM_DD_YYYY_HH_MM_SS/data_ingestion/ingested/
# Should show: train.csv, test.csv
```

---

## 📌 Summary

| Component | Purpose | Inputs | Outputs |
|-----------|---------|--------|---------|
| **push_data.py** | Data ingestion to MongoDB | CSV file | Data in MongoDB |
| **main.py** | Entry point for ML pipeline | MongoDB connection | DataIngestionArtifact |
| **DataIngestion** | Extract/transform data | MongoDB data | Train/test CSV files |
| **Config Classes** | Pipeline configuration | Parameters | Configured paths |
| **Exception Handler** | Error management | Exceptions | Formatted error messages |
| **Logger** | Tracking execution | Events | Log file |

All these components work together to create a **reproducible, modular ML pipeline** that can be easily extended with additional stages (preprocessing, training, evaluation, etc.).
