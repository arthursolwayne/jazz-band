
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2 to C3, MIDI 53 to 60), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=54, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F2 (root)

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),  # C3 (root)
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # D3 (fifth)
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),  # C3 (root)

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # D5
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # Ab4
]

# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875), # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # G5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D5
]

for note in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(note)

# You: Tenor sax, short motif, start it, leave it hanging, finish it
# Motif: F4 (65), Ab4 (60), F4 (65), Bb4 (62), rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4 (return)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Bb4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums bar 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
for i in range(2):
    kick_start = 1.5 + i * 1.5
    snare_start = 1.875 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Hihat every 8th in bars 2-4
for i in range(2):
    for j in range(4):
        start = 1.5 + i * 1.5 + j * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=6.0)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
