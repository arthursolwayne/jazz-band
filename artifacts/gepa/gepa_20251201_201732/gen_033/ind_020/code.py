
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

# Drums: Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
# D2-G2, roots and fifths with chromatic approaches
# Bar 2: D2 (root), Eb2 (chromatic), G2 (fifth), F2 (chromatic)
# Bar 3: A2 (root), Bb2 (chromatic), D3 (fifth), C#2 (chromatic)
# Bar 4: B2 (root), C2 (chromatic), F2 (fifth), E2 (chromatic)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0), # F2

    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375), # A2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5), # C#2

    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875), # B2
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0), # E2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: G7 (G, B, D, F)
# Bar 4: A7 (A, C#, E, G)

# Bar 2 (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0), # C#4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5), # F4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0), # C#5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0), # E5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0), # G5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (start), F#4 (chromatic), A4 (fifth), then leave it hanging on A4
# Then come back on the third bar and end with a C#4 followed by a D4

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # A4 (hold)

    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # C#4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)) # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375)) # Snare

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)) # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375)) # Snare

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)) # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375)) # Snare

# Add hihat on every eighth
for i in range(12):
    start = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
