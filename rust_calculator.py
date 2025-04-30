import customtkinter as ctk

# Define recycling values for components
RECYCLING_VALUES = {
    "road.sign": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.pipe": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.blade": {"scrap": 2, "hqm": 0, "metal": 18},
    "metal.spring": {"scrap": 12, "hqm": 2, "metal": 0},
    "smg.body": {"scrap": 18, "hqm": 2, "metal": 0},
    "sar.body": {"scrap": 18, "hqm": 2, "metal": 90},
    "rifle.body": {"scrap": 30, "hqm": 2, "metal": 0},
    "sheet.metal": {"scrap": 9, "hqm": 2, "metal": 120},
    "tech.trash": {"scrap": 24, "hqm": 2, "metal": 0}
}

class RustCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rust Road Sign Calculator")
        self.geometry("500x400")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configure main frame grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.grid(row=0, column=0, columnspan=2, padx=30, pady=30, sticky="ew")
        
        # Road Signs input
        self.signs_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Road Signs:"
        )
        self.signs_label.grid(row=0, column=0, padx=15, pady=10)

        self.signs_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of signs"
        )
        self.signs_entry.grid(row=0, column=1, padx=15, pady=10)

        # Metal Pipes input
        self.pipes_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Metal Pipes:"
        )
        self.pipes_label.grid(row=1, column=0, padx=15, pady=10)

        self.pipes_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of pipes"
        )
        self.pipes_entry.grid(row=1, column=1, padx=15, pady=10)

        # Metal Blades input
        self.blades_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Metal Blades:"
        )
        self.blades_label.grid(row=2, column=0, padx=15, pady=10)

        self.blades_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of blades"
        )
        self.blades_entry.grid(row=2, column=1, padx=15, pady=10)

        # Metal Springs input
        self.springs_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Metal Springs:"
        )
        self.springs_label.grid(row=3, column=0, padx=15, pady=10)

        self.springs_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of springs"
        )
        self.springs_entry.grid(row=3, column=1, padx=15, pady=10)

        # SMG Body input
        self.smg_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of SMG Bodies:"
        )
        self.smg_label.grid(row=4, column=0, padx=15, pady=10)

        self.smg_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of SMG bodies"
        )
        self.smg_entry.grid(row=4, column=1, padx=15, pady=10)

        # SAR Body input
        self.sar_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of SAR Bodies:"
        )
        self.sar_label.grid(row=5, column=0, padx=15, pady=10)

        self.sar_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of SAR bodies"
        )
        self.sar_entry.grid(row=5, column=1, padx=15, pady=10)

        # Rifle Body input
        self.rifle_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Rifle Bodies:"
        )
        self.rifle_label.grid(row=6, column=0, padx=15, pady=10)

        self.rifle_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of rifle bodies"
        )
        self.rifle_entry.grid(row=6, column=1, padx=15, pady=10)

        # Sheet Metal input
        self.sheet_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Sheet Metal:"
        )
        self.sheet_label.grid(row=7, column=0, padx=15, pady=10)

        self.sheet_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of sheet metal"
        )
        self.sheet_entry.grid(row=7, column=1, padx=15, pady=10)

        # Tech Trash input
        self.tech_label = ctk.CTkLabel(
            self.input_frame,
            text="Number of Tech Trash:"
        )
        self.tech_label.grid(row=8, column=0, padx=15, pady=10)

        self.tech_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter number of tech trash"
        )
        self.tech_entry.grid(row=8, column=1, padx=15, pady=10)

        # Calculate button
        self.calc_button = ctk.CTkButton(
            self.main_frame,
            text="Calculate",
            command=self.calculate_resources
        )
        self.calc_button.grid(row=1, column=0, columnspan=2, padx=30, pady=25)

        # Results frame
        self.results_frame = ctk.CTkFrame(self.main_frame)
        self.results_frame.grid(row=2, column=0, columnspan=2, padx=30, pady=30, sticky="ew")

        # Results labels
        self.scrap_label = ctk.CTkLabel(
            self.results_frame,
            text="Scrap: 0"
        )
        self.scrap_label.grid(row=0, column=0, padx=20, pady=10)

        self.hqm_label = ctk.CTkLabel(
            self.results_frame,
            text="HQM: 0"
        )
        self.hqm_label.grid(row=0, column=1, padx=20, pady=10)

        self.metal_label = ctk.CTkLabel(
            self.results_frame,
            text="Metal Fragments: 0"
        )
        self.metal_label.grid(row=0, column=2, padx=20, pady=10)

    def calculate_resources(self):
        try:
            # Get numbers from input
            num_signs = int(self.signs_entry.get() or 0)
            num_pipes = int(self.pipes_entry.get() or 0)
            num_blades = int(self.blades_entry.get() or 0)
            num_springs = int(self.springs_entry.get() or 0)
            num_smg = int(self.smg_entry.get() or 0)
            num_sar = int(self.sar_entry.get() or 0)
            num_rifle = int(self.rifle_entry.get() or 0)
            num_sheet = int(self.sheet_entry.get() or 0)
            num_tech = int(self.tech_entry.get() or 0)
            
            # Calculate total resources
            total_scrap = (num_signs * RECYCLING_VALUES["road.sign"]["scrap"] +
                         num_pipes * RECYCLING_VALUES["metal.pipe"]["scrap"] +
                         num_blades * RECYCLING_VALUES["metal.blade"]["scrap"] +
                         num_springs * RECYCLING_VALUES["metal.spring"]["scrap"] +
                         num_smg * RECYCLING_VALUES["smg.body"]["scrap"] +
                         num_sar * RECYCLING_VALUES["sar.body"]["scrap"] +
                         num_rifle * RECYCLING_VALUES["rifle.body"]["scrap"] +
                         num_sheet * RECYCLING_VALUES["sheet.metal"]["scrap"] +
                         num_tech * RECYCLING_VALUES["tech.trash"]["scrap"])
            total_hqm = (num_signs * RECYCLING_VALUES["road.sign"]["hqm"] +
                        num_pipes * RECYCLING_VALUES["metal.pipe"]["hqm"] +
                        num_blades * RECYCLING_VALUES["metal.blade"]["hqm"] +
                        num_springs * RECYCLING_VALUES["metal.spring"]["hqm"] +
                        num_smg * RECYCLING_VALUES["smg.body"]["hqm"] +
                        num_sar * RECYCLING_VALUES["sar.body"]["hqm"] +
                        num_rifle * RECYCLING_VALUES["rifle.body"]["hqm"] +
                        num_sheet * RECYCLING_VALUES["sheet.metal"]["hqm"] +
                        num_tech * RECYCLING_VALUES["tech.trash"]["hqm"])
            total_metal = (num_signs * RECYCLING_VALUES["road.sign"]["metal"] +
                          num_pipes * RECYCLING_VALUES["metal.pipe"]["metal"] +
                          num_blades * RECYCLING_VALUES["metal.blade"]["metal"] +
                          num_springs * RECYCLING_VALUES["metal.spring"]["metal"] +
                          num_smg * RECYCLING_VALUES["smg.body"]["metal"] +
                          num_sar * RECYCLING_VALUES["sar.body"]["metal"] +
                          num_rifle * RECYCLING_VALUES["rifle.body"]["metal"] +
                          num_sheet * RECYCLING_VALUES["sheet.metal"]["metal"] +
                          num_tech * RECYCLING_VALUES["tech.trash"]["metal"])
            
            # Update results
            self.update_results(total_scrap, total_hqm, total_metal)
            
        except ValueError:
            # Show error if input is not a valid number
            self.update_results(0, 0, 0)
            print("Please enter a valid number")

            


    def update_results(self, scrap, hqm, metal):
        self.scrap_label.configure(text=f"Scrap: {scrap}")
        self.hqm_label.configure(text=f"HQM: {hqm}")
        self.metal_label.configure(text=f"Metal Fragments: {metal}")

if __name__ == "__main__":
    app = RustCalculator()
    app.mainloop()
