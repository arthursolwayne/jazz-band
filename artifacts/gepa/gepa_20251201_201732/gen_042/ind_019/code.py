
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
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line - F2, G2, Ab2, A2 (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # A2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm9 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),    # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),    # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),    # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),    # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 2: Sax motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line - Bb2, B2, C2, Db2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # Db2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),    # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),    # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),    # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax - continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line - Eb2, F2, G2, Ab2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),    # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),    # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),    # Db
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=58, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
