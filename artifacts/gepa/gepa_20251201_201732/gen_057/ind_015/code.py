
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹=1)]

# Define key: F minor
key = 'Fm'

# Create instruments
instruments = {
    'bass': Instrument(program=Program.BASS_GUITAR_FINGER_STYLE, is_drum=False),
    'piano': Instrument(program=Program.ELECTRIC_PIANO_1, is_drum=False),
    'drums': Instrument(program=Program.DRUMS, is_drum=True),
    'sax': Instrument(program=Program.SAXOPHONE_ALTO, is_drum=False)
}

pm.instruments = list(instruments.values())

# --- Bass Line: Marcus (Walking line with chromatic approaches, roots and fifths)
# Bar 1: Empty
# Bar 2: Fm (F, C), chromatic approach to F
# Bar 3: Gm7 (G, D), chromatic approach to G
# Bar 4: Am7 (A, E), chromatic approach to A

# Bar 2
bass_notes = [
    Note(velocity=90, pitch=43, start=1.5, end=1.75),  # C (root)
    Note(velocity=90, pitch=40, start=1.75, end=2.0)   # F (fifth, chromatic approach)
]

# Bar 3
bass_notes.extend([
    Note(velocity=90, pitch=46, start=3.0, end=3.25),  # D (root of Gm7)
    Note(velocity=90, pitch=43, start=3.25, end=3.5)   # G (fifth, chromatic approach)
])

# Bar 4
bass_notes.extend([
    Note(velocity=90, pitch=47, start=4.5, end=4.75),  # E (root of Am7)
    Note(velocity=90, pitch=44, start=4.75, end=5.0)   # A (fifth, chromatic approach)
])

instruments['bass'].notes = bass_notes

# --- Piano: Diane (Open voicings, different chords each bar, comp on 2 and 4)
# Bar 1: Empty
# Bar 2: Fm7 (F, Am, D, G)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Am7 (A, C, E, G)

# Bar 2 (Fm7)
piano_notes = [
    Note(velocity=100, pitch=43, start=1.5, end=1.75),  # F
    Note(velocity=100, pitch=51, start=1.5, end=1.75),  # A
    Note(velocity=100, pitch=48, start=1.5, end=1.75),  # D
    Note(velocity=100, pitch=50, start=1.5, end=1.75)   # G
]

# Bar 3 (Gm7)
piano_notes.extend([
    Note(velocity=100, pitch=46, start=3.0, end=3.25),  # G
    Note(velocity=100, pitch=44, start=3.0, end=3.25),  # Bb
    Note(velocity=100, pitch=48, start=3.0, end=3.25),  # D
    Note(velocity=100, pitch=43, start=3.0, end=3.25)   # F
])

# Bar 4 (Am7)
piano_notes.extend([
    Note(velocity=100, pitch=47, start=4.5, end=4.75),  # A
    Note(velocity=100, pitch=49, start=4.5, end=4.75),  # C
    Note(velocity=100, pitch=52, start=4.5, end=4.75),  # E
    Note(velocity=100, pitch=50, start=4.5, end=4.75)   # G
])

instruments['piano'].notes = piano_notes

# --- Drums: Little Ray (Kick on 1 & 3, snare on 2 & 4, hihat on every eighth)
# Bar 1: Kick on 1, hihat on all eighths
# Bar 2: Kick on 1, snare on 2, hihat on all eighths
# Bar 3: Kick on 1, snare on 2, hihat on all eighths
# Bar 4: Kick on 1, snare on 2, hihat on all eighths

# Create a helper function for drum hits
def add_drum_hit(note_number, time, duration):
    note = Note(velocity=100, pitch=note_number, start=time, end=time + duration)
    instruments['drums'].notes.append(note)

# Bar 1
add_drum_hit(36, 0.0, 0.125)            # Kick
add_drum_hit(42, 0.0, 0.125)            # Hihat
add_drum_hit(42, 0.125, 0.125)
add_drum_hit(42, 0.25, 0.125)
add_drum_hit(42, 0.375, 0.125)
add_drum_hit(42, 0.5, 0.125)
add_drum_hit(42, 0.625, 0.125)
add_drum_hit(42, 0.75, 0.125)

# Bar 2
add_drum_hit(36, 1.5, 0.125)            # Kick
add_drum_hit(38, 1.75, 0.125)           # Snare
add_drum_hit(42, 1.5, 0.125)            # Hihat
add_drum_hit(42, 1.625, 0.125)
add_drum_hit(42, 1.75, 0.125)
add_drum_hit(42, 1.875, 0.125)
add_drum_hit(42, 2.0, 0.125)
add_drum_hit(42, 2.125, 0.125)
add_drum_hit(42, 2.25, 0.125)
add_drum_hit(42, 2.375, 0.125)

# Bar 3
add_drum_hit(36, 3.0, 0.125)            # Kick
add_drum_hit(38, 3.25, 0.125)           # Snare
add_drum_hit(42, 3.0, 0.125)            # Hihat
add_drum_hit(42, 3.125, 0.125)
add_drum_hit(42, 3.25, 0.125)
add_drum_hit(42, 3.375, 0.125)
add_drum_hit(42, 3.5, 0.125)
add_drum_hit(42, 3.625, 0.125)
add_drum_hit(42, 3.75, 0.125)
add_drum_hit(42, 3.875, 0.125)

# Bar 4
add_drum_hit(36, 4.5, 0.125)            # Kick
add_drum_hit(38, 4.75, 0.125)           # Snare
add_drum_hit(42, 4.5, 0.125)            # Hihat
add_drum_hit(42, 4.625, 0.125)
add_drum_hit(42, 4.75, 0.125)
add_drum_hit(42, 4.875, 0.125)
add_drum_hit(42, 5.0, 0.125)
add_drum_hit(42, 5.125, 0.125)
add_drum_hit(42, 5.25, 0.125)
add_drum_hit(42, 5.375, 0.125)

# --- Sax: You (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)

# Bar 1: Little Ray alone. No sax. Just space. Let it breathe.

# Bar 2: Start of motif
# (F - Ab - Bb - rest)
sax_notes = [
    Note(velocity=100, pitch=43, start=1.5, end=1.625),  # F
    Note(velocity=100, pitch=41, start=1.625, end=1.75),  # Ab
    Note(velocity=100, pitch=42, start=1.75, end=1.875),  # Bb
    # Leave it hanging. Silence from 1.875 to 2.0
]

# Bar 3: Continue the motif
# (rest - F - rest - rest)
# No notes from 2.0 to 2.25
# Then F at 2.25, but only half a note
sax_notes.append(Note(velocity=100, pitch=43, start=2.25, end=2.5))

# Bar 4: Complete the motif
# (Ab - Bb - F - rest)
sax_notes.extend([
    Note(velocity=100, pitch=41, start=4.5, end=4.625),  # Ab
    Note(velocity=100, pitch=42, start=4.625, end=4.75),  # Bb
    Note(velocity=100, pitch=43, start=4.75, end=5.0)     # F
])

instruments['sax'].notes = sax_notes

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
