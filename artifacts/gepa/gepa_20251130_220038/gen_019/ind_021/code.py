
import pretty_midi

# Initialize the MIDI file with the tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# --- Bar 1: Little Ray alone (0.0 - 1.5s) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:  # beats 1 and 3 in 4/4
    kick_time = beat * 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)

for beat in [1, 3]:  # beats 2 and 4
    snare_time = beat * 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)

# Hi-hats on every eighth note
for beat in range(8):
    hihat_time = beat * 0.125
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
    drums.notes.append(hihat)

# --- Bars 2-4: Full quartet (1.5 - 6.0s) ---

# D Major key: D, E, F#, G, A, B, C#
# Time signature: 4/4
# Bar length: 1.5 seconds (60 / 160 = 0.375s per beat, 4 beats = 1.5s)

# --- DRUMS for bars 2-4 ---
for bar in range(2, 5):
    start = bar * 0.375  # in seconds
    for beat in [0, 2]:  # beats 1 and 3
        kick_time = start + beat * 0.375
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
        drums.notes.append(kick)
    for beat in [1, 3]:  # beats 2 and 4
        snare_time = start + beat * 0.375
        snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
        drums.notes.append(snare)
    for beat in range(8):
        hihat_time = start + beat * 0.125
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(hihat)

# --- BASS LINE (Marcus) ---
# Walking line in D major, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2: D (root), F# (3rd), G (4th), A (5th)
    # Chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D (62)
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=1.875),  # F# (63)
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.125),  # G (64)
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),  # A (65)

    # Bar 3: A (5th), D (root), B (7th), D (root)
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.625),  # A (65)
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=2.875),  # D (62)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),  # B (67)
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.375),  # D (62)

    # Bar 4: C# (chromatic approach to D), D (root), F# (3rd), G (4th)
    pretty_midi.Note(velocity=80, pitch=61, start=3.5, end=3.625),  # C# (61)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.875),  # D (62)
    pretty_midi.Note(velocity=80, pitch=63, start=4.0, end=4.125),  # F# (63)
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.375),  # G (64)
]

bass.notes.extend(bass_notes)

# --- PIANO (Diane) ---
# 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# A7: A, C#, E, G
# B7: B, D#, F#, A

# Bar 2: D7 on beat 2, G7 on beat 4
piano_notes = []
for beat in [1, 3]:  # beats 2 and 4
    start = 1.5 + beat * 0.375
    if beat == 1:
        # D7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.125))  # D (62)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=start, end=start + 0.125))  # F# (63)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=start, end=start + 0.125))  # A (65)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=start, end=start + 0.125))  # C (60)
    else:
        # G7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.125))  # G (67)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.125))  # B (69)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.125))  # D (62)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=start, end=start + 0.125))  # F (64)

# Bar 3: A7 on beat 2, B7 on beat 4
for beat in [1, 3]:
    start = 2.5 + beat * 0.375
    if beat == 1:
        # A7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=start, end=start + 0.125))  # A (65)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.125))  # C# (67)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.125))  # E (69)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.125))  # G (67)
    else:
        # B7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.125))  # B (69)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=start, end=start + 0.125))  # D# (71)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.125))  # F# (67)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=start, end=start + 0.125))  # A (65)

# Bar 4: D7 on beat 2, G7 on beat 4
for beat in [1, 3]:
    start = 3.5 + beat * 0.375
    if beat == 1:
        # D7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.125))  # D (62)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=start, end=start + 0.125))  # F# (63)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=start, end=start + 0.125))  # A (65)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=start, end=start + 0.125))  # C (60)
    else:
        # G7
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.125))  # G (67)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.125))  # B (69)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.125))  # D (62)
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=start, end=start + 0.125))  # F (64)

piano.notes.extend(piano_notes)

# --- SAX (Dante) ---
# One short motif: D (62), F# (63), G (64), A (65) — start on beat 2 of bar 2, leave it hanging, come back to finish it in bar 4

# Bar 2, beat 2: D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.125),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # A (leaving it hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),  # D (coming back)
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.375),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # A (finishing it)
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("dante_introduction.mid")
