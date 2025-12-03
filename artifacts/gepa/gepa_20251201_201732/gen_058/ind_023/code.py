
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (D Major)
key = 'D'

# Time per bar in seconds (160 BPM, 4/4)
time_per_bar = 60 / 160 * 4  # 6 seconds per 4 bars
time_per_beat = 60 / 160  # 0.375 seconds per beat

# Create instruments
instrument_list = []

# ------------------------ Marcus on Bass (D2-G2, roots and fifths with chromatic approaches)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Bar 1: Rest (no bass)
# Bar 2: D (root), B (fifth) with chromatic approach
# Bar 3: E (root), C# (fifth), with chromatic approach
# Bar 4: F# (root), D (fifth) with chromatic approach
# Times: 0-6 seconds (4 bars)

note_map = {
    # Bar 1: Rest
    0: [],
    # Bar 2: D2 (D), B2 (B), with chromatic approach on D2 (C#2)
    1: [pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6),  # C#2 (chromatic approach)
        pretty_midi.Note(velocity=100, pitch=64, start=1.6, end=2.0),  # D2 (root)
        pretty_midi.Note(velocity=100, pitch=69, start=1.6, end=2.0),  # B2 (fifth)
        pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.1),  # B2 (chromatic exit)],
    # Bar 3: E2 (E), C#3 (C#), with chromatic approach on E2 (D2)
    2: [pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.1),  # D2 (chromatic approach)
        pretty_midi.Note(velocity=100, pitch=62, start=3.1, end=3.5),  # E2 (root)
        pretty_midi.Note(velocity=100, pitch=72, start=3.1, end=3.5),  # C#3 (fifth)
        pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.6),  # C#3 (chromatic exit)],
    # Bar 4: F#2 (F#), D3 (D), with chromatic approach on F#2 (G2)
    3: [pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.6),  # G2 (chromatic approach)
        pretty_midi.Note(velocity=100, pitch=69, start=4.6, end=5.0),  # F#2 (root)
        pretty_midi.Note(velocity=100, pitch=76, start=4.6, end=5.0),  # D3 (fifth)
        pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.1),  # D3 (chromatic exit)],
}

for bar_index, notes in note_map.items():
    for note in notes:
        bass.notes.append(note)

instrument_list.append(bass)

# ------------------------ Diane on Piano (Open voicings, different chord each bar, resolve on last)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Bar 1: Rest
# Bar 2: Dmaj7 (D, F#, A, C#) - comp on 2 and 4
# Bar 3: Em7 (E, G, B, D) - comp on 2 and 4
# Bar 4: F#m7 (F#, A, C#, E) - comp on 2 and 4
# Each chord is played on beat 2 and 4, with open voicings

note_map = {
    # Bar 2: Dmaj7 (beat 2 & 4)
    1: [
        pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # D4
        pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # F#4
        pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=1.875),  # A4
        pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=1.875),  # C#5,
        pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # D4
        pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),  # F#4
        pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.375),  # A4
        pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.375),  # C#5
    ],
    # Bar 3: Em7 (beat 2 & 4)
    2: [
        pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # E4
        pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),  # G4
        pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=2.875),  # B4
        pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=2.875),  # D5
        pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.375),  # E4
        pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.375),  # G4
        pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.375),  # B4
        pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.375),  # D5
    ],
    # Bar 4: F#m7 (beat 2 & 4)
    3: [
        pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),  # F#4
        pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=3.875),  # A4
        pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=3.875),  # B4
        pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=3.875),  # D5
        pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),  # F#4
        pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.375),  # A4
        pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.375),  # B4
        pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.375),  # D5
    ],
}

for bar_index, notes in note_map.items():
    for note in notes:
        piano.notes.append(note)

instrument_list.append(piano)

# ------------------------ Little Ray on Drums (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drum_program)

# Map drum pitches (MIDI note numbers)
# Kick: 36
# Snare: 38
# Hihat: 42

# Bar 1: Kick on 1, snare on 2, hihat on every eighth
# Bar 2: Kick on 1, snare on 2, hihat on every eighth
# Bar 3: Kick on 1, snare on 2, hihat on every eighth
# Bar 4: Kick on 1, snare on 2, hihat on every eighth

# Define the timing for each beat
for bar in range(4):
    bar_start = bar * 1.5
    # Kick on 1
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Kick on 3
    kick_start = bar_start + 0.75
    kick_end = kick_start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2
    snare_start = bar_start + 0.375
    snare_end = snare_start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Snare on 4
    snare_start = bar_start + 1.125
    snare_end = snare_start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every eighth
    for i in range(8):
        hihat_start = bar_start + (i * 0.375)
        hihat_end = hihat_start + 0.05
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

instrument_list.append(drums)

# ------------------------ Dante on Tenor Sax (Melody: short motif, sing, leave it hanging, come back)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

# Tenor sax motif — D4 (D), F#4 (F#), E4 (E), D4 (D) — short, sing, leave hanging
# Start on beat 1 of bar 2 (1.5 seconds)
# D4 (D), F#4 (F#), E4 (E), D4 (D)

# Bar 2: Motif (play on beat 1, rest on beat 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),   # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D4
]

# Bar 4: Return with a twist — D4 (D), F#4 (F#), G4 (G), A4 (A) — a new resolution
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),   # A4
])

for note in sax_notes:
    sax.notes.append(note)

instrument_list.append(sax)

# Add all instruments to the MIDI file
for instrument in instrument_list:
    pm.instruments.append(instrument)

# Write the MIDI file
pm.write("dante_intro.mid")
