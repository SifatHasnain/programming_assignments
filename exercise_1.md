1. Use case: Send Asset to LegALpprove when starting the third step of a task using the asset creation workflow (External Sub Step) in Welcome:

    a. external_sub_step_started [Webhook API](https://developers.welcomesoftware.com/webhooks.html?hash=kc67x#section/External-Work-Management-events/external_sub_step_started)

    b. POST /assets [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Library/paths/~1assets/post)

    Input: 

    Data

        {
            "key": "string",
            "title": "sample_image.png"
        }

    Output: 

        {
            "id": "5d7f910551b00a722e0418830cee6631",
            "title": "sample_image.png",
            "type": "image",
            "mime_type": "image/png",
            "created_at": "2019-10-06T13:15:30Z",
            "modified_at": "2019-10-07T13:15:30Z",
            "folder_id": "6bb8db20a5b611ebae319b7c541b1a5a",
            "file_location": "/all assets/important assets",
            "content": {
                "type": "url",
                "value": "http://images.welcomesoftware.com/Zz0xODQ3NDU3Y2Y2YmYzOTlmNjkyOTgyZDY3Y2I3YWM2OA==S"
            },
            "labels": [
                {
                "group": {
                    "id": "2467e583a60e23fda2b89db81a453cd2",
                    "name": "Content Format"
                },
                "values": [
                    {
                    "id": "71c378f3fee3d822759d1bdc2aab628c",
                    "name": "Photos"
                    }
                ]
                }
            ],
            "links": {
                "self": "https://api.welcomesoftware.com/v3/images/5d7f910551bw0a722e0418830cee6631"
            },
            "owner_organization_id": "5108c3a9becac35915111191"
        }

    c. task_asset_added [Webhook](https://developers.welcomesoftware.com/webhooks.html?hash=kc67x#section/Task-events/task_asset_added)

2. Use case: Task Asset Label data should be retrieved and pushed to LegALpprove:

    a. retrieve [Webhook API](https://developers.welcomesoftware.com/webhooks.html?hash=kc67x#section/External-Work-Management-events/external_sub_step_started)

    b. POST /tasks/{id}/assets [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Tasks/paths/~1tasks~1{id}~1assets/post)


    Input: 

    Parameter:

    • id : 5d7f910551b00a722e0418830cee6632 (Asset ID)

    Data

        {
            "key": "string",
            "title": "sample_image.png"
        }

    Output:

        {
            "id": "5d7f910551b00a722e0418830cee6631",
            "title": "sample_image.png",
            "type": "image",
            "mime_type": "image/png",
            "created_at": "2019-10-06T13:15:30Z",
            "modified_at": "2019-10-07T13:15:30Z",
            "content": {
                "type": "url",
                "value": "http://images.welcomesoftware.com/Zz0xODQ3NDU3Y2Y2YmYzOTlmNjkyOTgyZDY3Y2I3YWM2OA==S"
            },
            "labels": [
                {
                "group": {
                    "id": "2467e583a60e23fda2b89db81a453cd2",
                    "name": "Content Format"
                },
                "values": [
                    {
                    "id": "71c378f3fee3d822759d1bdc2aab628c",
                    "name": "Photos"
                    }
                ]
                }
            ],
            "links": {
                "self": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9/image/5d7f910551b00a722e0418830cee6631",
                "task": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9",
                "drafts": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9/assets/5d7f910551b00a722e0418830cee6631/drafts",
                "web_urls": {
                "self": "https://app.welcomesoftware.com/cloud/taskv3/5f857f30e1c4a2038d6179e9?contentTabGuid=5d7f910551b00a722e0418830cee6631",
                "task": "https://app.welcomesoftware.com/cloud/taskv3/5f857f30e1c4a2038d6179e9",
                "drafts": "https://app.welcomesoftware.com/cloud/task/5f857f30e1c4a2038d6179e9/image/5d7f910551b00a722e0418830cee6631"
                }
            }
        } 

3. Use case: Task Custom Fields data should be retrieved and shared to LegALpprove

   GET /tasks/{task_id}/custom-fields/{custom_field_id} [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Tasks/paths/~1tasks~1{id}~1custom-fields/get)

   Parameter:

   • task-id = 9nu8ue9wf8u9nusd9q

   Output:

    {
        "data": [
            {
            "id": "9nu8ue9wf8u9nusd9q",
            "name": "My Dropdown",
            "type": "dropdown",
            "values": [
                {
                "id": "1nu8ue9wf8u9nusd9u",
                "name": "Some text"
                }
            ],
            "links": {
                "self": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9/custom-fields/9nu8ue9wf8u9nusd9q",
                "choices": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9/custom-fields/9nu8ue9wf8u9nusd9q/choices"
            }
            }
        ],
        "pagination": {
            "next": "https://api.welcomesoftware.com/v3/tasks/5f857f30e1c4a2038d6179e9/custom-fields?offset=10&page_size=10",
            "previous": null
        }
    }

4. Use case: Update the External Work Information of the third step (External Sub Step) in Welcome’s workflow.

    a. PATCH /tasks/{task_id}/steps/{step_id}/sub-steps/{sub_step_id}/external-work [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Tasks/paths/~1tasks~1{task_id}~1steps~1{step_id}~1sub-steps~1{sub_step_id}~1external-work/patch)

    Input: 

    Parameter:
    - task_id: 7d7f910551b00a722e0418830cee6612 
    - step_id: 3
    - sub_step_id: 700f910551b00a722e0418830cee6612

    Data:

        {
            "identifier": "MY-PROJ-123",
            "title": "A very important ticket",
            "status": "In Progress",
            "url": "https://example.com/some-project/MY-PROJ-123"
        }

    Output:

        {
            "identifier": "MY-PROJ-123",
            "title": "A very important ticket",
            "status": "In Progress",
            "url": "https://example.com/some-project/MY-PROJ-123",
            "external_system": "jira",
            "links": {
                "self": "https://api.welcomesoftware.com/v3/tasks/5d7f910551b00a722e0418830cee6631/steps/32982hf94j98cnr48034nv035/sub-steps/9n390809r384nv503459075034nv5/external-work"
            }
        }

5. Usecase: Update the third step (External Sub Step) due date in Welcome based on the LegALpprove due date.

    external_sub_step_modified [Webhook](https://developers.welcomesoftware.com/webhooks.html?hash=kc67x#section/External-Work-Management-events/external_sub_step_modified)

6. Usecase: Create a Comment on the third step (External Sub Step) in Welcome’s workflow to notify the user that the asset is being reviewed. 

    a. external_sub_step_comment_added

    b. POST /tasks/{task_id}/steps/{step_id}/sub-steps/{sub_step_id}/comments [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Tasks/paths/~1tasks~1{task_id}~1steps~1{step_id}~1sub-steps~1{sub_step_id}~1comments/post)

    Input:

    Parameter:

    - task_id: 7d7f910551b00a722e0418830cee6612 
    - step_id: 3
    - sub_step_id: 700f910551b00a722e0418830cee6612

    Data:

        {
            "value": "Comment mentioning @[Organization User](https://api.welcomesoftware.com/v3/users/5fe38aeb574b52a62a089238)",
            "attachments": [
                {
                "key": "ce8995aea58b11ea8cd90242ac120005",
                "name": "sample_image.png"
                }
            ]
        }
    Output:
        
        {
            "id": "5fe38c39574b52a62a089239",
            "value": "Well done!",
            "is_resolved": false,
            "created_at": "2020-10-06T13:15:30Z",
            "modified_at": "2020-10-06T14:15:30Z",
            "attachments": [
                {
                "id": "a113667245d111eb8945000c",
                "name": "sample.png",
                "url": "https://files.welcomesoftware.com/download/96c314a645d111eb8945000c291b51d4?token="
                }
            ],
            "links": {
                "self": "https://api.welcomesoftware.com/v3/tasks/5d7f910551b00a722e0418830cee5534/steps/6d7f910551b00a722e0418830cee5564/sub-steps/9c7f910551b00a722e0418830cee2564",
                "comment_by": "https://api.welcomesoftware.com/v3/users/5fe38eea574b52a62a08923a",
                "task": "https://api.welcomesoftware.com/v3/tasks/5d7f910551b00a722e0418830cee5534",
                "sub_step": "https://api.welcomesoftware.com/v3/tasks/5d7f910551b00a722e0418830cee5534/steps/6d7f910551b00a722e0418830cee5564/sub-steps/9c7f910551b00a722e0418830cee2564"
            }
        }

7. Upload a new version of the asset to the task in Welcome.

    POST /assets/{asset_id}/versions [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Library/paths/~1assets~1{asset_id}~1versions/post)

    Input:

    Parameter:

    asset_id: 5f857f30e1c4a2038d6179e9

    Data:

        {
            "key": "string",
            "title": "sample_image.png"
        }

    Output:

        {
            "version_number": 2,
            "asset_id": "5d7f910551b00a722e0418830cee6631",
            "title": "sample_image.png",
            "type": "image",
            "mime_type": "image/png",
            "created_at": "2019-10-06T13:15:30Z",
            "content": {
                "type": "url",
                "value": "http://images.welcomesoftware.com/Zz0xODQ3NDU3Y2Y2YmYzOTlmNjkyOTgyZDY3Y2I3YWM2OA==S"
            },
            "links": {
                "asset": "https://api.welcomesoftware.com/v3/images/5d7f910551b00a722e0418830cee6631"
            }
        }

8. Close the third step (External Sub Step) in Welcome’s workflow. 
 
a. DELETE /tasks/{task_id}/steps/{step_id}/sub-steps/{sub_step_id}/comments/{comment_id} [Endpoint](https://developers.welcomesoftware.com/openapi.html?hash=kc67x#tag/Tasks/paths/~1tasks~1{task_id}~1steps~1{step_id}~1sub-steps~1{sub_step_id}~1comments~1{comment_id}/delete)

    task_id(required)(string)
    Example: 7d7f910551b00a722e0418830cee6612

    step_id(required)(string)
    Example: 897f910551b00a722e0418830cee6612

    sub_step_id(required)(string)
    Example: 700f910551b00a722e0418830cee6612

    comment_id(required)(string)
    Example: 5fe3886c574b52a62a089237