
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet enters

# Bass line - walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone motif - short, melodic, Dm scale
# Motif: D, Eb, F, G (starting on beat 2 of bar 2)
sax_notes = [
    # Bar 2: D (beat 2)
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),
    # Bar 3: Eb (beat 2)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),
    # Bar 4: F (beat 2)
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),
    # Bar 4: G (beat 3)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625)
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fills for bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
