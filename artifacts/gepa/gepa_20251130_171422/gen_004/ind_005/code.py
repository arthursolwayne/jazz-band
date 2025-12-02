
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file with 4 bars in D minor at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time per bar: 60 / 160 * 4 = 1.5 seconds
# Time per beat: 0.375 seconds

# Duration of the piece in seconds
duration = 6.0

# Create a time grid (in seconds)
bar_lengths = 4 * [1.5]  # 4 bars

# Create instruments
drums = Instrument(program=Program.DRUM_SET, is_drum=True)
bass = Instrument(program=Program.BASS_GUITAR_FINGERSTYLE)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
sax = Instrument(program=Program.TENOR_SAX)

# Define note events
def add_note(instrument, note, time, duration, velocity=100):
    note_obj = Note(note, time, duration, velocity)
    instrument.notes.append(note_obj)

# ---------------------------
# DRUMS (Bar 1: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th)
# BAR 1: 0.0 to 1.5 seconds
drum_map = {
    'kick': 36, 'snare': 38, 'hihat': 42
}

# Bar 1: Drums only
# Kick on 1 and 3 (beat 0 and 2)
add_note(drums, drum_map['kick'], 0.0, 0.1)
add_note(drums, drum_map['kick'], 0.75, 0.1)

# Snare on 2 and 4 (beat 1 and 3)
add_note(drums, drum_map['snare'], 0.375, 0.1)
add_note(drums, drum_map['snare'], 1.125, 0.1)

# Hihat on every 8th (0, 0.375, 0.75, 1.125)
for i in range(4):
    add_note(drums, drum_map['hihat'], i * 0.375, 0.1)

# ---------------------------
# BASS (Bar 1: Walking line, chromatic approaches)
# Bar 2: Enters with walking line in D minor
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Chromatic passing tones between notes

# Bar 2 to 4 (Time 1.5 to 6.0)
bass_notes = [
    # Bar 2: D, Eb, F, G
    (62, 1.5), (63, 1.875), (65, 2.25), (67, 2.625),
    # Bar 3: Ab, Bb, C, D
    (64, 3.0), (65, 3.375), (67, 3.75), (69, 4.125),
    # Bar 4: Eb, F, G, Ab
    (63, 4.5), (65, 4.875), (67, 5.25), (64, 5.625)
]

for note, time in bass_notes:
    add_note(bass, note, time, 0.1, velocity=75)

# ---------------------------
# PIANO (Bars 2–4: 7th chords, on 2 and 4)
# Dm7: D, F, A, C
# Gm7: G, Bb, D, F
# Am7: A, C, E, G
# Cm7: C, Eb, G, Bb

# Bar 2 (Time 1.5–2.0): Dm7 on beat 2 (1.875)
# Bar 2: Dm7
add_note(piano, 62, 1.875, 0.25, 90)  # D
add_note(piano, 65, 1.875, 0.25, 80)  # F
add_note(piano, 67, 1.875, 0.25, 70)  # A
add_note(piano, 69, 1.875, 0.25, 60)  # C

# Bar 3 (Time 3.0–3.5): Gm7 on beat 2 (3.375)
# Bar 3: Gm7
add_note(piano, 67, 3.375, 0.25, 90)  # G
add_note(piano, 69, 3.375, 0.25, 80)  # Bb
add_note(piano, 72, 3.375, 0.25, 70)  # D
add_note(piano, 74, 3.375, 0.25, 60)  # F

# Bar 4 (Time 4.5–5.0): Am7 on beat 2 (4.875)
# Bar 4: Am7
add_note(piano, 69, 4.875, 0.25, 90)  # A
add_note(piano, 72, 4.875, 0.25, 80)  # C
add_note(piano, 74, 4.875, 0.25, 70)  # E
add_note(piano, 76, 4.875, 0.25, 60)  # G

# ---------------------------
# SAX (Bars 2–4: Short motif with space and tension)
# Melody: D (62) -> Eb (63) -> F (65) -> G (67) -> Ab (64) -> D (62)
# D, Eb, F, G, Ab, D — spaced out with rests

sax_notes = [
    (62, 2.25, 0.25),  # D
    (63, 2.75, 0.25),  # Eb
    (65, 3.25, 0.25),  # F
    (67, 3.75, 0.25),  # G
    (64, 4.25, 0.25),  # Ab
    (62, 4.75, 0.25)   # D
]

for note, time, duration in sax_notes:
    add_note(sax, note, time, duration, velocity=100)

# ---------------------------
# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_russo_intro.mid")
