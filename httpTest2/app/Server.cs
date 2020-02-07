using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

//
// Python に送信するデータ
//
[System.Serializable]
public struct MyData {
    public float x;
    public float y;
    public float z;
}

//
// Python と通信するためのサーバーを建てる
//

public class Server : MonoBehaviour
{
    private HttpListener httpListener;
    private Thread thread;
    private Vector3 position;
    private bool detach;

    // Start is called before the first frame update
    void Start()
    {
        this.httpListener = new HttpListener();
        httpListener.Prefixes.Add("http://localhost:8080/");
        httpListener.Start();
        this.detach = false;
        this.thread = new Thread(ServerRun);
        thread.Start();
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.W))
        {
            transform.position += Vector3.up;
        } else if(Input.GetKeyDown(KeyCode.S))
        {
            transform.position += Vector3.down;
        }
        if(Input.GetKeyDown(KeyCode.A))
        {
            transform.position += Vector3.left;
        } else if(Input.GetKeyDown(KeyCode.D))
        {
            transform.position += Vector3.right;
        }
        this.position = transform.position;
    }

    void OnDestroy()
    {
        Debug.Log("Server exit.");
        this.detach = true;
    }

    private void ServerRun()
    {
        while(!detach)
        {
            httpListener.BeginGetContext(OnRequested, null);
            System.Threading.Thread.Yield();
        }
        httpListener.BeginGetContext(OnRequested, null);
    }

    private void OnRequested(IAsyncResult result)
    {
        if(!httpListener.IsListening)
        {
            return;
        }
        Debug.Log("OnRequested!");
        HttpListenerContext context = httpListener.EndGetContext(result);
        HttpListenerRequest req = context.Request;
        HttpListenerResponse res = context.Response;
        Debug.Log(req.QueryString);

        if(this.detach)
        {
            //終了メッセージを送信する
            using (var sw = new StreamWriter(res.OutputStream))
                sw.WriteLine("Goodnight");
        } else
        {
            //まだ生きてたら情報を渡す
            MyData data;
            data.x = position.x;
            data.y = position.y;
            data.z = position.z;
            using (var sw = new StreamWriter(res.OutputStream))
                sw.Write(JsonUtility.ToJson(data));
        }
        res.Close();
    }
}
