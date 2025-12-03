
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2, G2, Ab2, A2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=3.0),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif - F, Ab, Bb, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line (Bb2, B2, C2, D2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=4.5),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif - Bb, D, F, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line (Eb2, F2, G2, Ab2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif - Eb, G, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
for bar in [3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=90, pitch=36, start=bar, end=bar + 0.375),
        pretty_midi.Note(velocity=90, pitch=38, start=bar + 0.375, end=bar + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=bar, end=bar + 1.5),
        pretty_midi.Note(velocity=90, pitch=36, start=bar + 0.75, end=bar + 1.125),
        pretty_midi.Note(velocity=90, pitch=38, start=bar + 1.125, end=bar + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
