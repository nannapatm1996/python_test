package com.example.python_test;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        String objectTest = "test Object pass from app to python";

        Python py = Python.getInstance();
        PyObject pyf = py.getModule("API_AndroidVer"); //name of python file
        PyObject obj = pyf.callAttr("classify_image","027.jpg"); //name of function

        textView = findViewById(R.id.text1);
        textView.setText(obj.toString());
    }
}
