
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
TPQ = 480  # ticks per quarter note
TIME_SIGNATURE = (4, 4)
KEY = 'F'  # F Major
BAR_LENGTH = 60 / BPM * TPQ  # 6 seconds for 4 bars
NOTE_DURATION = 0.5  # in seconds (~1 beat)

# MIDI file setup
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM, time_signature=(4, 4))

# Define instruments
drums = Instrument(program=Program.DRUMS, name="Drums")
bass = Instrument(program=Program.ELECTRIC_BASS, name="Bass")
piano = Instrument(program=Program.ELECTRIC_PIANO_1, name="Piano")
sax = Instrument(program=Program.TENOR_SAX, name="Tenor Sax")

pm.instruments = [drums, bass, piano, sax]

# =================== DRUMS (Bar 1) ===================
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every 8th
def add_drums():
    for bar in range(1):
        for beat in [0, 2]:  # 1 and 3
            kick = Note(36, 0, NOTE_DURATION * TPQ)
            kick.start = bar * BAR_LENGTH + beat * NOTE_DURATION * TPQ
            drums.notes.append(kick)
        for beat in [1, 3]:  # 2 and 4
            snare = Note(38, 0, NOTE_DURATION * TPQ)
            snare.start = bar * BAR_LENGTH + beat * NOTE_DURATION * TPQ
            drums.notes.append(snare)
        for eighth in range(8):
            hihat = Note(42, 0, 0.25 * TPQ)
            hihat.start = bar * BAR_LENGTH + eighth * 0.25 * TPQ
            drums.notes.append(hihat)

add_drums()

# =================== BASS LINE (Bars 2–4) ===================
def add_bass():
    # Walking line with chromatic approach
    # F - G - Ab - A - Bb - B - C - D - Eb - F
    # Fmaj7 -> G7 -> C7 -> Ab7 -> Fmaj7
    notes = [71, 72, 70, 71, 69, 71, 72, 74, 71, 71]  # F, G, Ab, A, Bb, B, C, D, Eb, F
    for i, pitch in enumerate(notes):
        note = Note(pitch, 0, NOTE_DURATION * TPQ)
        note.start = (i % 4) * BAR_LENGTH / 4  # every 1/4 bar
        note.start += 1 * BAR_LENGTH  # start at bar 2
        bass.notes.append(note)

add_bass()

# =================== PIANO (Bars 2–4) ===================
def add_piano():
    # 7th chords on 2 and 4
    # Bars 2–4: F7, G7, C7, Ab7
    # On beat 2 and 4
    chords = [
        [64, 67, 69, 72],  # F7 (F, A, C, E)
        [67, 71, 72, 76],  # G7 (G, B, D, F)
        [64, 68, 72, 76],  # C7 (C, E, G, B)
        [71, 74, 76, 79],  # Ab7 (Ab, C, Eb, Gb)
    ]
    for bar, chord in enumerate(chords):
        for note in chord:
            n = Note(note, 100, 0.5 * TPQ)
            n.start = bar * BAR_LENGTH + 1 * NOTE_DURATION * TPQ  # beat 2
            piano.notes.append(n)
            n = Note(note, 100, 0.5 * TPQ)
            n.start = bar * BAR_LENGTH + 3 * NOTE_DURATION * TPQ  # beat 4
            piano.notes.append(n)

add_piano()

# =================== SAX (Bars 2–4) ===================
def add_sax():
    # Motive: F - Bb - Ab - G (hanging on G), then resolves to F again
    # Start on bar 2
    note1 = Note(71, 100, 0.375 * TPQ)  # F
    note1.start = 1 * BAR_LENGTH
    sax.notes.append(note1)
    note2 = Note(69, 100, 0.375 * TPQ)  # Bb
    note2.start = 1 * BAR_LENGTH + 0.375 * TPQ
    sax.notes.append(note2)
    note3 = Note(70, 100, 0.375 * TPQ)  # Ab
    note3.start = 1 * BAR_LENGTH + 0.75 * TPQ
    sax.notes.append(note3)
    note4 = Note(71, 100, 0.25 * TPQ)  # G (hang)
    note4.start = 1 * BAR_LENGTH + 1.125 * TPQ
    sax.notes.append(note4)
    # Resolution: F in the next bar
    note5 = Note(71, 100, 0.25 * TPQ)
    note5.start = 2 * BAR_LENGTH
    sax.notes.append(note5)

add_sax()

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
