
from pywebio import*
from pywebio.input import*
from pywebio.output import*
from pywebio import start_server
from pywebio import config

def app():
    put_html("""/
             <img src="https://i.pinimg.com/750x/e8/0c/d7/e80cd70bc152a8da30d6741743bb14fb.jpg" alt="try goodies"
             style="width: 900px , height: 200px">
            <h3 id='h3'>TRY GOODIES</h3>
             <p id='para'>WELCOME</p>
             <ul>
                <li>SOMETHING NEW IS COMING SOON</li>
                <li>IN SWEETS WE ARE THE BEST</li>
             </ul>
             <details id='y'>
                <summary>مروا هني قبل لا تطلبون</summary>
                <P> DELIVERY TAKES 2h-3h</P>
                <P> ONLINE PAYMENT ONLY</P>
                <P>و نوعدكم مرح تكون أول و أخر مرة تطلبون</P>
                <P>لا تنسوون تسوولنا FOLLOW </P>
             </details>
""")

start_server(app , port=34345 , debug=True)