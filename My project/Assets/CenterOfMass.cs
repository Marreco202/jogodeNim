// Expose center of mass to allow it to be set from
// the inspector.
using UnityEngine;
using System.Collections;

public class CenterOfMass : MonoBehaviour
{
    public Vector3 com;
    public Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        rb.centerOfMass = com;
    }
}