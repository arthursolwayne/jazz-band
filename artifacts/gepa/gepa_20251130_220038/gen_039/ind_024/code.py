
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # E
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (71), Ab (73), Bb (72), C (77)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=73, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=73, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=73, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat_eighths = [
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + (i + 1) * 0.375)
        for i in range(4)
    ]
    for note in [kick1, snare2, kick3, snare4] + hihat_eighths:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
