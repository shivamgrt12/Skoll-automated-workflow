Input/<task_id>/
│
├── PROMPT.md
├── rubric.json
├── README.md
├── TRUTH.md           
├── persona/             
│  ├── AGENTS.md          
│  ├── SOUL.md            
│  ├── MEMORY.md          
│  ├── IDENTITY.md        
│  ├── USER.md            
│  ├── TOOLS.md           
│  └── HEARTBEAT.md       
│
├── data/               
│
├── mock_data/         
│  └── <api></api>-api/*.csv|*.json 
│
├── task.yaml
│── inject
        └──stage0
│             └── mutations.json
  ── test_weights.json   ★ the REQUIRED opt-in signal {test_name: weight}
└── test_outputs.py
