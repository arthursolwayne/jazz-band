
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm7, chromatic approaches, no repeat notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=35, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=33, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=80, pitch=32, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=31, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=30, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=29, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=28, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=27, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=26, start=5.625, end=6.0),   # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) - 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Eb
    # Bar 3: Fm7 (F, Ab, C, Eb) - 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    # Bar 4: Fm7 (F, Ab, C, Eb) - 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone - motif in Fm, short, singable, one phrase
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Gb, C, Ab
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Gb (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),  # Ab (hold)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),    # F (return)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),   # F (hold)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # Gb (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # Ab (hold)
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),    # F (return)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),   # F (hold)
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),  # Gb (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.25),  # Ab (hold)
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),    # F (return)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),   # F (hold)
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # Gb (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.125, end=5.25),  # Ab (hold)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),    # F (return)
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.625),   # F (hold)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.875),  # Gb (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('waynes_intro.mid')
