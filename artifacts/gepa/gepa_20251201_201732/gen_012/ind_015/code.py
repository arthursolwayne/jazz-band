
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # Standard resolution

# Create instruments
drum_program = pretty_midi.programs.Program(0, 0)  # Drums
bass_program = pretty_midi.programs.Program(33, 0)  # Electric Bass
piano_program = pretty_midi.programs.Program(0, 0)  # Acoustic Piano
sax_program = pretty_midi.programs.Program(64, 0)  # Tenor Saxophone

# Add instruments
drum_instrument = pretty_midi.Instrument(program=drum_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define time per beat and per bar
beats_per_bar = 4
notes_per_beat = 4  # quarter note = 1 beat, so 4 notes per beat at 160 BPM
time_per_beat = 0.375  # seconds per beat at 160 BPM
time_per_bar = time_per_beat * beats_per_bar

# Bar 1: Drums only – kick on 1 & 3, snare on 2 & 4, hihat on every 8th
# Note timings: 0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5 (end of bar)
bar1_start = 0.0
bar1_end = time_per_bar

# Kick (1 & 3)
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.05),
              pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.8)]
drum_instrument.notes.extend(kick_notes)

# Snare (2 & 4)
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.4),
               pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.15)]
drum_instrument.notes.extend(snare_notes)

# Hi-hat (every 8th)
hihat_notes = []
for i in range(8):
    hihat_start = bar1_start + i * 0.1875
    hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.025))
drum_instrument.notes.extend(hihat_notes)

# Bar 2: Bass and Piano – Dm7, Gm7, Cm7, F7
bar2_start = bar1_end
bar2_end = bar1_end + time_per_bar

# Bass line: D (root), F (minor 3rd), C (fifth), G (chromatic up from F to G)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=bar2_start, end=bar2_start + 0.25),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=bar2_start + 0.25, end=bar2_start + 0.5),  # F2
    pretty_midi.Note(velocity=80, pitch=57, start=bar2_start + 0.5, end=bar2_start + 0.75),  # C2
    pretty_midi.Note(velocity=80, pitch=58, start=bar2_start + 0.75, end=bar2_start + 1.0),  # G2
]
bass_instrument.notes.extend(bass_notes)

# Piano: Open voicings, each bar has a different chord
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start, end=bar2_start + 0.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start, end=bar2_start + 0.25),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start, end=bar2_start + 0.25),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=bar2_start, end=bar2_start + 0.25),  # C5
]
piano_instrument.notes.extend(piano_notes)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.5, end=bar2_start + 0.75),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 0.5, end=bar2_start + 0.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=bar2_start + 0.5, end=bar2_start + 0.75),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=bar2_start + 0.5, end=bar2_start + 0.75),  # F5
]
piano_instrument.notes.extend(piano_notes)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=bar2_start + 1.0, end=bar2_start + 1.25),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=bar2_start + 1.0, end=bar2_start + 1.25),  # Eb5
    pretty_midi.Note(velocity=90, pitch=76, start=bar2_start + 1.0, end=bar2_start + 1.25),  # G5
    pretty_midi.Note(velocity=90, pitch=77, start=bar2_start + 1.0, end=bar2_start + 1.25),  # Bb5
]
piano_instrument.notes.extend(piano_notes)

# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=bar2_start + 1.25, end=bar2_start + 1.5),  # F5
    pretty_midi.Note(velocity=90, pitch=79, start=bar2_start + 1.25, end=bar2_start + 1.5),  # A5
    pretty_midi.Note(velocity=90, pitch=81, start=bar2_start + 1.25, end=bar2_start + 1.5),  # C6
    pretty_midi.Note(velocity=90, pitch=83, start=bar2_start + 1.25, end=bar2_start + 1.5),  # E6
]
piano_instrument.notes.extend(piano_notes)

# Bar 2: Sax – start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.15, end=bar2_start + 0.35),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.35, end=bar2_start + 0.55),  # F4
]
sax_instrument.notes.extend(sax_notes)

# Bar 4: Sax – return to finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.15, end=bar2_start + 1.35),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.35, end=bar2_start + 1.5),   # F4
]
sax_instrument.notes.extend(sax_notes)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
