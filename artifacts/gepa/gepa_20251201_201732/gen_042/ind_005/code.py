
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # Eb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving on beat 4
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Eb4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Fm, short and singable, leaves it hanging
# Fm7 (F, Ab, C, Eb) -> Gm7 (G, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.4375),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=2.4375, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.8125, end=3.0),  # F4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # Eb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving on beat 4
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation, resolve on beat 4
# Fm7 -> Gm7 -> Am7 (A, C, E, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.9375),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125), # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # E5
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.5),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # Eb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving on beat 4
# Bar 4: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif completion, resolve on beat 4
# Am7 (A, C, E, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # E5
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.8125, end=6.0),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar_start in [3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
