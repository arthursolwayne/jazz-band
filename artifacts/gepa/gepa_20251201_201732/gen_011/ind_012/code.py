
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, C, D
# Bar 2: Ab (VII), C (III), F (I), Bb (bVI) with chromatic approach to C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # Bb (approach to C)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif: F (1.5), Ab (1.875), C (2.25), Ab (2.625)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=48, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=48, start=2.625, end=3.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full ensemble
# Bass: Fm7 (F, Ab, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation: F (3.0), C (3.375), F (3.75), Eb (4.125)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=46, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full ensemble
# Bass: Cm7 (C, Eb, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=6.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),   # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution: F (4.5), C (4.875), F (5.25), C (5.625)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=52, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Bar 2
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.0, end=start_time + 1.5),    # Hihat every 8th
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),  # Kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

    # Bar 3
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.5, end=start_time + 1.875),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start_time + 2.25, end=start_time + 2.625), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.5, end=start_time + 3.0),    # Hihat every 8th
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.875, end=start_time + 2.25),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.25, end=start_time + 2.625),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.625, end=start_time + 3.0),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 2.625, end=start_time + 3.0),  # Kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

    # Bar 4
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 3.0, end=start_time + 3.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start_time + 3.75, end=start_time + 4.125), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.0, end=start_time + 4.5),    # Hihat every 8th
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.375, end=start_time + 3.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.75, end=start_time + 4.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.125, end=start_time + 4.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 4.125, end=start_time + 4.5),  # Kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

add_drums(1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
