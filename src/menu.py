import tkinter as tk


class ApplicationBarreMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface avec Barre de Menu")
        self.root.geometry("700x450")
        self.root.configure(bg="#f8f9fa")

        # --- 1. LA BARRE DE MENU (HEADER) ---
        self.header = tk.Frame(self.root, bg="#2c3e50", height=60)
        self.header.pack(fill="x", side="top")
        self.header.pack_propagate(False)  # Garde la hauteur fixe à 60px

        # Titre
        self.logo = tk.Label(
            self.header,
            fg="#3498db",
            bg="#2c3e50",
            font=("Arial", 14, "bold"),
            padx=20,
        )
        self.logo.pack(side="left")

        # --- 2. LES BOUTONS DE NAVIGATION ---
        # On définit une liste d'onglets
        onglets = ["Base de donnée", "équipe", "Tournoi"]

        for nom in onglets:
            btn = tk.Button(
                self.header,
                text=nom,
                font=("Arial", 10, "bold"),
                bg="#2c3e50",
                fg="white",
                relief="flat",
                activebackground="#34495e",
                activeforeground="#3498db",
                cursor="hand2",
                padx=15,
                command=lambda n=nom: self.changer_page(n),
            )
            btn.pack(side="left", fill="y")

        # --- 3. ZONE DE CONTENU ---
        self.zone_contenu = tk.Frame(self.root, bg="#ffffff", bd=0)
        self.zone_contenu.pack(expand=True, fill="both", padx=20, pady=20)

        self.label_titre_page = tk.Label(
            self.zone_contenu,
            text="Bienvenue",
            font=("Arial", 18),
            bg="#ffffff",
            fg="#2c3e50",
        )
        self.label_titre_page.pack(pady=20)

        self.label_description = tk.Label(
            self.zone_contenu,
            text="Sélectionnez une option dans la barre du haut.",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#7f8c8d",
        )
        self.label_description.pack()

    def changer_page(self, nom_page):
        """Met à jour l'affichage selon le bouton cliqué."""
        print(f"Navigation vers : {nom_page}")
        self.label_titre_page.config(text=nom_page)

        if nom_page == "Quitter":
            self.root.quit()


# --- LANCEMENT ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationBarreMenu(root)
    root.mainloop()
