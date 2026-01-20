P='clear'
O='room_id'
H=input
G=str
E=True
import requests as I,json,os,time as J,threading as Q
from rich.console import Console as R
from rich.table import Table
from rich.panel import Panel
K='https://script.google.com/macros/s/AKfycbwc99XN6uHKeTIvu2LdMEYf3B4hvhHDc7iAVqATJpjCUXk1XE_VfIKap3Dh7236Lc40/exec'
C=R()
A=[]
def L(room_id):
	try:A=I.get(K,params={O:room_id},timeout=5);return A.json()
	except:return
def F(room_id,messages):
	D=messages;os.system(P);C.print(Panel(f"💬 [bold cyan]ROOM: {room_id}[/bold cyan]",style='blue'));A=Table(expand=E,border_style='dim',box=None);A.add_column('Waktu',style='dim cyan',width=7);A.add_column('User',style='bold yellow',width=12);A.add_column('Pesan',style='white')
	if D:
		for B in D[-15:]:A.add_row(G(B[0]),G(B[1]),G(B[3]))
	C.print(A);C.print('[dim]------------------------------------------[/dim]')
def S(room_id):
	C=room_id;global A
	while E:
		B=L(C)
		if B is not None and B!=A:A=B;F(C,B)
		J.sleep(4)
def T(user,room_id,message):
	A={'user':user,O:room_id,'message':message}
	try:I.post(K,data=json.dumps(A))
	except:pass
os.system(P)
C.print('[bold green]TERMUX CHAT LOADED...[/bold green]')
M=H('Nama: ')
B=H('ID Ruang: ')
N=L(B)
A=N if N else[]
F(B,A)
Q.Thread(target=S,args=(B,),daemon=E).start()
while E:
	D=H('>> ')
	if D.lower()=='q':break
	elif D.strip()!='':T(M,B,D);U=J.strftime('%H:%M');A.append([U,M,B,D]);F(B,A)