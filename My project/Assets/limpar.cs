using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class limpar : MonoBehaviour
{
    public Sprite jogolimpo;
    private SpriteRenderer spriteRenderer;
    // Start is called before the first frame update
    void Start()
    {
        spriteRenderer.sprite = jogolimpo;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
