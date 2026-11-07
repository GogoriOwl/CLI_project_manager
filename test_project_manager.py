from project_manager import get_info, add_task, view_task, edit_task, tasks_filter, find_corespondance


def test_get_info_invalid_priority_then_valid(monkeypatch):
    tasks = {}

    inputs = iter([
        "Learn SQL",
        "Practice joins",
        "very important",
        "high",
        "backend",
        "python",
        "todo"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    result = get_info(tasks)

    assert result[0] == "Learn SQL"
    assert result[1] == "Practice joins"
    assert result[2] == "high"
    assert result[2] != "very important"
    assert result[3] == ["backend", "python"]
    assert result[4] == "todo"


def test_add_task():
    result = add_task(
        3,
        "Learn SQL",
        "Practice SELECT, WHERE and JOIN",
        "high",
        ["sql", "backend"],
        "todo"
    )

    assert "task-3" in result
    assert result["task-3"]["title"] == "Learn SQL"
    assert result["task-3"]["description"] == "Practice SELECT, WHERE and JOIN"
    assert result["task-3"]["priority"] == "high"
    assert result["task-3"]["tags"] == ["sql", "backend"]
    assert result["task-3"]["status"] == "todo"


def test_view_task():
    tasks = {
    "task-0": {
        "title": "Learn Python",
        "description": "Practice functions and pytest",
        "priority": "high",
        "tags": ["python", "backend"],
        "status": "todo"
    },

    "task-1": {
        "title": "Go to gym",
        "description": "Leg workout",
        "priority": "medium",
        "tags": ["health", "sport"],
        "status": "in progress"
    },

    "task-2": {
        "title": "Study SQL",
        "description": "Practice SELECT, WHERE and JOIN",
        "priority": "high",
        "tags": ["sql", "database", "backend"],
        "status": "todo"
    }
    }

    searched = view_task(tasks, 1)

    assert searched["title"] == "Go to gym"
    assert searched["description"] == "Leg workout"
    assert searched["priority"] == "medium"


def test_edit_task():
       tasks = {
        "task-0": {
            "title": "Learn Python",
            "description": "Practice functions and pytest",
            "priority": "high",
            "tags": ["python", "backend"],
            "status": "todo"
        },
    
        "task-1": {
            "title": "Go to gym",
            "description": "Leg workout",
            "priority": "medium",
            "tags": ["health", "sport"],
            "status": "in progress"
        },
    
        "task-2": {
            "title": "Study SQL",
            "description": "Practice SELECT, WHERE and JOIN",
            "priority": "high",
            "tags": ["sql", "database", "backend"],
            "status": "todo"
        }}

       edited_task = edit_task(tasks, 1, "title", "don't go to gym")
       assert edited_task["title"] == "don't go to gym"


def test_tasks_filter():
       tasks = {
             "task-0": {
                 "title": "Learn Python",
                 "description": "Practice functions and pytest",
                 "priority": "high",
                 "tags": ["python", "backend"],
                 "status": "todo"
             },
         
             "task-1": {
                 "title": "Go to gym",
                 "description": "Leg workout",
                 "priority": "medium",
                 "tags": ["health", "sport"],
                 "status": "in progress"
             },
         
             "task-2": {
                 "title": "Study SQL",
                 "description": "Practice SELECT, WHERE and JOIN",
                 "priority": "high",
                 "tags": ["sql", "database", "backend"],
                 "status": "todo"
             }}


       filtered = tasks_filter(tasks, "high")
       assert len(filtered) == 2
       assert "task-0" in filtered
       assert "task-2" in filtered
       assert "task-1" not in filtered

       assert filtered["task-0"]["priority"] == "high"
       assert filtered["task-2"]["priority"] == "high"

def test_find_corespondance():
     tasks = {
            "task-0": {
                      "title": "Learn Python",
                      "description": "Practice functions and pytest",
                      "priority": "high",
                      "tags": ["python", "backend"],
                      "status": "todo"
                  },
              
            "task-1": {
                      "title": "Go to gym",
                      "description": "Leg workout",
                      "priority": "medium",
                      "tags": ["health", "sport"],
                      "status": "in progress"
                  },
              
            "task-2": {
                      "title": "Study SQL",
                      "description": "Practice SELECT, WHERE and JOIN",
                      "priority": "high",
                      "tags": ["sql", "database", "backend"],
                      "status": "todo"
                  }}

     search = find_corespondance(tasks, "practice")

     assert len(search) == 2
     assert "task-0" in search
     assert "task-2" in search
     assert "task-1" not in search