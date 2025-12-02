
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature to D major
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]  # 2 = D major

# Define the tempo
pm.time_signature_changes[0].tempo = 160

# Define MIDI note numbers
D2 = 38  # C2 is 36, D2 is 38
D4 = 62
E4 = 64
F4 = 65
G4 = 67
A4 = 69
B4 = 71
C5 = 72
D5 = 74
F5 = 76
G5 = 78

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.PIANO)
sax = Instrument(program=Program.SAXOPHONE)

pm.instruments = [drums, bass, piano, sax]

# --- DRUMS: Little Ray (Bar 1 only, not filled in first bar) ---
# Kick on beats 1 and 3
# Snare on 2 and 4
# Hihat on every 8th
# Bar is 1.5 seconds, so each beat is 0.375s, each 8th is 0.1875s

def add_drums():
    bar_length = 1.5
    beat = 0.375
    eighth = 0.1875
    kick_notes = [0, 2]  # beats 1 and 3
    snare_notes = [1, 3]  # beats 2 and 4
    hihat_notes = [0, 1, 2, 3, 4, 5, 6, 7]  # every eighth

    for note in kick_notes:
        note_time = note * beat
        note_obj = Note(36, 100, note_time, note_time + 0.1)
        drums.notes.append(note_obj)

    for note in snare_notes:
        note_time = note * beat
        note_obj = Note(38, 100, note_time, note_time + 0.1)
        drums.notes.append(note_obj)

    for note in hihat_notes:
        note_time = note * eighth
        note_obj = Note(42, 90, note_time, note_time + 0.05)
        drums.notes.append(note_obj)

# --- BASS: Marcus (Walking line with chromatic approaches) ---
def add_bass():
    # Bar 1: D2 -> D2 -> E2 -> F2 (chromatic walk)
    # Bar 2: G2 -> A2 -> B2 -> C3 (chromatic)
    # Bar 3: D3 -> D3 -> E3 -> F3
    # Bar 4: G3 -> A3 -> B3 -> C4

    def bass_notes(start, chromatic_steps):
        notes = [start]
        for i in range(chromatic_steps):
            notes.append(notes[-1] + 1)
        return notes

    bar_length = 1.5
    beat = 0.375

    # Bar 1
    for i, note in enumerate(bass_notes(D2, 3)):
        time = i * beat
        note_obj = Note(note, 100, time, time + 0.1)
        bass.notes.append(note_obj)

    # Bar 2
    for i, note in enumerate(bass_notes(G2, 3)):
        time = 1.5 + i * beat
        note_obj = Note(note, 100, time, time + 0.1)
        bass.notes.append(note_obj)

    # Bar 3
    for i, note in enumerate(bass_notes(D3, 3)):
        time = 3.0 + i * beat
        note_obj = Note(note, 100, time, time + 0.1)
        bass.notes.append(note_obj)

    # Bar 4
    for i, note in enumerate(bass_notes(G3, 3)):
        time = 4.5 + i * beat
        note_obj = Note(note, 100, time, time + 0.1)
        bass.notes.append(note_obj)

# --- PIANO: Diane (Open voicings, resolve on last bar) ---
def add_piano():
    # Bar 1: D7 (D, F#, A, C)
    # Bar 2: G7 (G, B, D, F)
    # Bar 3: A7 (A, C#, E, G)
    # Bar 4: D7 (resolve)

    def chord_notes(root, chord_type):
        if chord_type == "7":
            return [root, root + 4, root + 7, root + 10]
        return []

    bar_length = 1.5
    beat = 0.375

    # Bar 1: D7
    for note in chord_notes(D4, "7"):
        time = 0
        note_obj = Note(note, 80, time, time + 0.1)
        piano.notes.append(note_obj)

    # Bar 2: G7
    for note in chord_notes(G4, "7"):
        time = 1.5
        note_obj = Note(note, 80, time, time + 0.1)
        piano.notes.append(note_obj)

    # Bar 3: A7
    for note in chord_notes(A4, "7"):
        time = 3.0
        note_obj = Note(note, 80, time, time + 0.1)
        piano.notes.append(note_obj)

    # Bar 4: D7
    for note in chord_notes(D4, "7"):
        time = 4.5
        note_obj = Note(note, 80, time, time + 0.1)
        piano.notes.append(note_obj)

# --- SAX: You (Tenor, haunting motif: D4 - F4 - E4 - D4, start then leave it) ---
def add_sax():
    # Motif: D4 -> F4 -> E4 -> D4
    # Play first two notes, leave the last two for the end

    # First two notes
    note1 = Note(D4, 100, 0, 0.2)
    note2 = Note(F4, 100, 0.2, 0.4)
    sax.notes.append(note1)
    sax.notes.append(note2)

    # Last two notes in the 4th bar
    # Wait until the end of the 4th bar to play
    note3 = Note(E4, 100, 4.5, 4.7)
    note4 = Note(D4, 100, 4.7, 4.9)
    sax.notes.append(note3)
    sax.notes.append(note4)

# --- Main execution ---
add_drums()
add_bass()
add_piano()
add_sax()

# Save the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file saved as 'jazz_intro.mid'")
